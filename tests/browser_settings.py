from selenium import webdriver


CHROME_VERSION = '72'

driver = webdriver.Chrome(f'./chromedriver{CHROME_VERSION}.exe')
# driver = webdriver.Remote(
#     command_executor='http://127.0.0.1:4444/wd/hub',
#     desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})

session_id = driver.session_id

