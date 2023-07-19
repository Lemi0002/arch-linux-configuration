# Arch Linux configuration
This repository contains scripts and information on how to configure Arch Linux.
As a general guide the [Arch Linux wiki](https://archlinux.org) shall be consulted.

# Preparations
Before any of these scripts can be run, follow the [installation guide](https://archlinux.org/title/installation_guide) and make sure the `git` package is installed.
Furthermore, a local user account should be set up according to [general recommendations](https://archlinux.org/title/General_recommendations).

# Bluetooth
If the host has Bluetooth capabilities the provided packages can be installed.
See [bluetooth](https://archlinux.org/title/Bluetooth) for more information.
For some reason it might not be possible to connect a Bluetooth headset.
In that case follow [bluetooth headset](https://archlinux.org/title/bluetooth_headset).

# Wifi
By using `wpa_supplicant` one might experience throttled download and upload speeds.
This might be fixed by using `iwd` instead.
In that case follow [iwd](https://wiki.archlinux.org/title/iwd).
