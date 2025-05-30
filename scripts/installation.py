'''
Script used for installing all essential packages and enabling certain services.
'''

import os
import subprocess
from auxillary import log, select

command = ['sudo', 'pacman', '-Su']
command_aur = ['yay', '-Su']
command_snap = ['sudo', 'snap', 'install']
packages = [
    'alacritty',
    'awesome',
    'cmake',
    'docker',
    'docker-compose',
    'dosfstools',
    'fcitx5-configtool',
    'fcitx5-im',
    'fcitx5-mozc',
    'firefox',
    'freerdp',
    'fzf',
    'gimp',
    'git',
    'github-cli',
    'go',
    'htop',
    'inkscape',
    'intel-gpu-tools',
    'intel-media-driver',
    'keepassxc',
    'kitty',
    'libreoffice',
    'libxcrypt-compat',
    'man-pages',
    'neofetch',
    'neovim',
    'networkmanager',
    'ninja',
    'noto-fonts',
    'noto-fonts-cjk',
    'noto-fonts-emoji',
    'noto-fonts-extra',
    'npm',
    'obs-studio',
    'okular',
    'openconnect',
    'openssh',
    'picom',
    'playerctl',
    'pulseaudio',
    'pulseaudio-alsa',
    'python-dbus',
    'python-pip',
    'qemu-base',
    'remmina',
    'ripgrep',
    'rofi',
    'rustup',
    'samba',
    'sddm',
    'strace',
    'tectonic',
    'texlive',
    'texlive-langgerman',
    'tigervnc',
    'tree',
    'tree-sitter-cli',
    'ttf-firacode-nerd',
    'ttf-indic-otf',
    'unzip',
    'vimiv',
    'vlc',
    'wget',
    'wl-clipboard',
    'xclip',
    'xorg',
    'yarn',
    'yazi',
    'zip',
]
packages_aur = [
    'google-chrome',
    'gowall',
    'gtkterm',
    'sddm-sugar-dark',
    'synology-drive',
    'ttf-google-thai',
    'ttf-khmer',
    'ttf-lao',
    'ttf-ms-fonts',
    'ttf-sil-padauk',
    'zsa-keymapp-bin',
]
packages_bluetooth = [
    'bluez',
    'bluez-utils',
    'pulseaudio-bluetooth',
]
packages_snap = [
]
repositories = [
    {'url': 'https://github.com/Lemi0002/awesomewm-configuration', 'path': '~/.config/awesome'},
    {'url': 'https://github.com/Lemi0002/nvim-configuration', 'path': '~/.config/nvim'},
    {'url': 'https://github.com/Lemi0002/yazi-configuration', 'path': '~/.config/yazi'},
    {'url': 'https://gitlab.com/dwt1/wallpapers', 'path': '~/version-control/wallpapers-dwt'},
]


if select('Install packages?'):
    log('Installing packages')
    subprocess.run([*command, *packages])

if select('Install bluetooth packages?'):
    log('Installing bluetooth packages')
    subprocess.run([*command, *packages_bluetooth])

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

if select('Install snap packages? Requires reboot after snapd was installed'):
    log('Installing snap packages')
    subprocess.run([*command_snap, *packages_snap])

if select('Install repositories?'):
    log('Installing repositories')

    for repository in repositories:
        subprocess.run(['git', 'clone', repository['url'], os.path.expanduser(repository['path'])])

if select('Bluetooth: Enable bluetooth.service daemon?'):
    log('Bluetooth: Enabling bluetooth.service daemon')
    subprocess.run(['sudo', 'systemctl', '--now',
                   'enable', 'bluetooth.service'])
