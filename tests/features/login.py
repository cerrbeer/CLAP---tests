from browser_settings import driver
from environment import auth_page, demo


def login():

    driver.get(auth_page)
    driver.find_element_by_id('loginUsername').send_keys(demo[0])
    driver.find_element_by_id('loginPassword').send_keys(demo[1])
    driver.find_element_by_class_name('submit-btn').click()
    driver.save_screenshot('1.png')

    driver.close()


login()
