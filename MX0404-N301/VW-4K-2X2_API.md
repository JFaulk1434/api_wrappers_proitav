# VW-4K-2X2 API Control

This document will contain API commands for IR, RS232, and TCP for the VW-4K-2X2 Matrix.
v1.1

## Table of Contents

- [VW-4K-2X2 API Control](#vw-4k-2x2-api-control)
  - [Table of Contents](#table-of-contents)
  - [Commands](#commands)
    - [Video Mode](#video-mode)
      - [Set Video Mode](#set-video-mode)
      - [Get Video Mode](#get-video-mode)
    - [Video Wall](#video-wall)
      - [Set Video Wall](#set-video-wall)
      - [Get Video Wall](#get-video-wall)
      - [Set Bezel Correction](#set-bezel-correction)
      - [Get Bezel Correction](#get-bezel-correction)
      - [Set 180° Rotation](#set-180-rotation)
      - [Get 180° Rotation](#get-180-rotation)
    - [Video Matrix](#video-matrix)
      - [Switch Input to Output](#switch-input-to-output)
      - [Switch Input to all Outputs](#switch-input-to-all-outputs)
      - [Get Mapping Status of Output](#get-mapping-status-of-output)
      - [Get Mapping Status of All Outputs](#get-mapping-status-of-all-outputs)
    - [Audio](#audio)
      - [Set Audio Mute](#set-audio-mute)
      - [Get Audio Mute](#get-audio-mute)
      - [Set CEC Power](#set-cec-power)
      - [Set CEC Auto Power](#set-cec-auto-power)
      - [Get CEC Auto Power](#get-cec-auto-power)
      - [Set CEC power delay](#set-cec-power-delay)
      - [Get CEC power delay](#get-cec-power-delay)
    - [HDCP](#hdcp)
      - [Set input HDCP support](#set-input-hdcp-support)
      - [Get input HDCP support](#get-input-hdcp-support)
      - [Set Input EDID](#set-input-edid)
      - [Get all input EDID status](#get-all-input-edid-status)
      - [Get one input EDID status](#get-one-input-edid-status)
      - [Write EDID to one input](#write-edid-to-one-input)
      - [Read EDID from output](#read-edid-from-output)
    - [System Info](#system-info)
      - [Factory Reset](#factory-reset)
      - [System Reboot](#system-reboot)
      - [Set IR System Code](#set-ir-system-code)
      - [Get IR System Code](#get-ir-system-code)
      - [Get API List](#get-api-list)
      - [Get IP address](#get-ip-address)
      - [Set IP address](#set-ip-address)
      - [GET Network Mode](#get-network-mode)
      - [Set Network Mode](#set-network-mode)
      - [Set to Standby](#set-to-standby)
      - [Wake from Standby](#wake-from-standby)
      - [Get standby status](#get-standby-status)
      - [Get Input connection status](#get-input-connection-status)
      - [Get Input signal status](#get-input-signal-status)
      - [Get Input video format](#get-input-video-format)
      - [Get HDCP version](#get-hdcp-version)
      - [Get Output connection status](#get-output-connection-status)
      - [Get Output signal status](#get-output-signal-status)
      - [Get Output video format](#get-output-video-format)
      - [Get Output HDCP version](#get-output-hdcp-version)
    - [Update Info](#update-info)
      - [Firmware Version](#firmware-version)
      - [Hardware Version](#hardware-version)
    - [Preset Info](#preset-info)
      - [Save Preset](#save-preset)
      - [Restore Preset](#restore-preset)
    - [Video Output](#video-output)
      - [Set Video Output Scaling](#set-video-output-scaling)
      - [Get Video Output Scaling](#get-video-output-scaling)
      - [Set Output Resolution](#set-output-resolution)
      - [Get Output Resolution](#get-output-resolution)
    - [RS232 Settings](#rs232-settings)
    - [Telnet/TCP Settings](#telnettcp-settings)
      - [Obtain IP address of the Device](#obtain-ip-address-of-the-device)
  - [IR Commands](#ir-commands)

## Commands

**Command Explanation**
Take Command `SET SW in <CR><LF>` as an example:

1. [SET SW] denotes command key words, case insensitive.
2. [in] denotes parameters, case insensitive; incorrect parameters will not be recognized.
3. `<CR><LF>` denotes a carriage return or a line feed.
4. all commands must end with a carriage return or a line feed.

### Video Mode

#### Set Video Mode

Sets the video output mode.

- Command: `SET VIDMODE prm`
- Return: `VIDMODE prm`
- Parameter: Matrix, VideoWall
- Example: `SET VIDMODE Matrix`
  - Returned: `VIDMODE Matrix`

#### Get Video Mode

Get's the video output mode

- Command: `GET VIDMODE`
- Return: `VIDMODE prm`
- Return Parameter: Matrix, VideoWall
- Example: `GET VIDMODE`
  - Returned: `GET VIDMODE Matrix`

<!--- ### Multiview -->

### Video Wall

#### Set Video Wall

Set video wall and select input source.

- Command: `SET VIDWALL in prm1 prm2 prm3 prm4`
- Return: `VIDWALL in prm1 prm2 prm3 prm4`
- Parameter _prm_: out1, out2, out3, out4
- Parameter _in_: in1, in2, in3, in4
- Return Parameter: out1, out2, out3, out4
- Example: `SET VIDWALL in1 out2 out1 out3 out4`
  - Returned: `VIDWALL in1 out2 out1 out3 out4`

#### Get Video Wall

Get Video Wall settings and the input source selected.

- Command: `GET VIDWALL`
- Return: `VIDWALL in prm1 prm2 prm3 prm4`
- Returned Parameter _prm_: out1, out2, out3, out4
- Returned Parameter _in_: in1, in2, in3, in4
- Example: `GET VIDWALL`
  - Returned: `VIDWALL in1 out2 out1 out3 out4`

#### Set Bezel Correction

Set the Video Wall bezel correction

- Command: `SET VIDWALLBEZEL VW OW VH OH`
- Return: `VIDWALLBEZEL VW OW VH OH`
- Parameter: _0-10000mm_
  - _VW_: Viewing Width
  - _OW_: Outer Width
  - _VH_: Viewing Height
  - _OH_: Outer Height
- Example: `SET VIDWALLBEZEL 889 914 495 520`
  - Returned: `VIDWALLBEZEL 889 914 495 520`

#### Get Bezel Correction

Get the Video Wall bezel correction

- Command: `GET VIDWALLBEZEL`
- Return: `VIDWALLBEZEL VW OW VH OH`
- Parameter: _0-10000mm_
  - _VW_: Viewing Width
  - _OW_: Outer Width
  - _VH_: Viewing Height
  - _OH_: Outer Height
- Example: `GET VIDWALLBEZEL`
  - Returned: `VIDWALLBEZEL 889 914 495 520`

#### Set 180° Rotation

Set the 180° rotation on or off

- Command: `SET VIDWALL_ROTATION prm1 prm2`
- Return: `VIDWALL_ROTATION prm1 prm2`
- Parameter _prm1_: out1, out2, out3, out4
- Parameter _prm2_: disable, enable
- Example: `SET VIDWALL_ROTATION out1 disable`
  - Returned: `VIDWALL_ROTATION out2 disable`

#### Get 180° Rotation

Get the status of the 180° rotation

- Command: `GET VIDWALL_ROTATION prm1`
- Return: `VIDWALL_ROTATION prm1 prm2`
- Parameter _prm1_: out1, out2, out3, out4
- Parameter _prm2_: disable, enable
- Example: `GET VIDWALL_ROTATION out2`
  - Returned: `VIDWALL_ROTATION out2 disable`

### Video Matrix

#### Switch Input to Output

Switch one input (source) to one output (display)

- Command: `SET SW in out`
- Return: `SW in1 out2`
- Parameter _in_: in1, in2, in3, in4
- Parameter _out_: out1, out2, out3, out4
- Example: `SET SW in1 out3`
  - Returned: `SW in1 out3`

#### Switch Input to all Outputs

Switch one input (source) to all outputs (displays)

- Command: `SET SW in all`
- Return: `SW in all`
- Parameter _in_: in1, in2, in3, in4
- Example: `SET SW in2 all`
  - Returned: `SW in2 all`

#### Get Mapping Status of Output

Get the mapping status of an output

- Command: `GET MP out`
- Return: `MP in out`
- Parameter _in_: in1, in2, in3, in4
- Parameter _out_: out1, out2, out3, out4
- Example: `GET MP out2`
  - Returned: `MP in3 out2`

#### Get Mapping Status of All Outputs

Gets the mapping status of all inputs and outputs

- Command: `GET MP all`
- Return: `MP in out`
- Parameter _in_: in1, in2, in3, in4
- Parameter _out_: out1, out2, out3, out4
- Example: `GET MP all`

  - Returned:

    ```text
    MP in1 out1
    MP in1 out2
    MP in1 out3
    MP in4 out4
    ```

### Audio

#### Set Audio Mute

Set Audio Mute for specific Audio Output

- Command: `SET AUDIO_MUTE out prm`
- Return: `AUDIO_MUTE out prm`
- Parameter _out_: zone1, zone2
- Parameter _prm_: on, off
- Example: `SET AUDIO_MUTE zone1 on`
  - Returned: `AUDIO_MUTE zone1 on`

#### Get Audio Mute

Get Audio Mute for specific Audio Output

- Command: `GET AUDIO_MUTE out`
- Return: `AUDIO_MUTE out prm`
- Parameter _out_: zone1, zone2
- Parameter _prm_: on, off
- Example: `GET AUDIO_MUTE zone1`
  - Returned: `AUDIO_MUTE zone1 on`

#### Set CEC Power

Set sink to power on or off

- Command: `SET CEC_PWR out prm`
- Return: `CEC_PWR out prm`
- Parameter _out_: out1, out2, out3, out4
- Parameter _prm_: on, off
- Example: `SET CEC_PWR out1 on`
  - Return: `CEC_PWR out1 on`

#### Set CEC Auto Power

Set sink auto power function on or off

- Command: `SET AUTOCEC_FN out prm`
- Return: `AUTOCEC_FN out prm`
- Parameter _prm_: on, off
- Parameter _out_: out1, out2, out3, out4
- Example: `SET AUTOCEC_FN out1 on`
  - Return: `AUTOCEC_FN out1 on`

#### Get CEC Auto Power

Get sink auto power function status

- Command: `GET AUTOCEC_FN out`
- Return: `AUTOCEC_FN out prm`
- Parameter _out_: out1, out2, out3, out4
- Parameter _prm_: on, off
- Example: `GET AUTOCEC_FN out1`
  - Return: `AUTOCEC_FN out1 on`

#### Set CEC power delay

Setup to automatically turn off display when no video for x amount of time

- Command: `SET AUTOCEC_D out prm`
- Return: `AUTOCEC_D out prm`
- Parameter _out_: out1, out2, out3, out4
- Parameter _prm_: `1-30` minutes. Default is 2
- Example: `SET AUTOCEC_D out1 2`
  - Return: `AUTOCEC_D out1 2`
  - Description:
    - When no active signal to HDMI1, after 2 minutes CEC will turn off the display.

#### Get CEC power delay

Get the status of the CEC auto power delay

- Command: `GET AUTOCEC_D out`
- Return: `AUTOCEC_D out prm`
- Parameter _out_: out1, out2, out3, out4
- Parameter _prm_: `1-30` minutes
- Example: `GET AUTOCEC_D out1`
  - Return: `AUTOCEC_D out1 2`

### HDCP

#### Set input HDCP support

Turn on or off HDCP support for input

- Command: `SET HDCP_S in prm`
- Return: `HDCP_S in prm`
- Parameter _prm_: on, off
- Parameter _in_: in1, in2, in3, in4
- Example: `SET HDCP_S in1 on`
  - Return: `HDCP_S in1 on`

#### Get input HDCP support

Get the HDCP status of input

- Command: `GET HDCP_S in`
- Return: `HDCP_S in prm`
- Parameter _prm_: on, off
- Parameter _in_: in1, in2, in3, in4
- Example: `GET HDCP_S in1`
  - Return: `HDCP_S in1 on`

#### Set Input EDID

Set the EDID for the Input

- Command: `SET EDID in prm`
- Return: `EDID in prm`
- Parameter _in_: in1, in2, in3, in4
- Parameter _prm_: `1-16`

  ```text
  1: Copy form hdmi output 1
  2: Copy form hdmi output 2
  3: Copy form hdmi output 3
  4: Copy form hdmi output 4
  5~10: Reserved
  11: Fixed 4K60 2.0CH PCM Audio with HDR
  12: Fixed 4K60 2.0CH PCM Audio with SDR
  13: Fixed 4K30 2.0CH PCM Audio with HDR
  14: Fixed 4K30 2.0CH PCM Audio with SDR
  15: Fixed 1080p@60Hz 2.0CH PCM Audio with HDR
  16: Fixed 1080p@60Hz 2.0CH PCM Audio with SDR
  ```

- Example: `SET EDID in1 12`
  - Return: `EDID in1 12`
  - Description:
    - Set the EDID for input1 to 4k60 2.0CH PCM Audio with SDR

#### Get all input EDID status

Get all input EDID status

- Command: `GET EDID all`
- Return:

  ```text
  EDID in prm
  EDID in prm
  EDID in prm
  ...
  ```

- Parameter _prm_: `1-16`

  ```text
  1: Copy form hdmi output 1
  2: Copy form hdmi output 2
  3: Copy form hdmi output 3
  4: Copy form hdmi output 4
  5~10: Reserved
  11: Fixed 4K60 2.0CH PCM Audio with HDR
  12: Fixed 4K60 2.0CH PCM Audio with SDR
  13: Fixed 4K30 2.0CH PCM Audio with HDR
  14: Fixed 4K30 2.0CH PCM Audio with SDR
  15: Fixed 1080p@60Hz 2.0CH PCM Audio with HDR
  16: Fixed 1080p@60Hz 2.0CH PCM Audio with SDR
  ```

- Example: `GET EDID all`

  - Return:

    ```text
    EDID in1 01
    EDID in2 13
    EDID in3 12
    EDID in4 4
    ```

#### Get one input EDID status

Get the EDID status of one input

- Command: `GET EDID in`
- Return: `EDID in prm`
- Parameter _in_: in1, in2, in3, in4
- Parameter _prm_: `1-16`

  ```text
  1: Copy form hdmi output 1
  2: Copy form hdmi output 2
  3: Copy form hdmi output 3
  4: Copy form hdmi output 4
  5~10: Reserved
  11: Fixed 4K60 2.0CH PCM Audio with HDR
  12: Fixed 4K60 2.0CH PCM Audio with SDR
  13: Fixed 4K30 2.0CH PCM Audio with HDR
  14: Fixed 4K30 2.0CH PCM Audio with SDR
  15: Fixed 1080p@60Hz 2.0CH PCM Audio with HDR
  16: Fixed 1080p@60Hz 2.0CH PCM Audio with SDR
  ```

- Example: `GET EDID in1`
  - Return: `EDID in1 12`

#### Write EDID to one input

Write EDID content to input

- Command: `SET EDID_W in prm1 prm2`
- Return: `EDID_W in prm1 prm3`
- Parameter _in_: in1, in2, in3, in4
- Parameter _prm1_: block0, block1
- Parameter _prm2_: one block of 256 bytes edid ascii data with spaces (hex data need conversion into ASCII code)
- Parameter _prm3_: ok, error
  - error: Checksum error
- Example:

  ```text
  SET EDID_W in block0 00ffffffffffff004c2d140f000e0001011c0103805932780a23ada4544d99260f474abdef80714f81c0810081809500a9c0b300010108e80030f2705a80b0588a00501d7400001e023a801871382d40582c4500501d7400001e000000fd00184b0f873c000a202020202020000000fc0053414d53554e470a20202020200177
  ```

  - Return: `EDID_W in1 block0 ok`

#### Read EDID from output

Read the EDID information from output

- Command: `GET EDID_R out`
- Return: `EDID_R out prm1 prm2`
- Parameter _prm1_: block0, block1
- Parameter _prm2_: one block of 256 bytes edid ascii data with spaces (hex data need conversion into ASCII code)
- Example: `GET EDID_R out1`

  - Return:

    ```text
    EDID_R out1 block0 00ffffffffffff004c2d140f000e0001011c0103805932780a23ada4544d99260f474abdef80714f81c0810081809500a9c0b300010108e80030f2705a80b0588a00501d7400001e023a801871382d40582c4500501d7400001e000000fd00184b0f873c000a202020202020000000fc0053414d53554e470a20202020200177
    EDID_R out1 block1 020356f05761101f041305142021225d5e5f606566626364071603122909070715075057070183010000e2004fe305c3016e030c002000b83c2000800102030467d85dc401788003e3060d01e30f01e0e5018b849001011d80d0721c1620102c2580501d7400009e662156aa51001e30468f3300501d7400001e000000000089
    ```

### System Info

#### Factory Reset

Reset unit back to factory settings

- Command: `RESET`
- Return: `RESET`

#### System Reboot

Reboot the unit

- Command: `REBOOT`
- Return: `REBOOT`

#### Set IR System Code

Sets the IR code set to be unique

- Command: `SET IR_SC prm`
- Return: `IR_SC prm`
- Parameter _prm_: all, mode1, mode2
  - mode1 = `0x00`
  - mode2 = `0x4e`
- Example: `SET IR_SC mode1`
  - Return: `IR_SC mode1`

#### Get IR System Code

Get the IR code status

- Command: `GET IR_SC`
- Return: `IR_SC prm`
- Parameter _prm_: all, mode1, mode2
  - mode1 = `0x00`
  - mode2 = `0x4e`
- Example: `GET IR_SC`
  - Return: `IR_SC mode1`

#### Get API List

Get API command list

- Command: `help`
- Return: a list of the API commands

#### Get IP address

Get the IP address of the unit

- Command: `GET IPADDR`
- Return: `ipaddr xxx.xxx.xxx.xxx MASK xxx.xxx.xxx.xxx GATEWAY xxx.xxx.xxx.xxx`
- Example: `GET IPADDR`
  - Return: `ipaddr 10.0.50.23 MASK 255.255.255.0 GATEWAY 10.0.50.1`

#### Set IP address

Sets the IP address but does not enable static

- Command: `SET IPADDR xxx.xxx.xxx.xxx MASK xxx.xxx.xxx.xxx GATEWAY xxx.xxx.xxx.xxx`
- Return: `ipaddr xxx.xxx.xxx.xxx MASK xxx.xxx.xxx.xxx GATEWAY xxx.xxx.xxx.xxx`
- Example: `SET IPADDR 10.0.50.99 MASK 255.255.255.0 GATEWAY 10.0.50.1`
  - Return: `IPADDR 10.0.50.99 MASK 255.255.255.0 GATEWAY 10.0.50.1`

#### GET Network Mode

Get Network Mode configuration

- Command: `GET NETCFG MODE`
- Return: `NETCFG MODE DHCP`

#### Set Network Mode

Set the Network Mode Configuration

- Command: `SET NETCFG MODE prm`
- Return: `NETCFG MODE prm`
- Parameter: HDCP, STATIC
- Example: `SET NETCFG MODE STATIC`
  - Return: `NETCFG MODE STATIC`

#### Set to Standby

Sets the device into standby mode

- Command: `STANDBY`
- Return: `STANDBY!`

#### Wake from Standby

Wakes up the device from Standby

- Command: `WAKE`
- Return: `WAKE!`

#### Get standby status

Get the standby status

- Command: `GET STANDBY`
- Return: `prm`
- Parameter: STANDBY!, WAKE!
- Example: `GET STANDBY`
  - Return: `WAKE!`

#### Get Input connection status

Get the connections status of the video input

- Command: `GET VIDIN_CONNECT in`
- Return: `VIDIN_CONNECT in prm`
- Parameter _in_: in1, in2, in3, in4
- Parameter _prm_: Disconnected, Connected
- Example: `GET VIDIN_CONNECT in1`
  - Return: `VIDIN_CONNECT in1 Disconnected`

#### Get Input signal status

Get the signal status of the video input

- Command: `GET VIDIN_SIG in`
- Return: `VIDIN_SIG in prm`
- Parameter _in_: in1, in2, in3, in4
- Parameter _prm_: no, valid
- Example: `GET VIDIN_SIG in1`
  - Return: `VIDIN_SIG in1 valid`

#### Get Input video format

Get the Inputs video format information

- Command: `GET VIDIN_FORMAT in`
- Return: `VIDIN_FORMAT in prm`
- Parameter _in_: in1, in2, in3, in4
- Parameter _prm_: {}
  - prm = `{<horizontal>x<vertical>,<rate>;<HDRinfo>;<ColorSpace>,<DeepColor>}`
  - horizontal = An integer value representing the horizontal
  - vertical = An integer value representing the vertical. May have an additional qualifier such as 'i' or 'p'
  - rate = An integer value representing the refresh rate
  - HDR info = none hdr / static hdr / dynamic hdr
  - Color space = RGB / Ycbcr 444 / Ycbcr 422 / Ycbcr 420
  - DeepColor = 8 bit / 10 bit / 12 bit / 16 bit
- Example: `GET VIDIN_FORMAT in1`
  - Return: `VIDIN_FORMAT in1 3840x2160,30;None HDR;RGB;8bit`

#### Get HDCP version

Get the HDCP version on the input

- Command: `GET VIDIN_HDCP in`
- Return: `VIDIN_HDCP in prm`
- Parameter _in_: in1, in2, in3, in4
- Parameter _prm_: no hdcp, hdcp1.4, hdcp2.2
- Example: `GET VIDIN_HDCP in1`
  - Return: `VIDIN_HDCP in1 HDCP1.4`

#### Get Output connection status

Get the connection status of the output

- Command: `GET VIDOUT_CONNECT out`
- Return: `VIDOUT_CONNECT in prm`
- Parameter _out_: out1, out2, out3, out4
- Parameter _prm_: Disconnected, Connected
- Example: `GET VIDOUT_CONNECT out1`
  - Return: `VIDOUT_CONNECT out1 Connected`

#### Get Output signal status

Get the signal status of the video output

- Command: `GET VIDOUT_SIG out`
- Return: `VIDOUT_SIG out prm`
- Parameter _out_: out1, out2, out3, out4
- Parameter _prm_: no, valid
- Example: `GET VIDOUT_SIG out1`
  - Return: `VIDOUT_SIG out1 Valid`

#### Get Output video format

Get the Outputs video format information

- Command: `GET VIDOUT_FORMAT out`
- Return: `VIDOUT_FORMAT out prm`
- Parameter _out_: out1, out2, out3, out4
- Parameter _prm_: {}
  - prm = `{<horizontal>x<vertical>,<rate>;<HDRinfo>;<ColorSpace>,<DeepColor>}`
  - horizontal = An integer value representing the horizontal
  - vertical = An integer value representing the vertical. May have an additional qualifier such as 'i' or 'p'
  - rate = An integer value representing the refresh rate
  - HDR info = none hdr / static hdr / dynamic hdr
  - Color space = RGB / Ycbcr 444 / Ycbcr 422 / Ycbcr 420
  - DeepColor = 8 bit / 10 bit / 12 bit / 16 bit
- Example: `GET VIDOUT_FORMAT out1`
  - Return: `VIDOUT_FORMAT out1 3840x2160,60;None HDR;RGB;8bit`

#### Get Output HDCP version

Get the Version of HDCP on selected output

- Command: `GET VIDOUT_HDCP out`
- Return: `VIDOUT_HDCP out prm`
- Parameter _out_: out1, out2, out3, out4
- Parameter _prm_: no hdcp, hdcp1.4, hdcp2.2
- Example: `GET VIDOUT_HDCP out2`
  - Return: `VIDOUT_HDCP out2 HDCP2.2`

### Update Info

#### Firmware Version

Get the current firmware version

- Command: `GET VER`
- Return: `VER prm`
- Parameter: The firmware version on the unit
- Example: `GET VER`
  - Return: `VER ARM VER V1.2.8 MCU VER V2.0.8`

#### Hardware Version

Get the current hardware version

- Command: `GET HW_VER`
- Return: `HW_VER prm`
- Parameter: The hardware version on the unit
- Example: `GET HW_VER`
  - Return: `HW_VER V0.1`

### Preset Info

#### Save Preset

Save up too 3 Preset Scenes

- Command: `SAVE PRESET prm`
- Return: `PRESET prm`
- Parameter: 1, 2, 3
- Example: `SAVE PRESET 1`
  - Return: `PRESET 1`

#### Restore Preset

Load the preset

- Command: `RESTORE PRESET prm`
- Return: `PRESET prm`
- Parameter: 1, 2, 3
- Example: `RESTORE PRESET 1`
  - Return: `PRESET 1`

### Video Output

#### Set Video Output Scaling

Set the scaling mode of the video output

- Command: `SET VIDOUT_SCALE out prm`
- Return: `VIDOUT_SCALE out prm`
- Parameter _out_: out1, out2, out3, out4, all
- Parameter _prm_: auto, manual, bypass
  - auto = matches TV EDID automatically
  - manual = Change the scalar output resolution
  - bypass = bypass all HDMI source signal to display
    - **note: only on output 1 and 2**
- Example: `SET VIDOUT_SCALE out1 auto`
  - Return: `VIDOUT_SCALE out1 auto`

#### Get Video Output Scaling

Get the scaling mode of the video output

- Command: `GET VIDOUT_SCALE out`
- Return: `VIDOUT_SCALE out prm`
- Parameter _out_: out1, out2, out3, out4, all
- Parameter _prm_: auto, manual, bypass
- Example: `GET VIDOUT_SCALE out1`
  - Return: `VIDOUT_SCALE out1 auto`

#### Set Output Resolution

Set the output resolution for one or all the outputs

- Command: `SET VIDOUT_RES out`
- Return: `VIDOUT_RES out prm`
- Parameter _out_: out1, out2, out3, out4, all
- Parameter _prm_: {}

  - prm =

    ```text
    4096x2160@60
    4096x2160@30
    4096x2160@25
    4096x2160@24
    3840x2160@60
    3840x2160@50
    3840x2160@30
    3840x2160@25
    3840x2160@24
    1920x1200@60
    1920x1080@60
    1920x1080@50
    1280x720@60
    1280x720@50
    1680x1050@60
    1600x1200@60
    1600x900@60
    1440x900@60
    1366x768@60
    1360x768@60
    1280x1024@60
    1280x960@60
    1280x800@60
    1280x768@60
    1024x768@60
    800x600@60
    ```

- Example: `SET VIDOUT_RES out1 3840x2160@60`
  - Return: `VIDOUT_RES out1 3840x2160@60`
- Note: Must set scaling to `manual` first

#### Get Output Resolution

Get the Output Resolution of one or all outputs

- Command: `GET VIDOUT_RES out`
- Return: `VIDOUT_RES out prm`
- Parameter _out_: out1, out2, out3, out4, all
- Parameter _prm_: {}

  - prm =

    ```text
    4096x2160@60
    4096x2160@30
    4096x2160@25
    4096x2160@24
    3840x2160@60
    3840x2160@50
    3840x2160@30
    3840x2160@25
    3840x2160@24
    1920x1200@60
    1920x1080@60
    1920x1080@50
    1280x720@60
    1280x720@50
    1680x1050@60
    1600x1200@60
    1600x900@60
    1440x900@60
    1366x768@60
    1360x768@60
    1280x1024@60
    1280x960@60
    1280x800@60
    1280x768@60
    1024x768@60
    800x600@60
    ```

- Example: `GET VIDOUT_RES all`

  - Return:

    ```text
    VIDOUT_RES out1 3840x2160@60
    VIDOUT_RES out2 1920x1080@60
    VIDOUT_RES out3 1920x1080@60
    VIDOUT_RES out4 1920x1080@60
    ```

### RS232 Settings

| Parameters   |            |
| ------------ | ---------- |
| Baud Rate    | 115200 bps |
| Data bits    | 8 bits     |
| Parity       | None       |
| Stop bits    | 1 bit      |
| Flow control | None       |

### Telnet/TCP Settings

Connect a control PC to the LAN port of the device. Before you intend to control the device through telnet API, you shall establish connection between this device and your computer. The form of the command for telnet connection is below: **telnet ip (port)**

- _ip:_ The device's IP address.
- _port:_ The device's port number, this is not required for some Telnet control tools. Default setting is 23.

For example, if the device’s IP address is `192.168.11.143`, the command for telnet connection shall be the following:
`telnet 192.168.11.143`

#### Obtain IP address of the Device

To obtain the device’s IP address:

1. Connect a control PC to the RS232 port of the device.
2. Configure RS232 parameters for the PC’s serial port correctly through a RS232 serial port tool, such as Serial Assist.
3. Input the command `GET IPADDR<CR><LF>` and send. You will get a response with IP address, see following:

**Input:**
`GET IPADDR<CR><LF>`

**Response:**
`IPADDR 172.16.18.173 MASK 255.255.255.0 GATEWAY 172.16.18.1`

![Serial Assist](<Assets/Screenshot 2023-12-04 at 3.07.21 PM.png>)

Note: When all is configured properly, you can control the device through commands, which are available in the separate document.

## IR Commands

| Output   | Action   | Standard Code | Expanded Code                                                                                                                                                                                                                                                                                                                                                                               |
| -------- | -------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Output 1 | Source 1 | 0x00 0x09     | 0000 006D 0022 0002 0155 00AA 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0015 0015 0015 0015 0040 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 05ED 0155 0055 0015 0E47 |
| Output 1 | Source 2 | 0x00 0x1D     | 0000 006D 0022 0002 0155 00AA 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0015 0015 0040 0015 0040 0015 0040 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 05ED 0155 0055 0015 0E47 |
| Output 1 | Source 3 | 0x00 0x1F     | 0000 006D 0022 0002 0155 00AA 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 05ED 0155 0055 0015 0E47 |
| Output 1 | Source 4 | 0x00 0x0D     | 0000 006D 0022 0002 0155 00AA 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0015 0015 0040 0015 0040 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 05ED 0155 0055 0015 0E47 |
| Output 1 | Right    | 0x00 0x41     | 0000 006D 0022 0002 0155 00AA 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0015 0015 0040 0015 05ED 0155 0055 0015 0E47 |
| Output 1 | Left     | 0x00 0x57     | 0000 006D 0022 0002 0155 00AA 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0015 0015 0040 0015 0015 0015 0040 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0015 0015 0040 0015 0015 0015 0040 0015 05ED 0155 0055 0015 0E47 |
| Output 2 | Source 1 | 0x00 0x17     | 0000 006D 0022 0002 0155 00AA 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0015 0015 0040 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0015 0015 0040 0015 0040 0015 0040 0015 05ED 0155 0055 0015 0E47 |
| Output 2 | Source 2 | 0x00 0x12     | 0000 006D 0022 0002 0155 00AA 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0015 0015 0040 0015 0015 0015 0015 0015 0040 0015 0015 0015 0015 0015 0015 0015 0040 0015 0015 0015 0040 0015 0040 0015 0015 0015 0040 0015 0040 0015 0040 0015 05ED 0155 0055 0015 0E47 |
| Output 2 | Source 3 | 0x00 0x59     | 0000 006D 0022 0002 0155 00AA 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0015 0015 0015 0015 0040 0015 0040 0015 0015 0015 0040 0015 0015 0015 0015 0015 0040 0015 0040 0015 0015 0015 0015 0015 0040 0015 0015 0015 0040 0015 05ED 0155 0055 0015 0E47 |
| Output 2 | Source 4 | 0x00 0x08     | 0000 006D 0022 0002 0155 00AA 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0015 0015 0015 0015 0015 0015 0040 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 05ED 0155 0055 0015 0E47 |
| Output 2 | Right    | 0x00 0x11     | 0000 006D 0022 0002 0155 00AA 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0015 0015 0015 0015 0015 0015 0040 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 0015 0015 0040 0015 0040 0015 0040 0015 05ED 0155 0055 0015 0E47 |
| Output 2 | Left     | 0x00 0x1B     | 0000 006D 0022 0002 0155 00AA 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0015 0015 0040 0015 0040 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 05ED 0155 0055 0015 0E47 |
| Output 3 | Source 1 | 0x00 0x5E     | 0000 006D 0022 0002 0155 00AA 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 0015 0015 0040 0015 0015 0015 0040 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0015 0015 0040 0015 05ED 0155 0055 0015 0E47 |
| Output 3 | Source 2 | 0x00 0x06     | 0000 006D 0022 0002 0155 00AA 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0015 0015 0040 0015 0040 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 05ED 0155 0055 0015 0E47 |
| Output 3 | Source 3 | 0x00 0x05     | 0000 006D 0022 0002 0155 00AA 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0015 0015 0040 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 05ED 0155 0055 0015 0E47 |
| Output 3 | Source 4 | 0x00 0x03     | 0000 006D 0022 0002 0155 00AA 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 05ED 0155 0055 0015 0E47 |
| Output 3 | Right    | 0x00 0x48     | 0000 006D 0022 0002 0155 00AA 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0015 0015 0015 0015 0015 0015 0040 0015 0015 0015 0015 0015 0040 0015 0015 0015 0040 0015 0040 0015 0040 0015 0015 0015 0040 0015 0040 0015 0015 0015 0040 0015 05ED 0155 0055 0015 0E47 |
| Output 3 | Left     | 0x00 0x55     | 0000 006D 0022 0002 0155 00AA 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0015 0015 0040 0015 0015 0015 0040 0015 0015 0015 0040 0015 0015 0015 0015 0015 0040 0015 0015 0015 0040 0015 0015 0015 0040 0015 0015 0015 0040 0015 05ED 0155 0055 0015 0E47 |
| Output 4 | Source 1 | 0x00 0x18     | 0000 006D 0022 0002 0155 00AA 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 05ED 0155 0055 0015 0E47 |
| Output 4 | Source 2 | 0x00 0x44     | 0000 006D 0022 0002 0155 00AA 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0015 0015 0015 0015 0040 0015 0015 0015 0015 0015 0015 0015 0040 0015 0015 0015 0040 0015 0040 0015 0015 0015 0040 0015 0040 0015 0040 0015 0015 0015 0040 0015 05ED 0155 0055 0015 0E47 |
| Output 4 | Source 3 | 0x00 0x0F     | 0000 006D 0022 0002 0155 00AA 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 05ED 0155 0055 0015 0E47 |
| Output 4 | Source 4 | 0x00 0x51     | 0000 006D 0022 0002 0155 00AA 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0015 0015 0015 0015 0015 0015 0040 0015 0015 0015 0040 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 0015 0015 0040 0015 0015 0015 0040 0015 05ED 0155 0055 0015 0E47 |
| Output 4 | Right    | 0x00 0x40     | 0000 006D 0022 0002 0155 00AA 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0015 0015 0040 0015 05ED 0155 0055 0015 0E47 |
| Output 4 | Left     | 0x00 0x07     | 0000 006D 0022 0002 0155 00AA 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 05ED 0155 0055 0015 0E47 |
