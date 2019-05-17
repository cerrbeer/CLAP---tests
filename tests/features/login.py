import sys
from tests.browser_settings import driver
sys.path.insert(0, 'E:/PythonProjects/CLAP---tests/')
from tests.environment import demo


def get_name():
    with open('\\tests\\names.txt', 'r') as names:
        name = names.read().splitlines()[-1][0:18]
        print(name)
        return name


def login(auth):

    driver.get(auth)
    # driver.find_element_by_id('loginUsername').send_keys(demo[0])
    driver.find_element_by_id('loginUsername').send_keys(get_name())
    driver.find_element_by_id('loginPassword').send_keys(demo[1])
    driver.find_element_by_class_name('submit-btn').click()
    driver.save_screenshot('1.png')

    driver.close()

