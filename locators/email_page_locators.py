from selenium.webdriver.common.by import By


class EmailPageLocators:
    SEARCH_FIELD = (By.CSS_SELECTOR, ".textinput__control")
    SEND_EMAIL_BUTTON = (By.CSS_SELECTOR, ".mail-ComposeButton-Text")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".search-input__form-button")
    LIST_OF_MAILS = (By.XPATH, "//span[@title='Simbirsoft Тестовое задание']")
    COUNT_OF_MAILS_BY_YANDEX = (By.CSS_SELECTOR, ".mail-MessagesSearchInfo-Title_misc")
    # Menu of profile
    USER_MENU = (By.CSS_SELECTOR, ".user-account__name")
    EXIT = (By.CSS_SELECTOR, "li:nth-of-type(6) > a[role='link'] > .menu__text")
