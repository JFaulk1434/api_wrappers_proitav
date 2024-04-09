# Murideo Python wrapper

## Goal is to be able to send all types of instructions and the program can construct the command and read the response

### Class requirements

- Name - Murideo_Generator
- Args - port, baud=115200
- Modules - Serial, Time, Yaml
- Yaml file will contain commands
- Functions
  - send
    - used to send command and receive feedback with a .5 delay between sending and receiving

### Command Format (Protocol)

- Header which is 2 parts
  - AA when sending from PC to Device byte number 1
    - device_id default is 0x0000 byte number 2
- Length byte number 2
  - total byte numbers except header
- Group address byte number 1
  - default address is 0x0000
- Device address byte number 1
  - default is 0
- Keyword byte number 2 (lower byte first)
  - keyword examples
    - 0x00B4: Enable eARC audio loop out to the HDMI input port for debug(HDMI input port switch to HDMI output port)
    - 0x00C0: SET Link Training
    - 0x7801: Address setting
    - 0x7802: Reset all settings
- Data byte number 4
- Checksum byte number 1

#### Notes

- The device ID for signal generator is 0x0000.
- Each device can be assigned a separate address. Address includes two bytes. Available group address and device are from 0x01 to 0xfe. If the address is 0x0000, that means this device has not been assigned with address.  0
- x0000 is the broadcast address. When computer send command with the address 0x0000, all devices will receive and execute the command. 0xffff is another broadcast address. All device need to receive and execute the command with address 0xffff but do not feed back any data to computer.
The device address can be shown in the OSD menu on the OLED panel.

- The keyword, which is less than 0x8000, is for setting. The keyword greater than 0x8000 is for status reading
- Command example for EDID reading:
PC->Device: AA +ID+06 00 00 00 38 B8 01+checksum
If the device can’t read EDID data from sink device, it will feedback data to PC as below:
Device->PC: AB+ID+ 06 00 00 00 38B8 00+checksum
If the device can read EDID data from sink device, it will feedback data to PC as below:
MCU->PC: AB +ID+05 01 00 00 38 B8 ~~~~~~(256BYTE)+checksum
- Command example for reading EDID from the first one stored in memory.
PC->MCU:AA +ID+06 00 00 00 aa 80 01+checksum
MCU->PC: AB +ID+06 01 00 00 aa 80 01~~~~~~(256BYTE)+checksum
- When PC send setting command (less than 0x8000) to device, device will reply with FFFFH at the position of keyword. After the keyword, there are 3 parameters. The first is the low byte of the keyword which is sent from PC to device, the second is the high byte of keyword, the third is the status related to the command(please refer to the table-3 below).  
Here is the example: When PC send command AA 00 00 06 00 00 00 00 61 00 00 EF (set the timing to the first timing 640x480)
The device will reply : AB 00 00 08 00 00 00 FF FF 61 00(61 00 are keyword)  00(00 means executed correctly)  EE (checksum)

#### Examples

- Command for VESA3840x2400P_60HZ
  - 65H
  - Example (to set VESA3840x2400P_60HZ): AA 00 00 06 00 00 00 61 00 65 8A (8A is checksum)

- Command for Set Color Space to YC444
  - 0063H
  - Example (to set YC444(16-235)): AA 00 00 06 00 00 00 63 00 02 EB (EB is checksum)
  - Notes: 0-RGB(0-255)
    1-RGB(16-235)
    2-YC444(16-235)
    3-YC422(16-235)
    4-YC420(16-235) Note: colorspace 420 can only be set in 4K 50/60Hz mode.
    5-AUTO

- Command for Sweep_Audio
  - 0069H
  - Example (to set SWEEP_AUDIO): AA 00 00 07 00 00 00 69 00 24 02 C0 (C0 is checksum)
  - Notes: 528-SPEAKER_ALLOCATION
    538-WHITE_NOISE
    548-SWEEP_AUDIO

#### Checksum examples

- AA 00 00 07 00 00 00 62 00 C8 01 24  (24 is checksum)
- AA 00 00 06 00 00 00 61 00 65 8A (8A is checksum)
- AA 00 00 06 00 00 00 63 00 02 EB (EB is checksum)
- AA 00 00 06 00 00 00 64 00 03 E9 (E9 is checksum)
- AA 00 00 06 00 00 00 67 00 03 E6 (E6 is checksum)
- AA 00 00 07 00 00 00 69 00 24 02 C0 (C0 is checksum)
- AA 00 00 19 00 00 00 A0 00 00 01 1D 06 80 07 18 01 58 00 2C 00 38 04 2D 00 04 00 05 00 E3 (E3 is checksum)
- AA 00 00 07 00 00 00 01 78 01 02 D3 (D3 is checksum)
- AA 00 00 06 00 00 00 AA 00 02 A4 (A4 is checksum)
- AA 00 00 06 00 00 00 AE 00 03 9F (9F is checksum)
- AA 00 00 06 00 00 00 AB 00 00 A5 (A5 is checksum)
- AA 00 00 85 00 00 00 7D 00 00 00 00 00 5B 00 00 25 66 00 00 39 93 25 66 F9 27 EE E2 25 66 43 D9 00 00 01 00 00 00 08 00 00 00 08 00 00 00 16 D5 25 E6 03 45 0A 08 2F E0 06 19 00 00 02 A7 3D 59 FF FF 00 00 00 00 00 00 00 00 0C 00 01 01 00 00 0F FF 00 2A 02 00 00 00 06 01 00 00 0F FF 05 55 00 00 00 04 04 0F FF 0F FF 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 99 DF A0 EF D2 (D2 is checksum)
- AA 00 00 07 00 00 00 7E 00 07 01 C9 (C9 is checksum)
- AA 00 00 24 00 00 00 80 00 81 01 04 6b 03 0c 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 B2 (B2 is checksum)
