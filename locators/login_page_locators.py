from selenium.webdriver.common.by import By


class LoginPageLocators:
    FIRST_LOGIN_BUTTON = (By.CSS_SELECTOR, ".button2_theme_mail-white")
    LOGIN_FIELD = (By.ID, "passp-field-login")  # noqa
    LOGIN_BUTTON = (By.ID, "passp:sign-in")  # noqa
    PASSWORD_FIELD = (By.ID, "passp-field-passwd")  # noqa
    # sign out
    CURRENT_ACCOUNT = (By.CSS_SELECTOR, ".CurrentAccount")
    DOTS_MENU = (
        By.CSS_SELECTOR,
        ".ContextMenuButton > .PasspIcon.PasspIcon_dots.PasspIcon_fill.PasspIcon_size_s",  # noqa
    )
    DELETE_FROM_LIST = (By.CSS_SELECTOR, ".ContextMenu-buttonName")
    PREVIOUS_STEP_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/a')
