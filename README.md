[![GitHub All Releases][downloads_total_shield]][releases]
[![PayPal.Me][paypal_me_shield]][paypal_me]

# SmartThings Soundbar

Adds support for SmartThings enabled Soundbar

## Features

- Turn on/off
- Set volume
- Step volume up/down
- Mute/unmute
- Select source
- Select soundmode
- Show current volume level
- Show current state: on/off/playing/paused/idle
- Show if muted/unmuted
- Show current source
- Switch Night mode, Bass boost, Voice amplifier

## Configuration options

| Key          | Type               | Required | Default                | Description                                                                                                                                               |
| -------------- | -------------------- | ---------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`       | `string`           | `False`  | `SmartThings Soundbar` | Name of soundbar                                                                                                                                          |
| `api_key`    | `string`           | `True`   | -                      | SmartThings API key (see:[here](https://github.com/PiotrMachowski/Home-Assistant-custom-components-SmartThings-Soundbar#getting-api-key-and-device-id))   |
| `device_id`  | `string`           | `True`   | -                      | SmartThings device id (see:[here](https://github.com/PiotrMachowski/Home-Assistant-custom-components-SmartThings-Soundbar#getting-api-key-and-device-id)) |
| `max_volume` | `positive integer` | `False`  | 100                    | Volume level that will be used as a maximum level in Home Assistant                                                                                       |

## Examples usage

```yaml
media_player:
  - platform: smartthings_soundbar
    name: Soundbar
    api_key: "YOUR API KEY"
    device_id: "YOUR DEVICE ID"
    max_volume: 30
```

```yaml
switch:
  - platform: smartthings_soundbar
    name: night_mode
    api_key: "YOUR API KEY"
    device_id: "YOUR DEVICE ID"
 - platform: smartthings_soundbar
    name: bass_boost
    api_key: "YOUR API KEY"
    device_id: "YOUR DEVICE ID"
 - platform: smartthings_soundbar
    name: voice_amplifier
    api_key: "YOUR API KEY"
    device_id: "YOUR DEVICE ID"
```

( You can't change the names of the switchs)
You can use !secret to avoid repeating API key and device id



## Getting API key and device id

Make sure your device is connected to yout SmartThings account.

Obtain an API key from https://account.smartthings.com/tokens

Go [here](https://graph-eu01-euwest1.api.smartthings.com/device/list) for your device id for each device. Click on the name of your device and the device id will be in the URL

> https://graph-eu01-euwest1.api.smartthings.com/device/show/XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXX

## Installation

### Manual

To install this integration manually you have to download [*smartthings_soundbar.zip*](https://github.com/PiotrMachowski/Home-Assistant-custom-components-SmartThings-Soundbar/releases/latest/download/smartthings_soundbar.zip) and extract its contents to `config/custom_components/smartthings_soundbar` directory:

```bash
mkdir -p custom_components/smartthings_soundbar
cd custom_components/smartthings_soundbar
wget https://github.com/thierry-rhone/Home-Assistant-custom-components-SmartThings-Soundbar/releases/latest/download/smartthings_soundbar.zip
unzip smartthings_soundbar.zip
rm smartthings_soundbar.zip
```

### Known problems

* If you have config validation issues after installing this component you have to follow these steps:
  * Install custom component
  * Restart Home Assistant
  * Add configuration
  * Restart Home Assistant again

## Supported devices

This integration was confirmed to work with following devices:

- Samsung HW-N950
- Samsung HW-Q800T
- Samsung HW-Q950T
- Samsung HW-Q990B
- Samsung HW-Q90R
- Samsung HW-Q80R
- Samsung HW-Q70R
- Samsung HW-S60T
- Samsung HW-S61T

<a href="https://www.buymeacoffee.com/PiotrMachowski" target="_blank"><img src="https://bmc-cdn.nyc3.digitaloceanspaces.com/BMC-button-images/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>
<a href="https://paypal.me/thierryBourbon" target="_blank"><img src="https://www.paypalobjects.com/webstatic/mktg/logo/pp_cc_mark_37x23.jpg" border="0" alt="PayPal Logo" style="height: auto !important;width: auto !important;"></a>

[releases_shield]: https://img.shields.io/github/release/thierry-rhone/Home-Assistant-custom-components-SmartThings-Soundbar.svg?style=popout
[releases]: https://github.com/thierry-rhone/Home-Assistant-custom-components-SmartThings-Soundbar/releases
[downloads_total_shield]: https://img.shields.io/github/downloads/thierry-rhone/Home-Assistant-custom-components-SmartThings-Soundbar/total

[paypal_me_shield]: https://img.shields.io/static/v1.svg?label=%20&message=PayPal.Me&logo=paypal
[paypal_me]: https://paypal.me/thierryBourbon

