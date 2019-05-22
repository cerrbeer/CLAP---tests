from tests.browser_settings import driver


def add_flat(auth):

    driver.get(auth)
    print("-Добавление квартиры")
    driver.find_element_by_id('createNewApartmentBtn').click()
    print("--Заполняем Город, дом улица")
    driver.find_element_by_id('address').send_keys("улица Соборная, 24, Винница, Винницкая область, Украина")

