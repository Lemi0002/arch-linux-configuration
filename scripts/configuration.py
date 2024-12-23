'''
Script used for configuring all essential packages.
'''

import os
import subprocess
from auxillary import log, select, choose


def prepend_user_directory(path):
    user = os.getenv('SUDO_USER')
    if user is None:
        user = os.getenv('USER', 'root')

    user_path = os.path.join('/home', user)
    return os.path.join(user_path, path)


def prepend_script_directory(path):
    return os.path.join(os.path.dirname(__file__), path)


def copy_files(files):
    for file in files:
        input_path = file['input_path']
        output_path = file['output_path']
        file_name = file['file_name']

        file_input = os.path.join(input_path, file_name)
        file_output = os.path.join(output_path, file_name)

        if not os.path.isabs(input_path):
            log(f'Skipping to link file as "{input_path}" is not an absolute input path')
            return

        if not os.path.isabs(output_path):
            log(f'Skipping to link file as "{output_path}" is not an absolute output path')
            return

        if not os.path.isdir(output_path):
            os.makedirs(output_path)

        if os.path.isfile(file_output):
            log(f'Overriding file "{file_output}" as it already exists')

        subprocess.run(['cp', file_input, file_output])


def link_files(files):
    for file in files:
        input_path = file['input_path']
        output_path = file['output_path']
        file_name = file['file_name']

        file_input = os.path.join(input_path, file_name)
        file_output = os.path.join(output_path, file_name)

        if not os.path.isabs(input_path):
            log(f'Skipping to link file as "{input_path}" is not an absolute input path')
            return

        if not os.path.isabs(output_path):
            log(f'Skipping to link file as "{output_path}" is not an absolute output path')
            return

        if not os.path.isdir(output_path):
            os.makedirs(output_path)

        if os.path.isfile(file_output):
            log(f'Skipping to link file as "{file_output}" already exists')
            return

        subprocess.run(['ln', '-s', file_input, file_name], cwd=output_path)


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


def set_sddm_configuration():
    sddm_input = prepend_script_directory('../configuration/sddm')
    sddm_output = '/etc/sddm.conf.d'
    theme_input = prepend_script_directory('../configuration/sddm/sugar-dark')
    theme_output = '/usr/share/sddm/themes/sugar-dark'
    background_input = theme_input
    background_output = os.path.join(theme_output, 'Backgrounds')

    files = [
        {'input_path': sddm_input, 'output_path': sddm_output, 'file_name': 'sddm.conf'},
        {'input_path': theme_input, 'output_path': theme_output, 'file_name': 'theme.conf.user'},
        {'input_path': background_input, 'output_path': background_output, 'file_name': 'background.jpg'},
    ]

    link_files(files)


def set_xorg_configuration():
    input = prepend_script_directory('../configuration/xorg')
    configuration_output = '/etc/X11/xorg.conf.d'
    initialization_output = '/etc/X11/xinit/xinitrc.d'
    user_output = prepend_user_directory('')

    files = [
        {'input_path': input, 'output_path': configuration_output, 'file_name': '00-keyboard.conf'},
        {'input_path': input, 'output_path': configuration_output, 'file_name': '20-touchpad.conf'},
        {'input_path': input, 'output_path': initialization_output, 'file_name': '00-xinitrc.sh'},
        {'input_path': input, 'output_path': user_output, 'file_name': '.Xresources'},
        {'input_path': input, 'output_path': user_output, 'file_name': '.Xmodmap'},
    ]

    link_files(files)
    make_files_executable([os.path.join(x['output_path'], x['file_name']) for x in files if x['file_name'].endswith('.sh')])


def set_alacritty_configuration():
    input = prepend_script_directory('../configuration/alacritty')
    output = prepend_user_directory('.config/alacritty')

    files = [
        {'input_path': input, 'output_path': output, 'file_name': 'alacritty.toml'},
    ]

    link_files(files)


def set_kitty_configuration():
    input = prepend_script_directory('../configuration/kitty')
    output = prepend_user_directory('.config/kitty')

    files = [
        {'input_path': input, 'output_path': output, 'file_name': 'kitty.conf'},
    ]

    link_files(files)


def set_picom_configuration():
    input = prepend_script_directory('../configuration/picom')
    output = prepend_user_directory('.config/picom')

    files = [
        {'input_path': input, 'output_path': output, 'file_name': 'picom.conf'},
    ]

    link_files(files)


def set_rofi_configuration():
    input = prepend_script_directory('../configuration/rofi')
    output = prepend_user_directory('.config/rofi')

    files = [
        {'input_path': input, 'output_path': output, 'file_name': 'config.rasi'},
    ]

    link_files(files)


def set_readline_configuration():
    input = prepend_script_directory('../configuration/readline')
    output = prepend_user_directory('')

    files = [
        {'input_path': input, 'output_path': output, 'file_name': '.inputrc'},
    ]

    link_files(files)


def set_bash_configuration():
    input = prepend_script_directory('../configuration/bash')
    output = prepend_user_directory('')

    files = [
        {'input_path': input, 'output_path': output, 'file_name': '.bashrc'},
        {'input_path': input, 'output_path': output, 'file_name': '.bash-aliases'},
        {'input_path': input, 'output_path': output, 'file_name': '.bash-functions'},
    ]

    link_files(files)


def set_backlight_rule(rule_name):
    input = prepend_script_directory('../configuration/rules')
    output = '/etc/udev/rules.d'

    files = [
        {'input_path': input, 'output_path': output, 'file_name': rule_name},
    ]

    link_files(files)


def set_zsa_rule():
    input = prepend_script_directory('../configuration/rules')
    output = '/etc/udev/rules.d'

    files = [
        {'input_path': input, 'output_path': output, 'file_name': '50-zsa.rules'},
    ]

    link_files(files)


def set_nrf_rule():
    input = prepend_script_directory('../configuration/rules')
    output = '/etc/udev/rules.d'

    files = [
        {'input_path': input, 'output_path': output, 'file_name': '60-nrf.rules'},
        {'input_path': input, 'output_path': output, 'file_name': '61-nrf-blacklist.rules'},
    ]

    link_files(files)


def set_quartus_rule():
    input = prepend_script_directory('../configuration/rules')
    output = '/etc/udev/rules.d'

    files = [
        {'input_path': input, 'output_path': output, 'file_name': '65-quartus-usbblaster.rules'},
    ]

    link_files(files)


if selection := choose('Choose backlight rule to apply. SUDO is required.', ['10-backlight.intel.rules', '10-backlight.acpi.rules']):
    log(f'Applying {selection} rule')
    set_backlight_rule(selection)

if select('Apply sddm configuration?'):
    log('Applying sddm configuration')
    set_sddm_configuration()

if select('Apply xorg configuration? SUDO is required.'):
    log('Applying xorg configuration')
    set_xorg_configuration()

if select('Apply zsa rules? SUDO is required.'):
    log('Applying zsa configuration')
    set_zsa_rule()

if select('Apply nrf rules? SUDO is required.'):
    log('Applying nrf configuration')
    set_nrf_rule()

if select('Apply quartus rules? SUDO is required.'):
    log('Applying quartus configuration')
    set_quartus_rule()

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

if select('Apply readline configuration?'):
    log('Applying readline configuration')
    set_readline_configuration()
