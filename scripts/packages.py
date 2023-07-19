'''
Script used for installing all essential packages and enabling certain services.
'''

import subprocess

command = ['sudo', 'pacman', '-Su']
packages = [
    'alacritty',
    'awesome',
    'cmake',
    'git',
    'github-cli',
    'gnome',
    'ninja',
    'neovim',
    'networkmanager',
    'npm',
    'python-pip',
    'ripgrep',
    'rust',
    'sddm',
    'unzip',
    'wget',
    'wl-clipboard',
    'xclip',
    'xorg',
    'yarn',
]
packages_bluetooth = [
    'bluez',
    'bluez-utils',
    'pulseaudio-alsa',
    'pulseaudio-bluetooth',
]
packages_wifi = [
    'iwd',
]


def log(*values):
    print('>>', *values)


def select(value):
    log(value, '[y/n]')
    return True if input() == 'y' else False


if select('Install packages?'):
    log('Installing packages')
    subprocess.run([*command, *packages])

if select('Install bluetooth packages?'):
    log('Installing bluetooth packages')
    subprocess.run([*command, *packages_bluetooth])

if select('Install wifi packages?'):
    log('Installing wifi packages')
    subprocess.run([*command, *packages_wifi])

if select('Install yay?'):
    log('Installing yay')
    subprocess.run(['git', 'clone', 'https://aur.archlinux.org/yay.git'])
    subprocess.run(['makepkg', '-si'], cwd='yay')
    subprocess.run(['rm', '-drf', 'yay'])

if select('Bluetooth: Enable bluetooth.service daemon?'):
    log('Bluetooth: Enabling bluetooth.service daemon')
    subprocess.run(['sudo', 'systemctl', '--now',
                   'enable', 'bluetooth.service'])

if select('Wifi: Disable wpa_supplicant.service and enable iwd.service daemon?'):
    log('Wifi: Disabling wpa_supplicant.service daemon')
    subprocess.run(['sudo', 'systemctl', '--now',
                   'disable', 'wpa_supplicant.service'])
    log('Wifi: Enabling iwd.service daemon')
    subprocess.run(['sudo', 'systemctl', '--now', 'enable', 'iwd.service'])
