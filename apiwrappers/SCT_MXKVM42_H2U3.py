"""
Python Wrapper for SCT_MXKVM42_H2U3
HDBaseT 4x2 Syscomtec Matrix

"""

import pexpect
import serial
import time


class SCT_MXKVM42_H2U3:
    def __init__(self, control_type, control_method: str, password) -> None:
        """Class for the 4x2 HDbaseT Matrix. Control options are RS232 or Telnet
        args:
        control_type = RS232 or Telnet
        if RS232:
            control_method = device_name ex: '/dev/ttyUSB0'
        if Telnet:
            control_method = IP address ex: '10.0.10.21'
        """
        if control_type == "RS232":
            self.control = "RS232"
            self.device = control_method
            self.rs232_baud = 115200
            self.rs232_data_bits = 8
            self.rs232_parity = "N"
            self.rs232_stop_bits = 1
            self.rs232_flow_control = "N"
            self.rs232_timeout = 1
            self.serial = serial.Serial(
                port=self.device,
                baudrate=self.rs232_baud,
                timeout=self.rs232_timeout,
                bytesize=self.rs232_data_bits,
                parity=self.rs232_parity,
                stopbits=self.rs232_stop_bits,
            )

        if control_type.lower() == "telnet":
            self.control = "telnet"
            self.ip = control_method
            self.port = 23
            self.password = password
            self.timeout = 10
            self.tn = None
            self.connect()

    def connect(self):
        """Creates Telnet connection"""
        self.tn = pexpect.spawn(f"telnet {self.ip} {self.port}")

        self.tn.expect("Password:", timeout=10)
        self.tn.sendline(self.password)
        self.tn.expect("Welcome to use matrix control system", timeout=10)

    def send_telnet(self, message) -> str:
        """Send Telnet Command and wait for response on Telnet"""
        self.tn.sendline(message)
        self.tn.expect("\r\n", timeout=10)
        response = self.tn.before.decode("utf-8").strip()
        return response

    def send_rs232(self, message) -> str:
        """Send RS232 command return response"""
        command_encoded = message.encode("ascii") + b"\r\n"
        print(f"Sent: {message}")
        self.serial.write(command_encoded)
        data = self.serial.read_until(b"\r\n")

        if not data:
            print(f"No response received within {self.rs232_timeout}s")
            return f"No response received within {self.rs232_timeout}s"
        else:
            data_decoded = data.decode("ascii")
            print(f"Received: {data_decoded}")
            return data_decoded

    def send_command(self, message):
        if self.control.lower() == "telnet":
            response = self.send_telnet(message)

        if self.control.lower() == "rs232":
            response = self.send_rs232(message)

        return response

    def set_switch_input_output(self, input, output="all"):
        """Switch input to output, if output is left blank will be sent
        to all outputs.
        input = {i00, i01, i02, i03, i04}
        output = {o01, o02, all}"""
        command = f"SET VIDSW {output} {input}"
        response = self.send_command(command)
        return response

    def set_rx_input(self, output, input):
        """Switch the input on the rx connected to the HDBT port
        output = {o01, o02, all}
        input = {i01, i02}

        out: {
            001-hdbtoutl,
            002=hdbtout2,
            all-both outputs
            }
        in: {
            i01=HDBT in,
            i02= HDMI in
            }
        """
        command = f"SET VIDSWRX {output} {input}"
        response = self.send_command(command)
        return response

    def get_switch_output(self, output):
        """Get which input is mapping to the output
        input = {i00, i01, i02, i03, i04}
        output = {o01, o02}"""
        command = f"GET VIDSW {output}"
        response = self.send_command(command)
        return response

    def get_switch_output_all(self):
        """Get all output mappings to inputs
        response = VIDSW out in
        in = {i00, i01, i02, i03, i04}
        out = {o01, o02}"""
        command = "GET VIDSW all"
        response = self.send_command(command)
        return response

    def get_rx_input(self, output):
        """Get the current input on RX connected to HDBT
        output = {o01, o02, all}
        input = {i01, i02}

        out: {
            001-hdbtoutl,
            002=hdbtout2,
            all-both outputs
            }
        in: {
            i01=HDBT in,
            i02= HDMI in
            }
        """
        command = f"GET VIDSWRX {output}"
        response = self.send_command(command)
        return response

    # CEC Control
    def set_cec_power(self, on_off, output):
        """Turn CEC power on/off for defined output
        on_off = {on, off}
        output = {o01, o02, o03, o04}"""
        command = f"SET CEC_PWR {output} {on_off}"
        response = self.send_command(command)
        return response

    def set_cec_power_auto(self, on_off, output):
        """Turn CEC Auto power on/off for defined output
        on_off = {on, off}
        output = {o01, o02, o03, o04, all}"""
        command = f"SET AUTOCEC_FN {output} {on_off}"
        response = self.send_command(command)
        return response

    def get_cec_power_auto(self, output):
        """Get CEC auto power status for defined output
        output = {o01, o02, o03, o04, all}
        response param = {on, off}"""
        command = f"GET AUTOCEC_FN {output}"
        response = self.send_command(command)
        return response

    def set_cec_power_delay(self, output, delay):
        """Sets the power delay, when HDMI video on the output is disconnected,
        the unit will send cec power after delay(minutes)
        output = {o01, o02, o03, o04, all}
        delay = {1, 2, 3, ...} minutes"""
        command = f"SET AUTOCEC_D {output} {delay}"
        response = self.send_command(command)
        return response

    def get_cec_power_delay(self, output):
        """Get's the power delay for the defined output
        output = {o01, o02, o03, o04, all}
        delay = {1, 2, 3, ...} minutes"""
        command = f"GET AUTOCEC_D {output}"
        response = self.send_command(command)
        return response

    # HDCP
    def set_hdcp_input(self, input, on_off):
        """Turns HDCP on or off for defined input
        input = {i01, i02, i03, i04}
        on_off = {on, off}"""
        command = f"SET HDCP_S {input} {on_off}"
        response = self.send_command(command)
        return response

    def get_hdcp_input(self, input):
        """Get HDCP support status for defined input
        input = {i01, i02, i03, i04}"""
        command = f"GET HDCP_S {input}"
        response = self.send_command(command)
        return response

    # EDID
    def set_edid_input(self, input, edid):
        """Set input EDID. Default EDID is 4k60 4:4:4 2.0ch PCM with SDR
        Parameter:
        input = {i01, i02, i03, i04};
        edid = {01-07}
        01: Copy form HDMIoutput 1 02:Copy form HDMIoutput 2 03:Copy form HDBToutput 1
        04: Copy form HDBToutput 2
        05: 4K@60Hz 2.0ch PCM With SDR
        06: 4K@30Hz 2.0ch PCM With SDR 07:1080P@60Hz 2.0ch PCM With SDR"""
        command = f"SET EDID {input} {edid}"
        response = self.send_command(command)
        return response

    def get_edid_input(self, input=all):
        """Get input EDID information, if input is left empty it will
        return all EDID information
        input = {i01, i02, i03, i04, all}"""
        command = f"GET EDID {input}"
        response = self.send_command(command)
        return response

    def set_edid_write(self, input, location, block):
        """Write EDID content to input, responds with ok or error.
        Parameter:
        input = {i01, i02, i03, i04};
        location = {block0, block1};
        block = one block of 256 bytes edid ascii data with no
        spaces (hex data need conversion into ASCII code)
        """
        command = f"SET EDID_W {input} {location} {block}"
        response = self.send_command(command)
        return response

    def get_edid_output(self, output):
        """Get EDID information from defined output
        output = {o01, o02, o03, o04, all}"""
        command = f"GET DID_R {output}"
        response = self.send_command(command)
        return response

    # System
    def factory_reset(self):
        """Reset unit to factory default"""
        command = "RESET"
        response = self.send_command(command)
        return response

    def reboot(self):
        """Reboot unit"""
        command = "REBOOT"
        response = self.send_command(command)
        return response

    def get_api(self):
        """Get api information"""
        command = "HELP"
        response = self.send_command(command)
        return response

    def set_ip_mode(self, prm):
        """Set IP mode DHCP/Static
        prm = {static, dhcp}"""
        command = f"SET IP MODE {prm}"
        response = self.send_command(command)
        return response

    def get_ip_mode(self):
        """Get IP mode DHCP/Static"""
        command = "GET IP MODE"
        response = self.send_command(command)
        return response

    def set_ip_address(self, ip, mask, gate):
        """Set IP address
        example:
        ip = 192.168.1.21
        mask = 255.255.255.0
        gate = 192.168.1.1"""
        command = f"SET IPADDR {ip} {mask} {gate}"
        response = self.send_command(command)
        return response

    def get_ip_address(self):
        """Get IP address of unit"""
        command = "GET IPADDR"
        response = self.send_command(command)
        return response

    def get_firmware(self):
        """Get current firmware version"""
        command = "GET VER"
        response = self.send_command(command)
        return response

    def save_preset(self, preset):
        """Save preset scene
        preset = {1,2,3}"""
        command = f"SAVE PRESET {preset}"
        response = self.send_command(command)
        return response

    def load_preset(self, preset):
        """Load preset
        preset = {1, 2, 3}"""
        command = f"RESTORE PRESET {preset}"
        response = self.send_command(command)
        return response

    # Audio
    def set_switch_audio(self, output, aout="ao01"):
        """Switch audio input to audio output
        aout = {ao01}
        output = {o00, o01, o02}"""
        command = f"SET AUDSW {aout} {output}"
        response = self.send_command(command)
        return response

    def get_switch_audio(self, aout="ao01"):
        """Get which input is mapping to audio out
        aout = {ao01}"""
        command = f"GET AUDSW {aout}"
        response = self.send_command(command)
        return response

    def set_audio_mute(self, status, aout="ao01"):
        """Set mute status for audio output
        aout = {ao01}
        status = {on, off}"""
        command = f"SET MUTE {aout} {status}"
        response = self.send_command(command)
        return response

    def get_audio_mute(self, aout="ao01"):
        """Get mute status for audio output"""
        command = f"GET MUTE {aout}"
        response = self.send_command(command)
        return response

    def set_volume_gain_increase(self, aout="ao01"):
        """Increase audio out volume by +1 level"""
        command = f"Set VOLGAIN_INC {aout}"
        response = self.send_command(command)
        return response

    def set_volume_gain_decrease(self, aout="ao01"):
        """Decrease audio out volume by +1 level"""
        command = f"SET VOLGAIN_DEC {aout}"
        response = self.send_command(command)
        return response

    def set_volume_level(self, level, aout="ao01"):
        """Set volume level"""
        command = f"SET VOLGAIN_DATA {aout} {level}"
        response = self.send_command(command)
        return response

    def get_volume_level(self, aout="ao01"):
        """Get volume level"""
        command = f"GET VOLGAIN_DATA {aout}"
        response = self.send_command(command)
        return response

    # Scaler
    def set_video_scaler(self, output, on_off):
        """Set 4k-1080p simple scaler on each video output On or Off
        out = {o01, o02, o03, o04, all}"""
        command = f"SET SCALER {output} {on_off}"
        response = self.send_command(command)
        return response

    def get_scaler_output(self, output):
        """Get scaler status for defined output
        out = {o01, o02, o03, o04, all}"""
        command = f"GET SCALER {output}"
        response = self.send_command(command)
        return response

    # USB Matrix
    def set_usb_model(self, prm):
        """Set USB working mode
        prm = {follow, independent}"""
        command = f"SET USB_M {prm}"
        response = self.send_command(command)
        return response

    def get_usb_model(self):
        """Get USB working mode"""
        command = "GET USB_M"
        response = self.send_command(command)
        return response

    def set_usb_switch(self, input, output="all"):
        """Set USB switch from input to output
        input = {i00, i01, i02, i03, i04}
        output = {o01, o02, all}"""
        command = f"SET USBSW {output} {input}"
        response = self.send_command(command)
        return response

    def get_usb_switch(self, output="all"):
        """Get USB Switch output mapping
        output = {o01, o02, all}"""
        command = f"GET USBSW {output}"
        response = self.send_command(command)
        return response

    # Video Status
    def get_video_signal(self, input):
        """Get the status of the video input
        input = {i00, i01, i02, i03, i04}"""
        command = f"GET VIDIN_SIG {input}"
        response = self.send_command(command)
        return response

    def get_video_sync(self, input):
        """Get video sync information
        input =
        response: {<horizontal>x<vertical>, <rate>; <HDR info>;<ColorSpace>,<De epColor>}
        horizontal = An integer value representing the horizontal.
        vertical = An integer value representing the vertical. May have an additional qualifier such
                as 'i' or 'p'.
        rate = An integer value representing the refresh rate.
        HDR info = none hdr/ static hdr
        Color space = RGB / Ycbcr 444 /Ycbcr 422/Ycbcr 420
        DeepColor = 8 bit/10 bit /12 bit/ 16 bit"""
        command = f"GET SYNC {input}"
        response = self.send_command(command)
        return response

    def get_audio_format(self, input):
        """Get the audio format of the input
        input = {i00, i01, i02, i03, i04}
        Response: {<NONE / PCM / COMPRESSED/ HBR>; <Sampling rate>}"""
        command = f"GET AUDIN_FORMAT {input}"
        response = self.send_command(command)
        return response

    def get_hdcp_version(self, input):
        """Get HDCP information for input
        input = {i00, i01, i02, i03, i04}"""
        command = f"GET VIDIN_HDCP {input}"
        response = self.send_command(command)
        return response

    @staticmethod
    def help():
        """Prints out all functions available"""
        functions = [
            func
            for func in dir(SCT_MXKVM42_H2U3)
            if callable(getattr(SCT_MXKVM42_H2U3, func))
            and not func.startswith("__")
            and not func.startswith("_")
        ]
        num_functions = len(functions)
        print("Available functions:")
        for i in range(0, num_functions, 2):
            func_name_1 = functions[i]
            func_name_2 = functions[i + 1] if i + 1 < num_functions else ""
            print("{:<30}{:<30}".format(func_name_1, func_name_2))
        print("")


if __name__ == "__main__":
    SCT_MXKVM42_H2U3.help()
    matrix = SCT_MXKVM42_H2U3("Telnet", "10.0.30.4", "admin")
    matrix.set_switch_input_output("i01", "o01")
    time.sleep(3)
    matrix.set_switch_input_output("i02", "o01")
