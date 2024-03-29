import sys
sys.path.insert(0, 'E:/PythonProjects/CLAP---tests/')
from tests.browser_settings import driver
from tests.environment import reg, randomize_name
from selenium.common.exceptions import NoSuchElementException


def registration(auth):
    print(auth)
    driver.get(auth)
    try:
        print('Нажимаем кнопку Регистрация')
        driver.find_element_by_css_selector('#loginForm > div.uk-form-row.space-between > span').click()
        print('Заполняем Фамилию')
        driver.find_element_by_id('registrationFirstName').send_keys(reg[0])
        print('Заполняем Имя')
        driver.find_element_by_id('registrationLastName').send_keys(reg[1])
        print('Заполняем Отчество')
        driver.find_element_by_id('registrationPatronymic').send_keys(reg[2])
        print('Нажимаем Next')
        driver.find_element_by_id('nextBtn').click()
        print('Заполняем Email')
        # driver.find_element_by_id('registrationUserName').send_keys(reg[3])
        driver.find_element_by_id('registrationUserName').send_keys(randomize_name())
        print('Заполняем Phone number')
        driver.find_element_by_id('registrationPhoneNumber').send_keys(reg[4])
        print('Нажимаем Next')
        driver.find_element_by_id('nextBtn').click()
        print('Enter password')
        driver.find_element_by_id('registrationPassword').send_keys(reg[5])
        print('Repeat password')
        driver.find_element_by_id('registrationRePassword').send_keys(reg[5])
        print('Нажимаем Complete')
        driver.find_element_by_id('doneBtn').click()
        # driver.save_screenshot('1.png')
    except NoSuchElementException:
        driver.save_screenshot(f'NoSuchElementException{registration.__name__}.png')
        driver.close()

    # driver.close()


# registration('https://auth.clap.ua/login')
