__config = {
    'name': 'PassMngr',
    'version': {
        'stage': 'Pre-alpha',
        'number': '0.01'
    },
    'license': 'MIT',
    'author': {
        'name': 'Poliweglan',
        'git': 'https://github.com/Poliweglan'
    }
}


def get_config():
    print(__config)


def get_program_name():
    return __config['name']


def get_version_stage():
    return __config['version']['stage']


def get_version_number():
    return __config['version']['number']
