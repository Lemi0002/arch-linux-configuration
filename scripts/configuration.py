'''
Script used for configuring all essential packages. Must be run with root privileges.
'''

import os
import subprocess
from auxillary import log, select, choose


user = os.getenv('SUDO_USER')
if user is None:
    user = os.getenv('USER', 'root')

path_user = os.path.join('/home', user)


def copy_files(files):
    for file in files:
        input_path = file['input_path']
        output_path = file['output_path']
        file_name = file['file_name']

        if not os.path.isdir(output_path):
            os.makedirs(output_path)

        subprocess.run(['cp', file_name, os.path.join(output_path, file_name)],
                    cwd=os.path.join(os.path.dirname(__file__), input_path))

def edit_file(file_name, text, key):
    lines = None

    with open(file_name, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if key != None and key in line:
            lines[i] = ''.join([key, text])

    with open(file_name, 'w') as file:
        file.writelines(lines)


def set_sddm_configuration(theme_name):
    log(f'Applying sddm {theme_name} configuration')
    sddm_input = '../configuration/sddm'
    sddm_output = '/etc/sddm.conf.d'
    theme_input = os.path.join('../configuration/sddm', theme_name)
    theme_output = os.path.join('/usr/share/sddm/themes', theme_name)
    background_input = theme_input
    background_output = os.path.join(theme_output, 'Backgrounds')

    files = [
        {'input_path': sddm_input, 'output_path': sddm_output, 'file_name': 'sddm.conf'},
        {'input_path': theme_input, 'output_path': theme_output, 'file_name': 'theme.conf.user'},
        {'input_path': background_input, 'output_path': background_output, 'file_name': 'background.jpg'},
    ]

    copy_files(files)
    file = os.path.join(files[0]['output_path'], files[0]['file_name'])
    edit_file(file, theme_name, 'Current=')


def set_xorg_configuration():
    input = '../configuration/xorg'
    output = '/etc/X11/xorg.conf.d'

    files = [
        {'input_path': input, 'output_path': output, 'file_name': '00-keyboard.conf'},
        {'input_path': input, 'output_path': output, 'file_name': '20-touchpad.conf'},
        {'input_path': input, 'output_path': path_user, 'file_name': '.Xresources'},
    ]

    copy_files(files)


def set_alacritty_configuration():
    input = '../configuration/alacritty'
    output = os.path.join(path_user, '.config/alacritty')

    files = [
        {'input_path': input, 'output_path': output, 'file_name': 'alacritty.yml'},
    ]

    copy_files(files)


def set_kitty_configuration():
    input = '../configuration/kitty'
    output = os.path.join(path_user, '.config/kitty')

    files = [
        {'input_path': input, 'output_path': output, 'file_name': 'kitty.conf'},
    ]

    copy_files(files)


def set_awesome_configuration():
    input = '../configuration/awesome'
    output = os.path.join(path_user, '.config/awesome')

    files = [
        {'input_path': input, 'output_path': output, 'file_name': 'rc.lua'},
    ]

    copy_files(files)

def set_backlight_rule(rule_name):
    input = '../configuration/rules'
    output = '/etc/udev/rules.d'

    files = [
        {'input_path': input, 'output_path': output, 'file_name': rule_name},
    ]

    copy_files(files)

if selection := choose('Choose sddm configuration to apply', ['sugar-candy', 'sugar-dark']):
    set_sddm_configuration(selection)

if select('Apply xorg configuration?'):
    log('Applying xord configuration')
    set_xorg_configuration()

if select('Apply alacritty configuration?'):
    log('Applying alacritty configuration')
    set_alacritty_configuration()

if select('Apply kitty configuration?'):
    log('Applying kitty configuration')
    set_kitty_configuration()

if select('Apply awesome configuration?'):
    log('Applying awesome configuration')
    set_awesome_configuration()

if selection := choose('Choose backlight rule to apply', ['10-backlight.intel.rules', '10-backlight.acpi.rules']):
    set_backlight_rule(selection)
