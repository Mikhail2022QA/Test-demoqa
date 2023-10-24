from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions, Options
from selenium.webdriver.common.by import By
import pytest
import time
import json

@pytest.mark.usefixtures('setup')
class TestMain:

    def test_1(self):
        self.driver.get('https://demoqa.com')
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div/div/div[1]/span/div/div[1]/span/svg').click()
        self.driver.find_element(By.XPATH, '//*[@id="item-1"]/span').click()
        self.driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/span/button/svg').click()
        self.driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[3]/span/button').click()
        self.driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[3]/ol/li[1]/span/label/span[1]').click()
