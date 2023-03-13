from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def visit(self, url):
        self.driver.get(url)

    def locate(self, loc, value):
        return self.driver.find_element(loc, value)

    def input(self, loc, value, input_value):
        self.locate(loc, value).send_keys(input_value)

    def click(self, loc, value):
        self.locate(loc, value).click()

    def quit(self):
        self.driver.quit()

    def wait(self, loc, value):
        return WebDriverWait(self.driver, 10, 0.5).until(lambda el: self.locate(loc, value), message='等待失败')

    def assert_text(self, loc, value, txt):
        try:
            assert txt == self.locate(loc, value).text, '断言失败'
            print(self.locate(loc, value).text)
            return True
        except:
            return False
