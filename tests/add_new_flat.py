from browser_settings import driver, session_id
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from time import sleep


def add_flat(auth):
    driver.session_id = session_id
    driver.get(auth)
    try:
        print("-Добавление квартиры")
        driver.save_screenshot('add_flat_init.png')
        driver.find_element_by_id('createNewApartmentBtn').click()
        driver.save_screenshot('createNewApartmentBtn.png')
        print("--Заполняем Город, дом улица")
        driver.find_element_by_id('address').send_keys("улица Соборная, 3, Винница, Винницкая область, Украина", Keys.ARROW_DOWN, Keys.ENTER)
        driver.save_screenshot('address.png')
        driver.find_element_by_xpath('//*[@id="createNewApartmentForm"]/div[5]/input').click()
        sleep(6)
        driver.save_screenshot('finish.png')
        driver.close()
    except NoSuchElementException:
        driver.save_screenshot(f'NoSuchElementException{add_flat.__name__}.png')
        driver.close()
