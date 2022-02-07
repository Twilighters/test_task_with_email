from selenium.webdriver.common.by import By


class EmailPageLocators:
    SEARCH_FIELD = (By.CSS_SELECTOR, ".textinput__control")
    TO_WRITE_EMAIL_BUTTON = (By.CSS_SELECTOR, ".mail-ComposeButton-Text")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".search-input__form-button")
    LIST_OF_MAILS = (By.XPATH, "//span[@title='Simbirsoft Тестовое задание']")
    COUNT_OF_MAILS_BY_YANDEX = (By.CSS_SELECTOR, ".mail-MessagesSearchInfo-Title_misc")
    # Menu of profile
    USER_MENU = (By.CSS_SELECTOR, "[href] [srcset]")
    EXIT = (By.CSS_SELECTOR, "li:nth-of-type(6) > a[role='link'] > .menu__text")
    # Write e-mail
    TO_FIELD = (By.CSS_SELECTOR, ".ComposeRecipients-ToField .composeYabbles")
    SUBJECT_FIELD = (By.CSS_SELECTOR, "input[name='subject']")
    BODY_OF_MAIL_FIELD = (By.CSS_SELECTOR, "#cke_1_contents_wrap [hidefocus] div")
    SEND_MAIL_BUTTON = (By.CSS_SELECTOR, "[aria-disabled='false']")
    SUCCESS_SEND_EMAIL = (By.CSS_SELECTOR, ".ComposeDoneScreen-Title")
