from pages.login_page.login_page import LoginPage
from pages.email_page.email_page import EmailPage


class Application:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.login = LoginPage(self)
        self.email = EmailPage(self)

    def open_main_page(self):
        self.driver.get(self.url)

    def quit(self):
        self.driver.quit()
