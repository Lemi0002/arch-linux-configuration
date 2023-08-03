'''
Script used for configuring all essential packages. Must be run with root privileges.
'''

import os
import subprocess
from auxillary import log, select, choose
# import screeninfo


def copy_files(files):
    for file in files:
        if not os.path.isdir(file['output_path']):
            os.makedirs(file['output_path'])

        subprocess.run(['cp', file['file_name'], os.path.join(file['output_path'], file['file_name'])],
                    cwd=os.path.join(os.path.dirname(__file__), file['input_path']))


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


def set_xorg_configuration():
    input = '../configuration/xorg'
    output = '/etc/X11/xorg.conf.d'

    files = [
        {'input_path': input, 'output_path': output, 'file_name': '00-keyboard.conf'},
        {'input_path': input, 'output_path': output, 'file_name': '20-touchpad.conf'},
    ]

    copy_files(files)


if selection := choose('Choose sddm configuration to apply', ['sugar-candy', 'sugar-dark']):
    set_sddm_configuration(selection)

if select('Apply xorg configuration?'):
    log('Applying xord configuration')
    set_xorg_configuration()
