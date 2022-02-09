import logging

from selenium.webdriver.remote.webelement import WebElement

from common.constants import EmailConstants
from locators.email_page_locators import EmailPageLocators
from locators.login_page_locators import LoginPageLocators

from models.auth import AuthData
from pages.base_page import BasePage

logger = logging.getLogger("test-task")


class LoginPage(BasePage):
    def click_first_login_button(self):
        self.click_element(self.first_login_button())

    def click_submit_button(self):
        self.click_element(self.submit_button())

    def input_email(self, text) -> None:
        email_locator = self.find_element(LoginPageLocators.LOGIN_FIELD)
        email_locator.send_keys(text)

    def input_password(self, text) -> None:
        password_locator = self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.fill_element(password_locator, text)

    def auth(self, data: AuthData):
        logger.info(f'User email is "{data.login}, user password {data.password}"')
        self.app.login.click_first_login_button()
        self.input_email(data.login)
        self.click_submit_button()
        self.input_password(data.password)
        self.click_submit_button()

    def submit_button(self) -> WebElement:
        return self.find_element(LoginPageLocators.LOGIN_BUTTON)

    def first_login_button(self) -> WebElement:
        return self.find_element(LoginPageLocators.FIRST_LOGIN_BUTTON)

    def is_auth(self):
        element = self.find_element(EmailPageLocators.TO_WRITE_EMAIL_BUTTON).text
        return element == EmailConstants.SEND_EMAIL_BUTTON_TEXT
