import logging

from selenium.webdriver.remote.webelement import WebElement
from locators.email_page_locators import EmailPageLocators
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage

logger = logging.getLogger("test-task")


class EmailPage(BasePage):
    def input_search_field(self, text) -> None:
        search_field_locator = self.find_element(EmailPageLocators.SEARCH_FIELD)
        search_field_locator.send_keys(text)

    def click_search_button(self):
        self.click_element(self.find_element(EmailPageLocators.SEARCH_BUTTON))

    def find_list_of_mails(self) -> int:
        element = self.find_elements(EmailPageLocators.LIST_OF_MAILS)
        return len(element)

    def yandex_number_of_mails(self) -> int:
        """
        Finding text as element and his convert to int
        """
        element = self.find_element(EmailPageLocators.COUNT_OF_MAILS_BY_YANDEX).text
        element = "".join(filter(lambda x: x.isdigit(), element))
        element = int(element)
        return element

    def to_write_email_button(self) -> WebElement:
        return self.find_element(EmailPageLocators.TO_WRITE_EMAIL_BUTTON)

    def click_to_write_email_button(self):
        self.click_element(self.to_write_email_button())

    def input_to_field(self, text) -> None:
        search_field_locator = self.find_element(EmailPageLocators.TO_FIELD)
        self.fill_element(search_field_locator, text)

    def input_subject_field(self, text) -> None:
        search_field_locator = self.find_element(EmailPageLocators.SUBJECT_FIELD)
        self.click_element(search_field_locator)
        self.fill_element(search_field_locator, text)

    def input_body_of_mail_field(self, text) -> None:
        body_field_locator = self.find_element(EmailPageLocators.BODY_OF_MAIL_FIELD)
        self.click_element(body_field_locator)
        self.fill_element(body_field_locator, text)

    def send_email_button(self) -> WebElement:
        return self.find_element(EmailPageLocators.SEND_MAIL_BUTTON)

    def click_send_email_button(self):
        self.click_element(self.send_email_button())

    def find_text_about_success_sending_email(self) -> str:
        element = self.find_element(EmailPageLocators.SUCCESS_SEND_EMAIL).text
        return element

    def click_user_menu_button(self):
        self.click_element(self.find_element(EmailPageLocators.USER_MENU))

    def click_exit_button(self):
        self.click_element(self.find_element(EmailPageLocators.EXIT))

    def current_account_from_login(self) -> WebElement:
        return self.find_element(LoginPageLocators.CURRENT_ACCOUNT)

    def delete_form_list_from_login(self) -> WebElement:
        return self.find_element(LoginPageLocators.DELETE_FROM_LIST)

    def previous_step_from_login(self) -> WebElement:
        return self.find_element(LoginPageLocators.PREVIOUS_STEP_BUTTON)

    def click_current_account_from_login(self):
        self.click_element(self.current_account_from_login())

    def click_dots_menu_from_login(self):
        self.click_element(self.find_element(LoginPageLocators.DOTS_MENU))

    def click_delete_form_list_from_login(self):
        self.click_element(self.delete_form_list_from_login())

    def click_previous_step_from_login(self):
        self.click_element(self.previous_step_from_login())

    def sign_out(self):
        self.click_user_menu_button()
        self.click_exit_button()
        self.click_current_account_from_login()
        self.click_dots_menu_from_login()
        self.click_delete_form_list_from_login()
        self.click_previous_step_from_login()
