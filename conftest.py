import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions, Options
from selenium.webdriver.common .by import By

@pytest.fixture(scope='class')
def setup(request):
    with open('setting.json', 'r') as setting:
        setting = json.loads(setting.read())
    if setting['browser'] == "chrome":
        driver = webdriver.Chrome()
    elif setting['browser'] == "firefox":
        driver = webdriver.Firefox()
    else:
        print("Некорректно указан браузер в настройках")
    chrome_options=Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.set_window_size(1920, 1080)
    request.cls.driver = driver
    yield driver
    driver.close()
