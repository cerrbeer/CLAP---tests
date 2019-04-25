from environment import *


def acceptance_test(env):

    if env == 'stage':
        auth = auth_page_stage
        main_page = main_page_stage
        print(auth, main_page)
    elif env == 'prod':
        auth = auth_page_prod
        main_page = main_page_prod
        print(auth, main_page)


if __name__ == "__main__":
    acceptance_test(input(':'))

# acceptance_test(envir)
# Registration
# Login
# Login & surf
