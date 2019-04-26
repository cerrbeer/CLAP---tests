from environment import *
import sys
sys.path.append('.')
sys.path.append('../tests')

envs = ''


def main(env):

    if env == 'stage':
        auth = auth_page_stage
        ui = main_page_stage
        print(auth, ui)
        return auth, ui
    elif env == 'prod':
        auth = auth_page_prod
        ui = main_page_prod
        print(auth, ui)
        return auth, ui


main(sys.argv)

# acceptance_test(envir)
# Registration
# Login
# Login & surf
