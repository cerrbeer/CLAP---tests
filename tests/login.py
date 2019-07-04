import sys
import os
from browser_settings import driver, session_id
from selenium.common.exceptions import NoSuchElementException
from environment import demo
sys.path.insert(0, 'E:/PythonProjects/CLAP---tests/')


def get_name():
    file = os.path.abspath('names.txt')
    with open(file, 'r') as names:
        name = names.read().splitlines()[-1][0:18]
        print(name)
        return name


def login(auth):
    driver.session_id = session_id
    driver.get(auth)
    try:
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
    except NoSuchElementException:
        driver.save_screenshot(f'NoSuchElementException{login.__name__}.png')
        driver.close()


