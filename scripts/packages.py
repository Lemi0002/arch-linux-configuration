import subprocess

command = ['sudo', 'pacman', '-Su']
packages = [
    'awesome',
    'cmake',
    'gnome',
    'ninja',
    'npm',
    'python-pip',
    'ripgrep',
    'rust',
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

if select('Enable bluetooth.service deamon?'):
    log('Enabling bluetooth.service deamon')
    subprocess.run(['sudo', 'systemctl', '--now',
                   'enable', 'bluetooth.service'])
