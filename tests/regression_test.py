from environment import *
import sys
sys.path.insert(0, 'E:/PythonProjects/CLAP---tests/')
from tests.features.registration import registration
debug = True

sys.path.append('.')
sys.path.append('/tests')
sys.path.append('/tests/features')

envs = ''


def main(env):

    if env == 'stage':
        auth = auth_page_stage
        ui = main_page_stage

        return auth, ui
    elif env == 'prod':
        auth = auth_page_prod
        ui = main_page_prod

        return auth, ui
    elif env == '-help':
        output_data = \
              'type -help               -for list all arguments' + '\n' \
              'stage                    -argument for use staging endpoints' + '\n' \
              'prod                     -argument for use production endpoints'
        print(output_data)
    elif env == '':
        output_data = 'use -help argument to get lis of commands'
        print(output_data)


registration(main(sys.argv[1])[0])
# main(sys.argv[1])
# main('stage')


# Registration
# Login
# Login & surf
