import logging

from selenium.webdriver.remote.webelement import WebElement
from locators.email_page_locators import EmailPageLocators
from pages.base_page import BasePage

logger = logging.getLogger("test-task")


class EmailPage(BasePage):
    def input_search_field(self, text) -> None:
        search_field_locator = self.find_element(EmailPageLocators.SEARCH_FIELD)
        search_field_locator.send_keys(text)

    def find_search_button(self) -> WebElement:
        return self.find_element(EmailPageLocators.SEARCH_BUTTON)

    def click_search_button(self):
        self.click_element(self.find_search_button())

    def find_list_of_mails(self) -> int:
        element = self.find_elements(EmailPageLocators.LIST_OF_MAILS)
        return len(element)

    def yandex_number_of_mails(self):
        element = self.find_element(EmailPageLocators.COUNT_OF_MAILS_BY_YANDEX).text
        element_convert_to_int = "".join(filter(lambda x: x.isdigit(), element))
        element_convert_to_int = int(element_convert_to_int)
        return element_convert_to_int
