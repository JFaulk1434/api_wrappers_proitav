# Websocket for Murideo 8K Seven Generator

## Table of Contents

- [Websocket for Murideo 8K Seven Generator](#websocket-for-murideo-8k-seven-generator)
  - [Table of Contents](#table-of-contents)
    - [Dictionary](#dictionary)
    - [Where to locate commands](#where-to-locate-commands)

### Dictionary

Format for the dictionary is the following:

```python
Murideo_WebUI = {  # Master Dictionary for WebUI of Murideo 8K Seven Genderator
    "video_generator": {
        "timing": {
            "function": "sendsingle",  # Function needed to send the command ex: SENDSINGLE||97,110
            "category_type": 97, # ID For the category in this case it's 97=Timing
            "8k": {
                "7680x4320@30": {
                    "id": 110, # command to be called for this resolution
                    "h_rez": 7680, # Horizontal Pixels
                    "v_rez": 4320, # Vertical Pixels
                    "refresh": 30, # Refresh Rate
                    "tag": "7680x4320 30Hz", # The actual Button text
                },
                "7680x4320@29.97": {
                    "id": 111, # command to be called for this resolution
                    "h_rez": 7680, # Horizontal Pixels
                    "v_rez": 4320, # Vertical Pixels
                    "refresh": 29.97, # Refresh Rate
                    "tag": "7680x4320 29.97Hz", # The actual Button text
                },
                "7680x4320@25": {
                    "id": 112, # command to be called for this resolution
                    "h_rez": 7680, # Horizontal Pixels
                    "v_rez": 4320, # Vertical Pixels
                    "refresh": 25, # Refresh Rate
                    "tag": "7680x4320 25Hz", # The actual Button text
                },
                "7680x4320@24": {
                    "id": 113, # command to be called for this resolution
                    "h_rez": 7680, # Horizontal Pixels
                    "v_rez": 4320, # Vertical Pixels
                    "refresh": 24, # Refresh Rate
                    "tag": "7680x4320 24Hz", # The actual Button text
                },
                "7680x4320@23.98": {
                    "id": 114, # command to be called for this resolution
                    "h_rez": 7680, # Horizontal Pixels
                    "v_rez": 4320, # Vertical Pixels
                    "refresh": 23.98, # Refresh Rate
                    "tag": "7680x4320 23.98Hz", # The actual Button text
                },
                "7680x4320@60": {
                    "id": 115, # command to be called for this resolution
                    "h_rez": 7680, # Horizontal Pixels
                    "v_rez": 4320, # Vertical Pixels
                    "refresh": 60, # Refresh Rate
                    "tag": "7680x4320 60Hz", # The actual Button text
                },
                "7680x4320@59.94": {
                    "id": 116, # command to be called for this resolution
                    "h_rez": 7680, # Horizontal Pixels
                    "v_rez": 4320, # Vertical Pixels
                    "refresh": 59.94, # Refresh Rate
                    "tag": "7680x4320 59.94Hz", # The actual Button text
                },
                "7680x4320@50": {
                    "id": 117, # command to be called for this resolution
                    "h_rez": 7680, # Horizontal Pixels
                    "v_rez": 4320, # Vertical Pixels
                    "refresh": 50, # Refresh Rate
                    "tag": "7680x4320 50Hz", # The actual Button text
                },
                "7680x4320@48": {
                    "id": 118, # command to be called for this resolution
                    "h_rez": 7680, # Horizontal Pixels
                    "v_rez": 4320, # Vertical Pixels
                    "refresh": 48, # Refresh Rate
                    "tag": "7680x4320 48Hz", # The actual Button text
                },
                "7680x4320@47.95": {
                    "id": 119, # command to be called for this resolution
                    "h_rez": 7680, # Horizontal Pixels
                    "v_rez": 4320, # Vertical Pixels
                    "refresh": 47.95, # Refresh Rate
                    "tag": "7680x4320 47.95Hz", # The actual Button text
                },
            },
            "uhd": {
                1: {
                    "id": 28,
                    "h_rez": 3840,
                    "v_rez": 2160,
                    "refresh": 30,
                    "tag": "3840x2160 30Hz",
                },
            },
            "4k-dci": {
                1: {
                    "id": 53,
                    "h_rez": 4096,
                    "v_rez": 2160,
                    "refresh": 30,
                    "tag": "4096x2160 30Hz",
                },
            },
        }
    }
}
```

### Where to locate commands

When inspecting the webUI the websocket is listed as `uart` under the network tab. When pressing buttons you will see commands being sent like `SENDSINGLE||97,53`.
