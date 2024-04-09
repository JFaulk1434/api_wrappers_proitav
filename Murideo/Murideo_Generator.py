import serial
import time


class Murideo_Generator:
    def __init__(self, port, baud=115200) -> None:
        self.serial = serial.Serial(port, baudrate=baud)

    def generate_command(self, keyword, data, group="00", device_address="00"):
        header = "AA 00 00"

        # Remove trailing 'H' and convert to little endian if necessary
        if keyword[-1].lower() == "h":
            keyword = keyword[:-1]
        if len(keyword) == 4:
            keyword = keyword[2:] + " " + keyword[:2]

        length = len(keyword.split()) + len(data.split()) + 3
        length_hex = f"{length:04x}"  # Convert length to a 4-digit hexadecimal
        length_hex = f"{length_hex[2:]} {length_hex[:2]}"  # Convert to little endian

        # Construct the command
        command = f"{header} {length_hex} {group} {device_address} {keyword} {data}"

        # Compute checksum
        command = self.add_checksum(command)  # Assume this is your checksum function

        return command

    def add_checksum(self, command):
        command = command.replace(" ", "")  # Remove all whitespaces
        bytes_arr = bytearray.fromhex(
            command
        )  # Convert the hex command string to a bytearray
        checksum = (
            sum(bytes_arr) & 0xFF
        )  # Sum all bytes values and keep only the last 8 bits (1 byte)
        checksum = (
            (~checksum) + 1
        ) & 0xFF  # One's complement and addition of 1 for negative checksum
        return f"{command} {checksum:02X}"  # Append the calculated checksum to the command string

    def _send(self, command):
        bytes_command = bytearray.fromhex(command.replace(" ", ""))
        self.serial.write(bytes_command)

        formatted_command = " ".join(format(x, "02X") for x in bytes_command)
        # print(f"Sent: {formatted_command}")

        time.sleep(0.3)
        response = self.serial.read_all()

        formatted_response = "".join(format(x, "02X") for x in response)
        formatted_response = " ".join(
            formatted_response[i : i + 2] for i in range(0, len(formatted_response), 2)
        )

        # print(f"Received: {formatted_response}")
        time.sleep(0.25)
        return formatted_response

    def send(self, keyword, data):
        command = self.generate_command(keyword, data)
        response = self._send(command)
        return response


if __name__ == "__main__":
    device = Murideo_Generator("/dev/tty.usbserial-A9UK1ODD")
    keyword = "78F7H"
    dhcp_off = device.generate_command(keyword, "00")
    dhcp_on = device.generate_command(keyword, "01")
    device.send(dhcp_off)
    time.sleep(1)
    device.send(dhcp_on)
