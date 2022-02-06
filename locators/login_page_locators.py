from selenium.webdriver.common.by import By


class LoginPageLocators:
    FIRST_LOGIN_BUTTON = (By.CSS_SELECTOR, ".button2_theme_mail-white")
    LOGIN_FIELD = (By.ID, "passp-field-login")  # noqa
    LOGIN_BUTTON = (By.ID, "passp:sign-in")  # noqa
    PASSWORD_FIELD = (By.ID, "passp-field-passwd")  # noqa
