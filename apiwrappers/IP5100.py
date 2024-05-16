# IP5100.py - IP5100 Python Module
# Version 1.0

from telnetlib import Telnet
import re
from webbrowser import get


# Helper functions
def string_to_dict(input_string):
    """
    Convert a string of key-value pairs to a dictionary.

    :param input_string: A string containing key-value pairs separated by '=' or ':'.
    :return: A dictionary representation of the input string.
    """
    try:
        # Split the string into lines
        lines = input_string.split("\n")

        # Split each line into a key-value pair and add it to the dictionary
        result_dict = {}
        for line in lines:
            separator = "=" if "=" in line else ":"
            if separator in line:
                key, value = line.split(
                    separator, 1
                )  # Only split on the first occurrence of the separator
                # Strip whitespace and carriage return characters from the key and value
                key = key.strip()
                value = value.strip().rstrip("\r")
                result_dict[key] = value

        return result_dict
    except Exception as e:
        print(f"Error converting string to dictionary: {e}")
        return {}


def format_pretty_audio_info(audio_info):
    # Extract the type and clean it by removing all text within parentheses and extracting channel info if present
    type_match = re.search(r"^(.*?)(?: \[.*\])?(?: \(.*\))?$", audio_info["Type"])
    audio_type = type_match.group(1) if type_match else audio_info["Type"]

    # Check for channel info in the type field
    channel_info_match = re.search(r"\[(.*?) Ch\]", audio_info["Type"])
    if channel_info_match:
        channel_info = (
            channel_info_match.group(1) + "Ch"
        )  # Appends 'Ch' directly to the number
    else:
        channel_info = (
            audio_info["Valid Ch"].split(" ")[0] + "Ch"
        )  # Adds 'Ch' if only a number is provided

    # Clean up frequency and sample size
    freq = audio_info["Sample Freq"].replace(" ", "")
    size = audio_info["Sample Size"].replace(" ", "")

    # Format the final string
    pretty_string = f"{channel_info} {audio_type} {freq} {size}"

    return pretty_string


class IP5100:
    """Python class for controlling the IP5100 encoder/decoder via Telnet."""

    def __init__(self, host, port=24, timeout=3, login="root"):
        """Create the class using the IP address, port, and login credentials."""
        self.host = host
        self.port = port
        self.timeout = timeout
        self.login = login
        self.tn = None

        self.model = None
        self.mac = None
        self.trueName = None
        self.alias = None

        self.connected = False
        self.get_info()

        self.url = f"http://{self.host}/settings.html"
        self.stream = f"http://{self.host}:8080/?action=stream"

    def __str__(self):
        return f"{self.trueName} - {self.alias} - {self.host} - {self.version} - {self.mac}"

    def connect(self):
        """
        Attempts to connect to the device, handling cases where the device might be offline or not responding.
        """
        if self.tn is None:
            self.tn = Telnet()
            # self.tn.set_debuglevel(1)  # Enable Telnet debug mode
        try:
            self.tn.open(self.host, self.port, timeout=1.0)
            response = self.tn.read_until(b"login:")
            # if not self.connected:
            #     response = response.decode().strip()
            #     self.trueName = response.replace(" login:", "")
            #     self.model = self.trueName.split("-")[1]

            self.tn.write(self.login.encode() + b"\r\n")
            self.tn.read_until(b"/ #")
            self.connected = True
            return True
        except Exception as e:
            print(f"Failed to connect to {self.host}. Error: {e}")
            self.tn = None  # Reset the connection
            return False

    def ensure_connection(self):
        """
        Ensures that the device is connected before sending commands.
        """
        if self.tn is None or self.tn.get_socket() is None:
            return self.connect()
        return True

    def send(self, message: str) -> str:
        """
        Sends a message to the Controller and returns the response, ensuring the device is connected.
        Includes a retry mechanism if the initial send fails due to a connection issue.
        """
        retry_attempts = 2  # Number of retry attempts
        for attempt in range(retry_attempts):
            if not self.ensure_connection():
                print(
                    f"Attempt {attempt + 1}: Unable to send command to {self.host}, device is not connected."
                )
                continue

            try:
                message_bytes = f"{message}\n".encode()
                self.tn.write(message_bytes)
                stdout = self.tn.read_until(b"/ #").decode()
                response = stdout.strip("/ #")
                if response.startswith(message):
                    response = response[len(message) :].strip()
                return response
            except Exception as e:
                print(
                    f"Attempt {attempt + 1}: Failed to send command to {self.host}. Error: {e}"
                )
                self.disconnect()  # Ensure disconnection before retrying
                self.tn = None  # Reset the Telnet connection

                if attempt == retry_attempts - 1:
                    return "Failed to send command after retries"

        return "Failed to establish connection"

    def disconnect(self):
        """
        Safely closes the Telnet connection if it exists.
        """
        if self.tn is not None:
            try:
                self.tn.close()
            except Exception as e:
                print(f"Error closing Telnet connection: {e}")
            finally:
                self.tn = None

    def get_info(self):
        """Gathers all device information."""
        self.get_model_version()
        self.get_alias()
        mac = self.get_mac()
        mac = mac.replace(":", "")
        self.trueName = f"{self.model}-{mac}"

    def get_model_version(self):
        """
        Get the model of the device.
        """
        response = self.send("cat /etc/version")
        lines = response.strip().split("\n")

        if len(lines) >= 2:
            self.model = lines[0].strip()
            self.version = lines[1].strip()
        else:
            self.model = None
            self.version = None
        return f"{self.model} - {self.version}"

    def get_ip_mode(self):
        """
        Get the IP mode of the device.
        """
        response = self.send("astparam g ip_mode")
        if "not defined" in response.lower():
            self.ip_mode = None
        else:
            self.ip_mode = response.strip()
        return self.ip_mode

    def get_multicast_ip(self):
        """
        Get the multicast IP of the device.
        """
        response = self.send("astparam g multicast_ip")
        if "not defined" in response.lower():
            self.multicast_ip = None
        else:
            self.multicast_ip = response.strip()
        return self.multicast_ip

    def get_subnet_mask(self):
        """
        Get the subnet mask of the device.
        """
        response = self.send("ifconfig|grep Mask|sed -n 1p|awk -F " ":" " '{print $4}'")
        if "not defined" in response.lower():
            self.netmask = None
        else:
            self.netmask = response.strip()
        return self.netmask

    def get_gateway_ip(self):
        """
        Get the gateway IP of the device.
        """
        response = self.send("route -n | grep UG | awk '{print $2}'")
        if "not defined" in response.lower():
            self.gateway_ip = None
        else:
            self.gateway_ip = response.strip()
        return self.gateway_ip

    def get_login_prompt(self):
        """
        Get the login prompt of the device.
        """
        response = self.send("")

    def dump(self):
        """
        Get all parameters from the device.
        """
        response = self.send("astparam dump")
        return string_to_dict(response)

    def flush(self):
        """
        Flush all parameters from the device.
        """
        return self.send("astparam flush")

    def save(self):
        """
        Save all parameters to the device.
        """
        return self.send("astparam save")

    def reboot(self):
        """
        Reboot the device.
        """
        self.save()
        return self.send("reboot")

    def set_astparam(self, key, value):
        """
        Set a specific astparam key-value pair.
        """
        return self.send(f"astparam s {key} {value}")

    def remove_astparam(self, key, value):
        """
        Remove a specific astparam key-value pair.
        """
        return self.send(f"astparam s {key}={value}")

    def set_no_video(self, status: bool = True):
        """
        Enable or Disable the video of the device. Unit will reboot after this command.
        True: Disable VideoIP
        False: Enable VideoIP
        """
        if status:
            return self.send("astparam s no_video y; astparam save; reboot")
        else:
            return self.send("astparam s no_video n; astparam save; reboot")

    def video_wall(self, value):
        """
        Set the video wall of the device.
        y: Enable
        n: Disable
        """
        return self.send(f"astparam s video_wall {value}")

    def set_ip(self, gateway, netmask, ipaddr):
        """
        Set the IP of the device.
        """
        response = self.send(
            f"astparam s gatewayip {gateway}; astparam s netmask {netmask}; astparam s ipaddr {ipaddr}; astparam s ip_mode static"
        )

        return response

    def set_ip_mode(self, mode):
        """
        Set the IP mode of the device.
        static
        dhcp
        auto
        """
        return self.send(f"astparam s ip_mode {mode}")

    def set_hdcp_1_4(self, value):
        """
        Set the HDCP 1.4 of the device.
        y: Enable
        n: Disable
        """
        return self.send(f"astparam s hdcp_always_on {value}")

    def set_hdcp_2_2(self, value):
        """
        Set the HDCP 2.2 of the device.
        y: Enable
        n: Disable
        """
        return self.send(f"astparam s hdcp_2_2 {value}")

    def set_hdcp(self, status: int = 1):
        """
        Set the HDCP of the device.
        0: Disabled
        1: Enabled
        """
        if status == 0:
            return self.send(f"astparam s hdcp_enable n")
        else:
            return self.send(f"astparam s hdcp_enable y")

    def set_addon(self, value):
        """
        Set the addon of the device.
        none: Disable
        dante: Enable
        """
        return self.send(f"astparam s a_addon {value}")

    def set_analog_in_volume(self, value):
        """
        Set the analog in volume of the device.
        """
        return self.send(f"echo {value} > /sys/devices/platform/1500_i2s/analog_in_vol")

    def set_analog_out_volume(self, value):
        """
        Set the analog out volume of the device.
        """
        return self.send(
            f"echo {value} > /sys/devices/platform/1500_i2s/analog_out_vol"
        )

    def set_bridge_enable(self, value):
        """
        Set the bridge of the device.
        y: Enable
        n: Disable
        """
        return self.send(f"astparam s a_bridge_en {value}")

    def set_serial_enabled(self, status: bool = True) -> str:
        """
        Set the serial of the device.
        True: Enabled
        False: Disabled
        """
        if status:
            return self.send("astparam s no_soip n")
        else:
            return self.send("astparam s no_soip y")

    def set_serial_baudrate(
        self,
        baudrate: int = 115200,
        data_bits: int = 8,
        stop_bits: int = 1,
        parity: str = "n",
    ):
        """
        Set the serial baudrate of the device.
        """
        command = f"astparam s s0_baudrate {baudrate}-{data_bits}{parity}{stop_bits}"
        return self.send(command)

    def set_serial_feedback(self, value):
        """
        Serial feedback data describe string as HEX mode or printable ASCII mode.
        y: HEX mode
        n: Printable ASCII mode
        """
        return self.send(f"astparam s soip_feedback_hex {value}")

    def set_serial_feedback_mode(self, value):
        """
        Feedback mode is get serial data to multicast group to controller
        Pass-through is tranmitting serial data between encoder and decoder

        y: Enable for feedback
        n: Disable for pass-through

        """
        return self.send(f"astparam s soip_feedback_mode {value}")

    def set_serial_feedback_wait(self, value):
        """
        Set the serial feedback wait of the device in miliseconds.
        """
        return self.send(f"astparam s soip_feedback_wait {value}")

    def send_serial_data(
        self, rs232_param, content, is_hex=False, append_cr=True, append_lf=True
    ):
        """
        Send data to serial when feedback mode is enabled.

        :param rs232_param: Format "b-dps"
            b - baud rate
            d - data bits
            p - parity
            s - stop bit
        :param content: The serial content need be sent.
        :param is_hex: Identify the "CONTENT" is a hex format description string and update the feedback hex setting as same format to controller.
        :param append_cr: append <CR> to the end of CONTENT
        :param append_lf: append <LF> after <CR> or to the end of CONTENT
        """
        # Prepare the command
        command = f'soip2 -f /dev/ttyS0 -b {rs232_param} -s "{content}"'

        # Add optional parameters
        if is_hex:
            command += " -H"
        if append_cr:
            command += " -r"
        if append_lf:
            command += " -n"

        # Send the command
        return self.send(command)

    # TODO - Add rest of the serial commands

    def set_cec_enable(self, status: bool = True):
        """
        Enable or disable CEC on the device.
        True: Enable
        False: Disable
        """
        if status:
            return self.send("astparam s no_cec n")
        else:
            return self.send("astparam s no_cec y")

    def find_me(self, time):
        """
        Find me command
        time: time in seconds
        """
        return self.send(f"e e_find_me::{time}")

    def cec_send(self, command):
        """
        Send CEC command
        """
        return self.send(f"cec_send {command}")

    def factory_reset(self):
        """
        Factory reset the device.
        """
        return self.send("reset_to_default.sh")

    def set_alias(self, value):
        """
        Set the alias of the device.
        """
        self.alias = value
        return self.send(f"astparam s name {value}; astparam save")

    def get_alias(self):
        """
        Get the alias of the device.
        """
        response = self.send("astparam g name")
        if response.startswith('"name" not defined'):
            self.alias = None
        else:
            self.alias = response
        return self.alias

    def get_mac(self):
        """
        Get the MAC address of the device.
        """
        response = self.send("gbparam r ethaddr")
        self.mac = response.strip()
        return response


class Encoder5100(IP5100):
    def __init__(self, host, port=24, timeout=3):
        """Create the class for an Encoder using the IP address, port, and login credentials."""
        super().__init__(host, port, timeout)

    @property
    def video_specs(self):
        response = self.get_video_specs()
        return response

    @video_specs.setter
    def video_specs(self, value):
        self._video_specs = value  # Set the private attribute

    def get_video_specs(self):
        """
        Get the video specs of the device.
        BR1-5100 3840x2160@60 HDR10 YCbCr_4:2:0
        """
        response = self.get_video_input_info()
        if response["hdmi in active"] == "true":
            display = f"{response['resolution']}@{response['hdmi in frame rate']} {response['hdr']} {response['color depth']}bits {response['color space']} {response['chroma sampling']}"
            return display
        else:
            return "No video signal detected"

    def set_video_quality(self, value):
        """
        Set the video quality of the device.
        -1: Auto
        0: Best
        1:
        2:
        3:
        4:
        5: Worst
        """
        return self.send(f"astparam s ast_video_quality_mode {value}")

    def switch_in(self, value):
        """
        Set the switch in of the device.
        hdmi1
        hdmi2
        usb-c
        """
        return self.send(f"e e_v_switch_in::{value}")

    def switch_mode(self, value):
        """
        Set the switch mode of the device.
        auto
        manual
        priority
        """
        return self.send(f"e e_v_switch_mode::{value}")

    def switch_priority(self, value):
        """
        Set the switch priority of the device.
        example: hdmi1::hdmi2::usb-c
        """
        return self.send(f"e e_v_switch_pri::{value}")

    def set_audio_direction(self, value):
        """
        Set analog audio as input or output, for encoder with programable analog audio connector.

        in: 3.5mm audio jack as input
        out: 3.5mm audio jack as output
        """
        return self.send(f"e e_a_direction::{value}")

    def set_audio_source(self, value):
        """
        Set the audio source of the device.
        auto: auto select analog when encoder's analog line in plugged (3.5mm socket)
        hdmi: Fixed hdmi audio
        analog: Fixed analog audio
        """
        return self.send(f"e e_a_input::{value}")

    def edid_write(self, edid):
        """
        Write EDID to the device.
        """
        return self.send(
            f'echo "{edid}" > /sys/devices/platform/videoip/eeprom_content'
        )

    def edid_read(self):
        """
        Read EDID from the device.
        """
        return self.send("cat /sys/devices/platform/videoip/edid_cache")

    def get_audio_input_info(self):
        """
        Get audio information from the device.
        """
        response = self.send("cat /sys/devices/platform/1500_i2s/input_audio_info")
        return string_to_dict(response)

    def get_video_input_info(self):
        """
        Get video information from the device.
        """
        response = self.send("gbstatus")
        return string_to_dict(response)

    @property
    def audio_specs(self):
        """Returns a string of audio information from the device."""
        response = self.get_audio_input_info()
        if response["State"] == "On":
            return format_pretty_audio_info(response)
        else:
            return "No Audio"


class Decoder5100(IP5100):
    def __init__(self, host, port=24, timeout=3):
        """Create the class for a Decoder using the IP address, port, and login credentials."""
        super().__init__(host, port, timeout)

        self.timing = {
            0: {"name": "Pass-Through", "hex": "00000000"},
            1: {"name": "Pass-Through (Strict Mode)", "hex": "10000000"},
            2: {"name": "Base on EDID", "hex": "82000000"},
            3: {"name": "Ultra HD 2160p60", "hex": "80000061"},
            4: {"name": "Ultra HD 2160p50", "hex": "80000060"},
            5: {"name": "Ultra HD 2160p30", "hex": "8000005F"},
            6: {"name": "Ultra HD 2160p25", "hex": "8000005E"},
            7: {"name": "Ultra HD 2160p24", "hex": "8000005D"},
            8: {"name": "Full HD 1080p60", "hex": "80000010"},
            9: {"name": "Full HD 1080p50", "hex": "8000001F"},
            10: {"name": "Full HD 1080p30", "hex": "80000022"},
            11: {"name": "Full HD 1080p25", "hex": "80000021"},
            12: {"name": "Full HD 1080p24", "hex": "80000020"},
            13: {"name": "HD 720p60", "hex": "80000004"},
            14: {"name": "HD 720p50", "hex": "80000013"},
            15: {"name": "HD 720p30", "hex": "8000003E"},
            16: {"name": "HD 720p25", "hex": "8000003D"},
            17: {"name": "HD 720p24", "hex": "8000003C"},
            18: {"name": "WXGA 1366x768@60", "hex": "81004048"},
            19: {"name": "WXGA+ 1440x900@60", "hex": "81004021"},
            20: {"name": "WUXGA 1920x1200@60", "hex": "81004032"},
            21: {"name": "SXGA+ 1400x1050@60", "hex": "8100401D"},
        }

    def set_ui_resolution(self, width, height, fps):
        """
        Set the UI resolution of the device.
        """
        return self.send(f"astparam s ui_default_res {width}x{height}@{fps}")

    def ui_show_text(self, status: bool = True):
        """
        Show text on the device.
        """
        if status:
            return self.send("astparam s ui_show_text y")
        else:
            return self.send("astparam s ui_show_text n")

    def set_channel(self, channel, value):
        """
        Set the channel of the device.
        a: Audio channel selection
        c: CEC channel selection (IP5100 only)
        i: ARP channel selection (IP5100 only)
        r: IR channel selection
        s: Serial channel selection
        u: USB channel selection
        v: Video channel selection
        """
        return self.send(f"astparam s ch_select_{channel} {value}")

    def set_video_genlock_scaling(self, value):
        """
        Set the video genlock scaling of the device.
        y: Enable
        n: Disable
        """
        return self.send(f"astparam s video_genlock_scaling {value}")

    def set_hdr(self, value):
        """
        Set the HDR of the device.
        0: HDR Passthrough
        n: HDR Off
        """
        return self.send(f"astparam s v_hdmi_hdr_mode {value}")

    def set_output_timing(self, value):
        """
        Set the output timing of the device.
        0: Pass-Through
        1: Pass-Through
        2: Pass-Through (Strict Mode)
        3: Base on EDID
        4: Ultra HD 2160p60
        5: Ultra HD 2160p50
        6: Ultra HD 2160p30
        7: Ultra HD 2160p25
        8: Ultra HD 2160p24
        9: Full HD 1080p60
        10: Full HD 1080p50
        11: Full HD 1080p30
        12: HD 1080p25
        13: Full HD 1080p24
        14: HD 720p60
        15: HD 720p50
        16: HD 720p30
        17: HD 720p25
        18: HD 720p24
        19: WXGA 1366x768@60
        20: WXGA+ 1440x900@60
        21: WUXGA 1920x1200@60
        22: SXGA+ 1400x1050@60

        """
        value = self.timing[value]["hex"]
        return self.send(f"astparam s v_output_timing_convert {value}")

    def set_vwall(self, value):
        """
        Set the vwall of the device.
        y: Enable
        n: Disable
        """
        return self.send(f"astparam s en_video_wall {value}")

    def set_vwall_rotate(self, value):
        """
        Set the vwall rotate of the device.
        0: No rotate
        1: Vertical flip
        2: Horizontal flip
        3: 180 degree rotation
        4: Not Used
        5: 90 degree rotation
        6: 270 degree rotation
        """

        return self.send(f"e e_vw_rotate_{value}")

    def set_vwall_stretch(self, value):
        """
        Set the vwall stretch of the device.
        1: Stretch Out
        2: Fit In
        """
        return self.send(f"astparam s vw_stretch_type {value}")

    def set_audio_out_source(self, value):
        """
        Source selection for I2S output.
        native: Native audio output
        addon: Add-on audio output (Dante)
        """
        return self.send(f"e e_a_out_src_sel::{value}")

    def cec_onetouch_play(self):
        """
        Send CEC one touch play command.
        """
        return self.send("e e_cec_one_touch_play")

    def cec_standby(self):
        """
        Send CEC standby command.
        """
        return self.send("e e_cec_system_standby")

    def set_audio_hdmi_mute(self, status: bool):
        """
        Set the audio HDMI mute of the device.
        True: Mute
        False: Unmute
        """
        if status:
            return self.send("e e_hdmi_audio_mute::y")
        else:
            return self.send("e e_hdmi_audio_mute::n")

    def edid_read(self):
        """
        Read EDID from the device.
        """
        return self.send("cat /sys/devices/platform/display/monitor_edid")

    def set_hdmi_out(self, value):
        """
        Set the HDMI out of the device.
        0: Enable
        1: Disable
        """
        return self.send(f"echo {value} > /sys/devices/platform/display/screen_off")

    def get_audio_output_info(self):
        """
        Get audio information from the device.
        """
        response = self.send("cat /sys/devices/platform/1500_i2s/output_audio_info")
        return string_to_dict(response)

    def get_video_output_info(self):
        """
        Get video information from the device.
        """
        response = self.send("gbstatus")
        return string_to_dict(response)

    def set_source(self, mac):
        """Connect to encoder with mac address or NULL to disconnect."""
        return self.send(f"gbconfig --source-select {mac}")


if __name__ == "__main__":
    ipd5100 = Decoder5100("10.0.50.30")
    ipe5100 = Encoder5100("10.0.50.27")
    ipe2 = Encoder5100("10.0.50.29")
    ipe3 = Encoder5100("10.0.50.28")

    print(ipd5100.get_model_version())
    print(ipe5100.audio_info)
    print(ipe3.audio_info)