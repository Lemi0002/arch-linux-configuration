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
