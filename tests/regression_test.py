from environment import auth_page_stage, auth_page_prod, main_page_stage, main_page_prod
import sys
sys.path.insert(0, 'E:/PythonProjects/CLAP---tests/')

from tests.features.registration import registration
from tests.features.login import login
from tests.features.add_new_flat import add_flat


debug = True
sys.path.insert(0, 'E:/PythonProjects/CLAP---tests/')

sys.path.append('.')
sys.path.append('/tests')
sys.path.append('/tests/features')


def main():
    try:
        argument = sys.argv[1]

        if argument == 'stage':
            registration(auth_page_stage)
            login(auth_page_stage)
            add_flat('https://ui.stage.clap.ua/')

        elif argument == 'prod':
            registration(auth_page_prod)
            login(auth_page_prod)
            add_flat('https://ui.stage.clap.ua/')

        elif argument == '-help':
            output_data = \
                  'type -help               -for list all arguments' + '\n' \
                  'stage                    -argument for use staging endpoints' + '\n' \
                  'prod                     -argument for use production endpoints'
            print(output_data)
    except IndexError:
        print('use -help argument to get lis of commands')


main()
