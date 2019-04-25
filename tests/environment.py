# here store a const and variables for global project
from random import choice
from string import ascii_lowercase
from .regression_test import env
# stage endpoints
auth_page_stage = 'https://auth.stage.clap.ua/login'
auth_page_prod = 'https://auth.clap.ua/login'
main_page_stage = 'https://ui.stage.clap.ua/'
main_page_prod = 'https://ui.clap.ua/'


def switcher():
    if env == 'stage':
        auth_page = auth_page_stage
        main_page = main_page_stage
        return auth_page, main_page
    elif env == 'prod':
        auth_page = auth_page_prod
        main_page = main_page_prod
        return auth_page, main_page


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


if __name__ == "__main__":
    pass