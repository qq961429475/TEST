from time import sleep
import pytest
from selenium.webdriver.common.by import By


def test_baidu_case01(browser):
    driver = browser
    driver.get("https://www.baidu.com")
    sleep(1)
    driver.find_element(By.ID,'kw').send_keys('狗狗币')
    sleep(1)
    driver.find_element(By.ID,'su').click()
    sleep(1)
    assert driver.title == "11狗狗币_百度搜索"


