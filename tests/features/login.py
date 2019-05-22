import sys
import os
from tests.browser_settings import driver
sys.path.insert(0, 'E:/PythonProjects/CLAP---tests/')
from tests.environment import demo


def get_name():
    file = os.path.abspath('names.txt')
    with open(file, 'r') as names:
        name = names.read().splitlines()[-1][0:18]
        print(name)
        return name


def login(auth):

    driver.get(auth)
    print('---Login flow')
    # driver.find_element_by_id('loginUsername').send_keys(demo[0])
    print('-enter mail')
    driver.find_element_by_id('loginUsername').send_keys(get_name())
    print('-enter password')
    driver.find_element_by_id('loginPassword').send_keys(demo[1])
    print('-click login')
    driver.find_element_by_class_name('submit-btn').click()
    print('-make screenshot')
    driver.save_screenshot('1.png')

    driver.close()
