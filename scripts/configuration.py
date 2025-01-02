'''
Script used for configuring all essential packages.
'''

import os
from auxillary import log, select, choose, prepend_user_directory, prepend_script_directory, copy_files, link_files


def set_sddm_configuration():
    sddm_input = prepend_script_directory('../configuration/sddm')
    sddm_output = '/etc/sddm.conf.d'
    theme_input = prepend_script_directory('../configuration/sddm/sugar-dark')
    theme_output = '/usr/share/sddm/themes/sugar-dark'
    background_input = theme_input
    background_output = os.path.join(theme_output, 'Backgrounds')

    copy_files([
        {'input_path': sddm_input, 'output_path': sddm_output, 'file_name': 'sddm.conf'},
        {'input_path': theme_input, 'output_path': theme_output, 'file_name': 'theme.conf.user'},
        {'input_path': background_input, 'output_path': background_output, 'file_name': 'background.jpg'},
    ])


def set_xorg_configuration():
    input = prepend_script_directory('../configuration/xorg')
    configuration_output = '/etc/X11/xorg.conf.d'
    initialization_output = '/etc/X11/xinit/xinitrc.d'
    user_output = prepend_user_directory('')

    copy_files([
        {'input_path': input, 'output_path': configuration_output, 'file_name': '00-keyboard.conf'},
        {'input_path': input, 'output_path': configuration_output, 'file_name': '20-touchpad.conf'},
        {'input_path': input, 'output_path': initialization_output, 'file_name': '00-xinitrc.sh'},
    ])

    link_files([
        {'input_path': input, 'output_path': user_output, 'file_name': '.Xresources'},
        {'input_path': input, 'output_path': user_output, 'file_name': '.Xmodmap'},
    ])


def set_alacritty_configuration():
    input = prepend_script_directory('../configuration/alacritty')
    output = prepend_user_directory('.config/alacritty')

    link_files([
        {'input_path': input, 'output_path': output, 'file_name': 'alacritty.toml'},
    ])


def set_kitty_configuration():
    input = prepend_script_directory('../configuration/kitty')
    output = prepend_user_directory('.config/kitty')

    link_files([
        {'input_path': input, 'output_path': output, 'file_name': 'kitty.conf'},
    ])


def set_picom_configuration():
    input = prepend_script_directory('../configuration/picom')
    output = prepend_user_directory('.config/picom')

    link_files([
        {'input_path': input, 'output_path': output, 'file_name': 'picom.conf'},
    ])


def set_rofi_configuration():
    input = prepend_script_directory('../configuration/rofi')
    output = prepend_user_directory('.config/rofi')

    link_files([
        {'input_path': input, 'output_path': output, 'file_name': 'config.rasi'},
    ])


def set_readline_configuration():
    input = prepend_script_directory('../configuration/readline')
    output = prepend_user_directory('')

    link_files([
        {'input_path': input, 'output_path': output, 'file_name': '.inputrc'},
    ])


def set_bash_configuration():
    input = prepend_script_directory('../configuration/bash')
    output = prepend_user_directory('')

    link_files([
        {'input_path': input, 'output_path': output, 'file_name': '.bashrc'},
        {'input_path': input, 'output_path': output, 'file_name': '.bash-aliases'},
        {'input_path': input, 'output_path': output, 'file_name': '.bash-functions'},
    ])


def set_backlight_rule(rule_name):
    input = prepend_script_directory('../configuration/rules')
    output = '/etc/udev/rules.d'

    copy_files([
        {'input_path': input, 'output_path': output, 'file_name': rule_name},
    ])


def set_zsa_rule():
    input = prepend_script_directory('../configuration/rules')
    output = '/etc/udev/rules.d'

    copy_files([
        {'input_path': input, 'output_path': output, 'file_name': '50-zsa.rules'},
    ])


def set_nrf_rule():
    input = prepend_script_directory('../configuration/rules')
    output = '/etc/udev/rules.d'

    copy_files([
        {'input_path': input, 'output_path': output, 'file_name': '60-nrf.rules'},
        {'input_path': input, 'output_path': output, 'file_name': '61-nrf-blacklist.rules'},
    ])


def set_quartus_rule():
    input = prepend_script_directory('../configuration/rules')
    output = '/etc/udev/rules.d'

    copy_files([
        {'input_path': input, 'output_path': output, 'file_name': '65-quartus-usbblaster.rules'},
    ])


if selection := choose('Choose backlight rule to apply.', ['10-backlight.intel.rules', '10-backlight.acpi.rules']):
    log(f'Applying {selection} rule')
    set_backlight_rule(selection)

if select('Apply sddm configuration?'):
    log('Applying sddm configuration')
    set_sddm_configuration()

if select('Apply xorg configuration?'):
    log('Applying xorg configuration')
    set_xorg_configuration()

if select('Apply zsa rules?'):
    log('Applying zsa configuration')
    set_zsa_rule()

if select('Apply nrf rules?'):
    log('Applying nrf configuration')
    set_nrf_rule()

if select('Apply quartus rules?'):
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
