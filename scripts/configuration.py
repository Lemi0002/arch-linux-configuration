'''
Script used for configuring all essential packages. SUDO priviliges are required for some configurations.
If priviliges are not required SUDO must not be used.
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


def make_files_executable(files):
    for file in files:
        subprocess.run(['chmod', '+x', file])


def set_sddm_configuration(theme_name):
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
    configuration_output = '/etc/X11/xorg.conf.d'
    initialization_output = '/etc/X11/xinit/xinitrc.d'

    files = [
        {'input_path': input, 'output_path': configuration_output, 'file_name': '00-keyboard.conf'},
        {'input_path': input, 'output_path': configuration_output, 'file_name': '20-touchpad.conf'},
        {'input_path': input, 'output_path': initialization_output, 'file_name': '00-xinitrc.sh'},
        {'input_path': input, 'output_path': path_user, 'file_name': '.Xresources'},
        {'input_path': input, 'output_path': path_user, 'file_name': '.Xmodmap'},
    ]

    copy_files(files)
    make_files_executable([os.path.join(x['output_path'], x['file_name']) for x in files if x['file_name'].endswith('.sh')])


def set_alacritty_configuration():
    input = '../configuration/alacritty'
    output = os.path.join(path_user, '.config/alacritty')

    files = [
        {'input_path': input, 'output_path': output, 'file_name': 'alacritty.toml'},
    ]

    copy_files(files)


def set_kitty_configuration():
    input = '../configuration/kitty'
    output = os.path.join(path_user, '.config/kitty')

    files = [
        {'input_path': input, 'output_path': output, 'file_name': 'kitty.conf'},
    ]

    copy_files(files)


def set_picom_configuration():
    input = '../configuration/picom'
    output = os.path.join(path_user, '.config/picom')

    files = [
        {'input_path': input, 'output_path': output, 'file_name': 'picom.conf'},
    ]

    copy_files(files)


def set_rofi_configuration():
    input = '../configuration/rofi'
    output = os.path.join(path_user, '.config/rofi')

    files = [
        {'input_path': input, 'output_path': output, 'file_name': 'config.rasi'},
    ]

    copy_files(files)

def set_bash_configuration():
    input = '../configuration/bash'
    output = path_user

    files = [
        {'input_path': input, 'output_path': output, 'file_name': '.bashrc'},
        {'input_path': input, 'output_path': output, 'file_name': '.bash-aliases'},
    ]

    copy_files(files)


def set_backlight_rule(rule_name):
    input = '../configuration/rules'
    output = '/etc/udev/rules.d'

    files = [
        {'input_path': input, 'output_path': output, 'file_name': rule_name},
    ]

    copy_files(files)

def set_zsa_rule():
    input = '../configuration/rules'
    output = '/etc/udev/rules.d'

    files = [
        {'input_path': input, 'output_path': output, 'file_name': '50-zsa.rules'},
    ]

    copy_files(files)

def set_nrf_rule():
    input = '../configuration/rules'
    output = '/etc/udev/rules.d'

    files = [
        {'input_path': input, 'output_path': output, 'file_name': '60-nrf.rules'},
        {'input_path': input, 'output_path': output, 'file_name': '61-nrf-blacklist.rules'},
    ]

    copy_files(files)

if selection := choose('Choose sddm configuration to apply. SUDO is required.', ['sugar-candy', 'sugar-dark']):
    log(f'Applying sddm {selection} configuration')
    set_sddm_configuration(selection)

if selection := choose('Choose backlight rule to apply. SUDO is required.', ['10-backlight.intel.rules', '10-backlight.acpi.rules']):
    log(f'Applying {selection} rule')
    set_backlight_rule(selection)

if select('Apply xorg configuration? SUDO is required.'):
    log('Applying xorg configuration')
    set_xorg_configuration()

if select('Apply zsa rules? SUDO is required.'):
    log('Applying zsa configuration')
    set_zsa_rule()

if select('Apply nrf rules? SUDO is required.'):
    log('Applying nrf configuration')
    set_nrf_rule()

if select('Apply alacritty configuration?'):
    log('Applying alacritty configuration')
    set_alacritty_configuration()

if select('Apply kitty configuration?'):
    log('Applying kitty configuration')
    set_kitty_configuration()

if select('Apply picom configuration?'):
    log('Applying picom configuration')
    set_picom_configuration()

if select('Apply rofi configuration?'):
    log('Applying rofi configuration')
    set_rofi_configuration()

if select('Apply bash configuration?'):
    log('Applying bash configuration')
    set_bash_configuration()
