from .environment import *
import sys
sys.path.append('.')
sys.path.append('../tests')

env = ''


def get_env():
    env = sys.argv[1]
    return env


def acceptance_test(env):

    if env == 'stage':
        auth = auth_page_stage
        main = main_page
        print(auth, main_page)
    elif env == 'prod':
        auth = auth_page
        main = main_page
        print(auth, main_page)


if __name__ == "__main__":
    acceptance_test(get_env())

# acceptance_test(envir)
# Registration
# Login
# Login & surf
