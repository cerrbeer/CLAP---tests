from selenium import webdriver

CHROME_VERSION = '73'

# driver = webdriver.Chrome(f'E:/PythonProjects/CLAP---tests/chromedriver{CHROME_VERSION}.exe')
driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4444/wd/hub',
    desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})
