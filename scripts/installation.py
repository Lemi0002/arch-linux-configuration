'''
Script used for installing all essential packages and enabling certain services.
'''

import subprocess
from auxillary import log, select

command = ['sudo', 'pacman', '-Su']
command_aur = ['yay', '-Su']
command_snap = ['sudo', 'snap', 'install']
packages = [
    'alacritty',
    'awesome',
    'cmake',
    'firefox',
    'gimp',
    'git',
    'github-cli',
    'gnome',
    'go',
    'htop',
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
    'tree',
    'ttf-firacode-nerd',
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
packages_snap = [
    'nordpass',
]
packages_wifi = [
    'iwd',
    'dhcpcd',
]


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

if select('Install snapd?'):
    log('Installing snapd')
    subprocess.run(['git', 'clone', 'https://aur.archlinux.org/snapd.git'])
    subprocess.run(['makepkg', '-si'], cwd='snapd')
    subprocess.run(['rm', '-drf', 'snapd'])
    subprocess.run(['sudo', 'systemctl', 'enable', '--now', 'snapd.socket'])
    subprocess.run(['sudo', 'ln', '-s', '/var/lib/snapd/snap', '/snap'])
    subprocess.run(['sudo', 'systemctl', 'enable', '--now', 'snapd.apparmor'])

if select('Install snap packages?'):
    log('Installing snap packages?')
    subprocess.run([*command_snap, *packages_snap])

if select('Bluetooth: Enable bluetooth.service daemon?'):
    log('Bluetooth: Enabling bluetooth.service daemon')
    subprocess.run(['sudo', 'systemctl', '--now',
                   'enable', 'bluetooth.service'])

if select('Wifi: Enable iwd.service daemon?'):
    log('Wifi: Enabling iwd.service daemon')
    subprocess.run(['sudo', 'systemctl', '--now', 'enable', 'iwd.service'])

if select('Wifi: Enable dhcpcd.service for all network interfaces?'):
    log('Wifi: Enabling dhcpcd.service for all network interfaces')
    subprocess.run(['sudo', 'systemctl', '--now', 'enable', 'dhcpcd.service'])
