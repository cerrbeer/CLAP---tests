from environment import auth_page_stage, auth_page_prod, main_page_stage, main_page_prod
import sys
sys.path.insert(0, 'E:/PythonProjects/CLAP---tests/')
from tests.features.registration import registration
from tests.features.login import login
debug = True

sys.path.append('.')
sys.path.append('/tests')
sys.path.append('/tests/features')


def get_argument():
    auth = sys.argv[1]
    # auth = 'stage'
    print(auth)
    return auth


arg = get_argument()


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


registration(main(arg)[0])
login('https://ui.stage.clap.ua/')
# registration(main(sys.argv[1])[0])
# login(main(sys.argv[1])[0])
# registration(main('stage'))
# main(sys.argv[1])
# main('stage')


# Registration
# Login
# Login & surf
