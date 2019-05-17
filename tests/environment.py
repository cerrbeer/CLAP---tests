# here store a const and variables for global project
from random import choice
from string import ascii_lowercase
from datetime import datetime

# stage endpoints
auth_page_stage = 'https://auth.stage.clap.ua/login'
auth_page_prod = 'https://auth.clap.ua/login'
main_page_stage = 'https://ui.stage.clap.ua/'
main_page_prod = 'https://ui.clap.ua/'


def randomize_name():
    name = ''.join(choice(ascii_lowercase) for i in range(5))
    names = open('names.txt', 'a')
    login = f'{name}@testmail.com'
    names.write(login + ' ' + f'{datetime.now()}' + '\n')
    names.close()
    return login


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
    'заглушка',
    # f'{randomize_name()}@testmail.com',
    '0630000745',
    '111111'
]



# if __name__ == "__main__":
#     pass
