import os
import subprocess


def log(*values):
    print('>>', *values)


def select(text):
    log(text, '[y/n]')
    return True if input() == 'y' else False


def choose(text, values, force_selection=False):
    log(text)

    for i, value in enumerate(values):
        log(f'{i:2}: {value}')

    if not force_selection:
        log(' n: none')

    try:
        input_value = int(input())
        return values[input_value]
    except:
        log('Selection discarded')
        if force_selection:
            return values[0]
        else:
            return False


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
            if not select(f'Continue to override file as "{file_output}" already exists?'):
                log(f'Skipping to override file as "{file_output}" already exists')
                return

        command = ['cp', file_input, file_output]
        if not os.access(output_path, os.W_OK):
            command.insert(0, 'sudo')

        subprocess.run(command)


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
            if select(f'Continue to remove file as "{file_output}" already exists?'):
                remove_file(file_output)
            else:
                log(f'Skipping to link file as "{file_output}" already exists')
                return

        command = ['ln', '-s', file_input, file_name]
        if not os.access(output_path, os.W_OK):
            command.insert(0, 'sudo')

        subprocess.run(command, cwd=output_path)


def remove_file(file):
    command = ['rm', file]
    if os.path.islink(file):
        if not os.access(os.path.dirname(file), os.W_OK):
            command.insert(0, 'sudo')
    else:
        if not os.access(file, os.W_OK):
            command.insert(0, 'sudo')

    subprocess.run(command)
