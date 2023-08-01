'''
Script used for installing all essential packages and enabling certain services.
'''

import subprocess

command = ['sudo', 'pacman', '-Su']
command_aur = ['yay', '-Su']
packages = [
    'alacritty',
    'awesome',
    'cmake',
    'gimp',
    'git',
    'github-cli',
    'gnome',
    'okular',
    'ninja',
    'neovim',
    'networkmanager',
    'npm',
    'python-pip',
    'ripgrep',
    'rust',
    'sddm',
    'texlive',
    'texlive-langgerman',
    'unzip',
    'wget',
    'wl-clipboard',
    'xclip',
    'xorg',
    'yarn',
]
packages_aur = [
    'google-chrome',
    'sddm-sugar-candy',
    'sddm-sugar-dark',
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

if select('Install aur packages?'):
    log('Installing aur packages')
    subprocess.run([*command_aur, *packages_aur])

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

if select('Display manager: Set default theme to sugar-dark?'):
    log('Display manager: Setting default theme to sugar-dark')
