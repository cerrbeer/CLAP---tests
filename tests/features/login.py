from tests.browser_settings import driver
from tests.environment import reg, demo


def login(auth):

    driver.get(auth)
    driver.find_element_by_id('loginUsername').send_keys(demo[0])
    driver.find_element_by_id('loginPassword').send_keys(demo[1])
    driver.find_element_by_class_name('submit-btn').click()
    driver.save_screenshot('1.png')

    driver.close()
