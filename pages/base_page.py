from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import WAIT_TIME


class BasePage:
    def __init__(self, app):
        self.app = app

    def find_element(self, locator):
        element = WebDriverWait(self.app.driver, WAIT_TIME).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )
        return element

    @staticmethod
    def fill_element(element, text):
        element.clear()
        if text:
            element.send_keys(text)
            return element

    @staticmethod
    def click_element(element):
        element.click()

    def find_elements(self, locator):
        return self.app.driver.find_elements(*locator)
