__config = {
    'name': 'PassMngr',
    'version': {
        'stage': 'Pre-alpha',
        'number': '0.01'
    },
    'license': 'MIT',
    'author': {
        'username': 'Poliweglan',
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


def get_license():
    return __config['license']


def get_author_username():
    return __config['author']['username']


def get_author_git():
    return __config['author']['git']