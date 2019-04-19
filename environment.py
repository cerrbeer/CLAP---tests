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
demo_user = 'demo@clap.ua'
demo_pass = '111111'

# Using random names for registration
registration_user = f'{randomize_name()}@testmail.com'
registration_pass = '111111'
