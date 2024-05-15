# VW-4K-2X2 User Manual

4K 4x4 Seamless Matrix Switcher with 2x2 Video Wall
v1.1
![Alt text](Assets/CustomerPhotoFront.png)

- [VW-4K-2X2 User Manual](#vw-4k-2x2-user-manual)
  - [Introduction](#introduction)
    - [Overview](#overview)
    - [Features](#features)
    - [Package Contents](#package-contents)
    - [Specifications](#specifications)
    - [Panel Description](#panel-description)
  - [Installation and Wiring](#installation-and-wiring)
    - [Installation](#installation)
    - [Wiring](#wiring)
  - [Control](#control)
    - [Buttons](#buttons)
    - [IR](#ir)
    - [API Commands](#api-commands)
      - [RS232](#rs232)
      - [Telnet/TCP](#telnettcp)
        - [Obtain IP address of the Device](#obtain-ip-address-of-the-device)
    - [Web UI](#web-ui)
      - [Matrix Control](#matrix-control)
        - [Video Mode](#video-mode)
          - [Matrix Switcher](#matrix-switcher)
          - [Video Wall](#video-wall)
        - [HDMI A/V Mute](#hdmi-av-mute)
        - [De-Embedded Audio Mute](#de-embedded-audio-mute)
        - [Scaling](#scaling)
        - [Presets Matrix Control](#presets-matrix-control)
      - [General Settings](#general-settings)
        - [Source Naming](#source-naming)
        - [Zone Naming](#zone-naming)
      - [Advanced Settings](#advanced-settings)
        - [Lower Power Mode](#lower-power-mode)
        - [EDID Presets](#edid-presets)
        - [EDID Read](#edid-read)
        - [CEC Control](#cec-control)
        - [HDCP](#hdcp)
        - [Change Login Password](#change-login-password)
        - [Network](#network)
        - [Custom Web UI Logo](#custom-web-ui-logo)
        - [System Version](#system-version)
        - [FW Update](#fw-update)
        - [System](#system)
        - [Log](#log)

## Introduction

### Overview

This product is a full 4K 4x4 HDMI seamless matrix switcher. It features compact enclosure, instant switching and scaling up to 4K@60Hz SDR and HDR. It allows four sources to be switched to four HDMI outputs, while providing both analog and digital S/PDIF audio de-embedding for outputs 1 & 2. The product can be easily managed and controlled, for example through front panel buttons, IR, RS232, web UI and TCP protocols. The product is perfect for applications where 4K seamless switching is required. It also supports Videowall in a 2x2 layout. The ability to adjust for the display bezels and the ability to flip the displays 180° if needed to install upside down.

### Features

- Seamless switching without seeing a black screen between four HDMI inputs and outputs.
- Each HDMI input and output support video format up to 4K@60Hz SDR and HDR.
- HDCP 2.2 compliant and backward compatible.
- EDID management including EDID presets, EDID copy and custom EDID.
- Advanced video processing capabilities:
  - Supports free scaling between 480p and 4K@60Hz.
  - Supports conversion between SDR and HDR formats.
  - Supports conversion on color space, chroma and color bits.
  - Supports instant switching between sources so black screen transition is avoided.
  - Supports rich scaler processing modes, including auto scaler, manual scaler and video bypass.
  - 2x2 Video Wall with bezel adjustments.
  - Video rotation 180° for installing displays upside down.
- Can be easily managed and controlled through front panel buttons, IR, RS232, web UI and TCP protocols.
- Supports firmware upgrade through web UI and Micro USB port.

### Package Contents

- 1 x Matrix Switcher
- 1 x DC 12V 3A Power Adapter
- 1 x IR Remote Controller
- 1 x IR Receiver Cable
- 1 x AC Power Cord (with US Pins)
- 1 x 3.5mm 3-Pin Phoenix Male Connector
- 2 x 3.5mm 5-Pin Phoenix Male Connector
- 2 x Mounting Brackets (with Screws)

### Specifications

| Technical                         |                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Input/Output Ports                | 4 x HDMI IN, 4 x HDMI OUT, 1 x RS-232, 1 x LAN (RJ45), 2 x S/PDIF OUT, 2 x Analog AUDIO OUT, 1 x FW (Micro USB), 1 x DC 12V                                                                                                                                                                                                                               |
| Input/Output Signal               | HDMI with 4K@60Hz 4:4:4                                                                                                                                                                                                                                                                                                                                   |
| Input/Output Resolution Supported | **VESA:** 800x600^8^, 1024x768^8^, 1280x768^8^, 1280x800^8^, 1280x960^8^, 1280x1024^8^,1360x768^8^, 1366x768^8^, 1440x900^8^, 1600x900^8^, 1600x1200^8^, 1680x1050^8^,1920x1200^8^ <br> **SMPTE:** 720x576P^6^, 1280x720P^6,7,8^ 1920x1080P^2,5,6,7,8^, 3840x2160^2,3,5,6,8^, 4096x2160^2,3,5,6,8^ <br> 2=24Hz, 3=25Hz, 5=30Hz, 6=50Hz, 7=59.94Hz, 8=60Hz |
| Audio Format                      | **HDMI IN/OUT:** Fully supports audio formats in HDMI 2.0 specification, including PCM 2.0/5.1/7.1,Dolby TrueHD, Dolby Atmos, DTS HD Master Audio and DTS:X <br> **AUDIO OUT:** Balance stereo audio <br> **S/PDIF OUT:** PCM 2.0/5.1, Dolby digital and DTS up to 5.1 Channel                                                                            |
| Maximum Data Rate                 | 18Gbps                                                                                                                                                                                                                                                                                                                                                    |
| Control Method                    | Front Panel Buttons, RS232, IR, LAN (Telnet & Web UI)                                                                                                                                                                                                                                                                                                     |

| General                           |                                                                                  |
| --------------------------------- | -------------------------------------------------------------------------------- |
| Operating Temperature             | 0°C to 45°C (32°F to 113°F)                                                      |
| Storage Temperature               | -20°C to 70°C (-4°F to 158°F)                                                    |
| Humidity                          | 10% to 90%, non-condensing                                                       |
| ESD Protection                    | **Human-body Model:** <br> ±8kV (Air-gap discharge) <br>±4kV (Contact discharge) |
| Power Supply                      | DC 12v                                                                           |
| Power Consumption _(Max)_         | 16 Watts                                                                         |
| Dimensions _US_ _(W x H x D)_     | 8.46" x 1.65" x 5.52"                                                            |
| Dimensions _Metric_ _(W x H x D)_ | 215mm x 42mm x 140.2mm                                                           |
| Product Weight                    | 2.64lbs / 1.2kg                                                                  |

| Cable Type | Range                                 | Supported Video                              |
| ---------- | ------------------------------------- | -------------------------------------------- |
| HDMI       | Input: 50ft/15m <br> Output: 33ft/10m | 1080P@60Hz 24bpp                             |
| HDMI       | Input/Output: 33ft/10m                | 4K@30Hz 4:4:4 24bpp <br> 4K@60Hz 4:2:0 24bpp |
| HDMI       | Input/Output: 10ft/3m                 | 4K@60Hz 4:4:4 24bpp                          |

### Panel Description

![Front Panel](Assets/frontpanel.png)

| ID  | Name          | Description                                                                                                                                                                                                                                                                                                                |
| --- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Power LED     | On: The device is powered on. <br> Off: The device is powered off.                                                                                                                                                                                                                                                         |
| 2   | Input Select  | Input selection LED's and buttons for input ports _(1-4)_ <br> **LED On:** The input port is selected.<br> **LED Blinking:** The input port is routed to a specific output.<br> **LED Off:** The input port is not selected.<br> Input selection buttons (1-4): press to select specific input port.                       |
| 3   | Output Select | Output selection LEDs and buttons for output ports _(1-4)_. <br>**LED On:** The output port is selected.<br> **LED Blinking:** The output port is routed to a specific input port.<br>**LED Off:** The output port is not selected.<br>Output selection buttons _(1-4)_: press to select or deselect specific output port. |
| 4   | Enter         | Press this button to perform the input and output selection.                                                                                                                                                                                                                                                               |

![Rear Panel](Assets/rearpanel.png)

| ID  | Name             | Description                                                                                          |
| --- | ---------------- | ---------------------------------------------------------------------------------------------------- |
| 1   | 12v              | Connect to the power adapter and AC power cord provided for power input.                             |
| 2   | HDMI In _(1-4)_  | Connect the HDMI source devices.                                                                     |
| 3   | HDMI Out _(1-4)_ | Connect to the HDMI display devices.                                                                 |
| 4   | FW               | Connect to the PC for Firmware Upgrade.                                                              |
| 5   | RS232            | Connect to the PC for RS232 Control on this device.                                                  |
| 6   | LAN              | Connect to network (ex: network switch, router, computer, etc.) for LAN control via WebUI or Telnet. |
| 7   | IR EXT.          | IR extension port. Connect to the IR Receiver Cable.                                                 |
| 8   | AUDIO OUT1       | Analog audio de-embedded output from HDMI out 1. Connect to an amplifier or a speaker.               |
| 9   | S/PDIF OUT1      | Digital audio de-embedded output from HDMI out 1. Connect to an A/V receiver or similar.             |
| 10  | AUDIO OUT2       | Analog audio de-embedded output from HDMI out 2. Connect to an amplifier or a speaker.               |
| 11  | S/PDIF OUT2      | Digital audio de-embedded output from HDMI out 2. Connect to an A/V receiver or similar.             |

## Installation and Wiring

**Warnings:**

- Before Installation and wiring, disconnect power from the device.
- During wiring, connect and disconnect the cables gently.

### Installation

1. Attach the bracket to one side of the enclosure using the
   screws provided. The bracket is attached to the enclosure as
   shown.
   ![Bracket](Assets/bracket.png)
2. Repeat step 1 for the other side of the enclosure.
3. Attach the brackets to the surface or location desired using screws (surface mount screws not included in the package).

### Wiring

![Wiring](Assets/wiring.png)

## Control

### Buttons

Users can perform basic switching of input sources to output
displays using front panel buttons.

To select an input source for the output display:

1. Press one or multiple buttons of OUT 1-4 to select output port(s). The LED will light up once specific output port is selected.
2. Press one button of IN 1-4 to select an input port. The LED will light up one specific input port is selected.
3. Press the ENTER button to implement the selection. The selection takes effect when the LEDs are off.

### IR

The device can be controlled by the IR remote controller.
Connect the IR receiver cable to the IR EXT. port at the rear
panel of the device and ensure the receiver eye is accessible to
the remote controller.

![Remote](Assets/remote.png)

To select an input source for one output display:

1. Connect the IR receiver cable to the IR EXT. port at the rear
   panel of the device.
2. Select the target output display from the column 1-4.
3. Press the target input port number or previous( < ) or next( > ) button to select the desired input source.

### API Commands

Advanced users may need to control the device via API commands. Two methods are provided for controlling this device through API commands:

#### RS232

Connect a control PC to the RS232 port of the device. Before sending API commands to control the device, ensure the serial ports between this device and PC are configured correctly. A professional RS232 serial interface software (e.g. Serial Assist) may be needed as well.

| Parameters   | Default Value |
| ------------ | ------------- |
| Baud Rate    | 115200 bps    |
| Data bits    | 8 bits        |
| Parity       | None          |
| Stop bits    | 1 bit         |
| Flow control | None          |

#### Telnet/TCP

Connect a control PC to the LAN port of the device. Before you intend to control the device through telnet API, you shall establish connection between this device and your computer. The form of the command for telnet connection is below: **telnet ip (port)**

- _ip:_ The device's IP address.
- _port:_ The device's port number, this is not required for some Telnet control tools. Default setting is 23.

For example, if the device’s IP address is `192.168.11.143`, the command for telnet connection shall be the following:
`telnet 192.168.11.143`

##### Obtain IP address of the Device

To obtain the device’s IP address:

1. Connect a control PC to the RS232 port of the device.
2. Configure RS232 parameters for the PC’s serial port correctly through a RS232 serial port tool, such as Serial Assist.
3. Input the command `GET IPADDR<CR><LF>` and send. You will get a response with IP address, see following:

**Input:**
`GET IPADDR<CR><LF>`

**Response:**
`IPADDR 172.16.18.173 MASK 255.255.255.0 GATEWAY 172.16.18.1`

![Serial Assist](Assets/uart.png)

Note: When all is configured properly, you can control the device through commands, which are available in the API documentation.

### Web UI

The Web UI designed for this device allows for basic controls and advanced settings. It can be accessed through a modern browser, e.g. Chrome, Safari, Firefox, IE10+, etc.

To get access the Web UI:

1. Connect the LAN port of the device to a local area network. (Ensure there’s a DHCP server in the network so that the device can obtain a valid IP address.)
2. Connect the PC to the same network as this device.
3. Input the device’s IP address in the browser and press `Enter` and wait for the login page (Refer to Obtain IP Address of the Device section to get the device’s IP address quickly).
4. Input the password (default password: admin) and click Login.
5. Input a new password in the dialog box and click Apply to enter the main page. The password shall be alphanumeric with 4 to 16 characters in length.

#### Matrix Control

##### Video Mode

###### Matrix Switcher

![Matrix Switcher](Assets/matrix.png)
This section manages distribution of input sources to output displays. Click the button in the table to select the input for the output display (button turns from white to green once selection is done).

- ALL OUTPUTS: Click to route INPUT (n) for all OUTPUTs. Default setting: Input 1 is routed to Output 1, …, Input (n) is routed to Output (n), n = 1, 2, 3, 4.
- CEC Control:
  - On: Click to power on the display connected to the output selected through CEC.
  - Off: Click to power off the display connected to the output selected through CEC.
- Video Details: Click to view detailed information of input and output ports including status, resolution, framerate, etc., see following:
  ![Video Details](Assets/videodetails.png)

###### Video Wall

![Video Wall](Assets/videowall.png)
This section manages the Video Wall settings. First select the correct OUTPUT connected the to the Video Wall. In this example the Top Left Display is connected to OUTPUT1.

- Video Wall Input
  - Here you select which input is to be displayed on the video wall.
- Video Wall Flip
  - When installing the video wall if you needed to install some displays upside down because of the type of bezel you can flip it by selecting the check box.
- Bezel Adjustment
  - Here you need to set the size of the Bezel around each display so the final display looks correct.
  - The measurement is in _Millimeters_
  - Fill in the following fields:
    - VW: _Viewing Width_
    - OW: _Outer Width_
    - VH: _Viewing Height_
    - OH: _Outer Height_

##### HDMI A/V Mute

![HDMI Mute](Assets/hdmimute.png)

- ON: Select to mute video and audio for selected HDMI output port.
- OFF: Select to unmute video and audio for selected HDMI output port.
  - Default setting: OFF

##### De-Embedded Audio Mute

![De-embedding](Assets/deembeddingaudiomute.png)

- ON: Select to mute de-embedded audio for selected audio output ports.
- OFF: Select to unmute de-embedded audio for selected audio output ports.
  - Default setting: OFF

##### Scaling

![Scaling](Assets/Scaling.png)

This section manages scaler configurations for Output 1-4. Three operation options are provided for each output scaler.

- Auto: Select to automatically adapt to display EDID and resolution. E.g. If the display supports up to 4K@30Hz, the device will output signal with 4K@30Hz.
- Manual: Select a desired output resolution from the Resolution dropdown menu for the selected output port.
- Bypass: Select to bypass the input video source to the selected output port. When “Bypass” is selected, black screen may occur on the display if unsupported resolutions are switched to the display.

Note: “Auto” and “Manual” options are available for all output ports (1 to 4), while “Bypass” is available for Output 1 and Output 2 only.

##### Presets Matrix Control

![Preset Matrix](Assets/presetmatrix.png)

This section saves or loads the settings of or to Video Matrix Control section.

- Save: Click to save settings of Video Matrix Control section.
- Load: Click to load settings to Video Matrix Control section.

To save a setting of Video Matrix to Preset 1:

1. Complete the input and output routing in Video Matrix Control section.
2. Click “Save” in “Preset 1”. Then the “Preset 1” is saved successfully.

#### General Settings

##### Source Naming

![Source Naming](Assets/sourcenaming.png)

This section allows you to change to new input ports’ names.

- Save: Click to save and apply all changes.
- Reset: Click to reset all changes.

Note: The length of each new name shall not exceed 15 characters.

##### Zone Naming

![Zone Naming](Assets/zonenaming.png)

This section allows you to change the output names.

- Save: Click to save and apply all changes.
- Reset: Click to reset all changes.

Note: The length of each new name shall not exceed 15 characters.

#### Advanced Settings

##### Lower Power Mode

This section provides setting of Lower Power Mode. In Low Power Mode, the device will shut down all video outputs and enter standby status.

- ON: Select to turn on Lower Power Mode to make the device enter standby status.
  - Note: When on is selected, the web UI page will log out, you need to re-login to enter the main page.
- OFF: Select to turn off Lower Power Mode to make the device work properly.
  - Default setting: OFF

##### EDID Presets

![EDID Presets](Assets/edidpresets.png)

This section allows you to configure EDID setting for each input port. Available EDID options are provided from the dropdown menu, click to select a desired option.

- Copy From Output 1
- Copy From Output 2
- Copy From Output 3
- Copy From Output 4
- 4K60 2.0CH PCM Audio with HDR
- 4K60 2.0CH PCM Audio with SDR
- 4K30 2.0CH PCM Audio with HDR
- 4K30 2.0CH PCM Audio with SDR
- 1080p@60Hz 2.0CH PCM Audio with HDR
- 1080p@60Hz 2.0CH PCM Audio with SDR
- EDID Write

##### EDID Read

Click Enter to enter EDID Setting page, select the desired HDMI output and click to “Read” its EDID information.
![EDID Read](Assets/edidread.png)

- Read: Click to read the selected output port’s EDID information.
- Write: Click to write EDID information to the selected input port.
- Export: Click to export EDID file to your local computer.
- Import: Click to import EDID file from your local computer.

##### CEC Control

![CEC Control](Assets/ceccontrol.png)

- **Note: Display must support CEC and have that feature enabled.**
- Display On: Click to power on the display connected to the output selected.
- Display Off: Click to power off the display connected to the output selected.
- Auto On/Off: Select to enable or disable CEC Auto Control.
  Default setting: Off
- Auto Delay Time (1~30min): Click the up/down arrow to set the time for the display to power off automatically when no signal is present. For example, if the time is set to 2 minutes, the output display will power off automatically when there’s no signal at the display for 2 minutes.

##### HDCP

![HDCP](Assets/hdcp.png)

This section allows you to enable or disable HDCP encryption of each input port.

- On: Select to enable HDCP encryption for the selected input port.
- Off: Select to disable HDCP encryption for the selected input port.
  - Default setting: On

##### Change Login Password

![Change Login](Assets/changelogin.png)
This section is to change login password.
Default setting: `admin`
Note: Password must be 4 to 16 characters in length, alphanumeric only.

##### Network

![Network](Assets/network.png)
This section is to set the network mode between static and dynamic IP address (DHCP).

- IP Type:
  - DHCP: When enabled, the IP address of the Matrix is assigned automatically by the DHCP server connected.
  - Static: When enabled, you need to set up the IP address, Subnet Mask, and Gateway manually.
- Default setting: DHCP
- Save: Click to save and perform the network setting, and the setting change will take effect immediately.

Note: When "Static" is selected, please ensure your PC is in the same network segment as the device.

##### Custom Web UI Logo

![Custom WebUI Logo](Assets/customwebui.png)
This section allows you to create your own logo for the Web UI.

- To create customized Web UI logo: click “Browse” for the new logo file, and choose “Apply”.

Note: The new logo used should be in PNG format and less than 300x60 pixels.

##### System Version

This section provides Web UI and MCU version information.

##### FW Update

![Firmware Update](Assets/firmwareupdate.png)
To update device’s firmware:

1. Click “Browse” for the update file.
2. Click “Update” to perform upgrade. The update will be completed when the progress bar reaches 100%.

Note: The device will reboot automatically when firmware update is completed successfully. Please wait for about 2-3 minutes, then refresh and log in again **DO NOT power off the device during the updating process.**

##### System

- Reboot: Click to reboot device.
- Factory Reset: Click to reset the device to factory default.

##### Log

This section displays system setting change records. Click “Export Log” to download the log to your local computer.
