from Murideo_Generator import Murideo_Generator
import yaml


class Generator:
    """Used to bring all the classes together to create a dot notation for
    the Murideo_Generator class"""

    def __init__(self, port) -> None:
        self.murideo_gen = Murideo_Generator(port)
        self.audio = Audio(self.murideo_gen)
        self.video = Video(self.murideo_gen)


class Audio:
    def __init__(self, murideo_gen) -> None:
        self.murideo_gen = murideo_gen

    def sample(self, rate):
        """Set Audio Sample Rate {rate}
        example: (44.1k), (auto)"""
        command = "0067H"
        params = {
            "32k": "00",
            "44.1k": "01",
            "48k": "02",
            "88k": "03",
            "96k": "04",
            "176k": "05",
            "192k": "06",
            "auto": "07",
        }
        value = params.get(rate)
        if value is None:
            print(f"Invalid sample rate: {rate}")

        print(f"Audio Sample Rate {rate}")

        return self.murideo_gen.send(command, value)

    def channel(self, channel):
        """Set Audio test channel {channel}
        example: (ch0), (ch7)"""
        command = "0047H"
        params = {
            "ch0": "00",
            "ch1": "01",
            "ch2": "02",
            "ch3": "03",
            "ch4": "04",
            "ch5": "05",
            "ch6": "06",
            "ch7": "07",
        }
        value = params.get(channel)
        if value is None:
            print(f"Invalid Audio Test Channel {channel}")

        print(f"Audio test channel {channel}")

        return self.murideo_gen.send(command, value)

    def bit(self, bit):
        """Set Audio Bit Rate {bit}
        example: (16), (24)"""
        command = "0068H"
        params = {"16": "00", "20": "01", "24": "02", "auto": "03"}
        value = params.get(bit)
        if value is None:
            print(f"Invalid Bit {bit}")

        print(f"Audio Bit Depth {bit}")

        return self.murideo_gen.send(command, value)

    def pcm(self):
        """Set to PCM Audio"""
        command = "0069H"
        value = "01"
        print("PCM Audio")
        return self.murideo_gen.send(command, value)

    def dolby_digital(self, rate):
        """Set Dolby Digital {rate ch}
        example: (32k 2ch), (48k 5ch)"""
        command = "0069H"
        params = {
            "32k 2ch": "02",
            "32k 5ch": "03",
            "44k 2ch": "04",
            "44k 5ch": "05",
            "48k 2ch": "06",
            "48k 5ch": "07",
        }
        value = params.get(rate)
        if value is None:
            print(f"Invalid Rate {rate}")
        print(f"Dolby Digital {rate}")
        return self.murideo_gen.send(command, value)

    def dolby_digital_plus(self, rate):
        """Set Dolby Digital Plus {rate ch}
        example: (48k 2ch), (48k atmos)"""
        command = "0069H"
        params = {
            "48k 2ch": "08",
            "48k 5ch": "09",
            "48k 7ch": "10",
            "48k atmos": "11",
        }
        value = params.get(rate)
        if value is None:
            print(f"Invalid Rate {rate}")
        print(f"Dolby Digital Plus {rate}")
        return self.murideo_gen.send(command, value)

    def dolby_mat(self, rate):
        """Set Dolby MAT {rate ch}
        example: (44k 2ch), (48k 7ch)"""
        command = "0069H"
        params = {
            "44k 2ch": "12",
            "44k 5ch": "13",
            "44k 7ch": "14",
            "48k 2ch": "15",
            "48k 5ch": "16",
            "48k 7ch": "17",
            "44k atmos": "18",
            "48k atmos": "19",
        }
        value = params.get(rate)
        if value is None:
            print(f"Invalid Rate {rate}")
        print(f"Dolby MAT {rate}")
        return self.murideo_gen.send(command, value)

    def dolby_mat_truehd(self, rate):
        """Set Dolby MAT TrueHD {rate ch}
        example: (48k 2ch), (96k 7ch)"""
        command = "0069H"
        params = {
            "48k 2ch": "20",
            "48k 5ch": "21",
            "48k 7ch": "22",
            "96k 2ch": "23",
            "96k 5ch": "24",
            "96k 7ch": "25",
            "192k 2ch": "26",
            "192k 5ch": "27",
            "48k atmos": "28",
        }
        value = params.get(rate)
        if value is None:
            print(f"Invalid Rate {rate}")
        print(f"Dolby MAT TrueHD {rate}")
        return self.murideo_gen.send(command, value)

    def mute(self, status):
        """enable/disable audio mute"""
        command = " 0074H"
        params = {"disable": "00", "enable": "01"}
        value = params.get(status)
        if value is None:
            print(f"Invalid Status {status}")
        print(f"Setting Audio Mute to {status}")
        return self.murideo_gen.send(command, value)

    def volume(self, db):
        """Set Volume level from -60db to 0db
        example: (-60), (-24)"""
        command = "006DH"
        params = {
            "-60": "00",
            "-54": "01",
            "-48": "02",
            "-42": "03",
            "-36": "04",
            "-30": "05",
            "-24": "06",
            "-18": "07",
            "-12": "08",
            "-6": "09",
            "0": "10",
        }
        volume_levels = {
            int(k): v for k, v in params.items()
        }  # Convert keys to integers

        # Check if the input volume level is valid
        try:
            db = int(db)
        except ValueError:
            print(f"Invalid volume level {db}")
            return

        closest_level = min(volume_levels.keys(), key=lambda x: abs(x - db))
        value = volume_levels[closest_level]
        print(f"Set Volume to {closest_level}db")
        return self.murideo_gen.send(command, value)

    def sine(self, frequency):
        """Set PCM Sine Wave Frequency
        example: (100), (1k)"""
        command = "0073H"
        params = {
            "100": "00",
            "200": "01",
            "300": "02",
            "400": "03",
            "500": "04",
            "600": "05",
            "700": "06",
            "800": "07",
            "900": "08",
            "1k": "09",
            "2k": "10",
            "3k": "11",
            "4k": "12",
            "5k": "13",
        }
        value = params.get(frequency)
        if value is None:
            print(f"Invalid frequency {frequency}hz")
        print(f"PCM Sine Wave to {frequency}hz")
        return self.murideo_gen.send(command, value)

    def arc(self, status):
        """Set ARC/eARC out setup
        example: (disable), (enable earc)"""
        command = "0083H"
        params = {"disable": "00", "enable earc": "01", "enable arc": "02"}
        value = params.get(status)
        if value is None:
            print(f"Invalid Status {status}")
        print(f"Set {status}")
        return self.murideo_gen.send(command, value)


class Video:
    def __init__(self, murideo_gen) -> None:
        self.murideo_gen = murideo_gen

    def timing(self, resolution):
        """Set Resolution {resolution}
        example: (480 60), (4k 30)"""
        command = "0061H"
        params = {
            "480 60": "11",
            "720 60": "12",
            "1080 30": "10",
            "1080 60": "14",
            "4k 30": "1c",
            "4k 60": "22",
        }


if __name__ == "__main__":
    gen = Generator("/dev/tty.usbserial-A9UK1ODD")
    response = gen.audio.sample("48k")
    print(response)
