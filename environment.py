# here store a const and variables for global project
from random import choice
from string import ascii_lowercase

# stage endpoints
auth_page = 'https://auth.stage.clap.ua/login'
main_page = 'https://ui.stage.clap.ua/'


def randomize_name():
    name = ''.join(choice(ascii_lowercase) for i in range(5))
    return name


# USERS
demo = [
    'demo@clap.ua',
    '111111'
]

# Using random names for registration
reg = [
    'Тестовый',
    'Аккаунт',
    'Аккаунтович',
    f'{randomize_name()}@testmail.com',
    '0630000745',
    '111111',

]
