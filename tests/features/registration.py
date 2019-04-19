from browser_settings import driver
from environment import auth_page, demo, reg


def registration():
    driver.get(auth_page)
    driver.find_element_by_class_name(' ???').click()
    driver.find_element_by_id('registrationFirstName').send_keys(reg[0])
    driver.find_element_by_id('registrationLastName').send_keys(reg[1])
    driver.find_element_by_id('registrationPatronymic').send_keys(reg[2])
    driver.find_element_by_class_name('nextBtn').click()
    driver.find_element_by_id('registrationUserName').send_keys(reg[3])
    driver.find_element_by_id('registrationPhoneNumber').send_keys(reg[4])
    driver.find_element_by_class_name('nextBtn').click()
    driver.find_element_by_id('registrationPassword').send_keys(reg[5])
    driver.find_element_by_id('registrationRePassword').send_keys(reg[5])
    driver.find_element_by_class_name('doneBtn').click()
    driver.save_screenshot('1.png')

    driver.close()


registration()
