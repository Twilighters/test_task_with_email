from models.auth import AuthData


class TestAuth:
    def test_auth_valid_data(self, app):
        """
        Steps
        1. Open the authorization page for email - The page opened with the Login button
        2. Click on the Login button - The go to the Authorization page for the mail service is completed # noqa
        3. Enter the correct email in the ID field - email is displayed in the field
        4. Click on the login button - The password field is displayed on the page
        5. Enter the correct password in the password field - the password is displayed in the field in the form # noqa
            of asterisks # noqa
        6. Click on the login button - the transition to the page of the mail service has been completed on the page # noqa
            there is a "Write" button # noqa
        """
        app.open_auth_page()
        app.login.click_first_login_button()
        data = AuthData(login="task.testing@yandex.ru", password="Username1")
        app.login.input_email(data.login)
        app.login.click_submit_button()
        app.login.input_password(data.password)
        app.login.click_submit_button()
        assert app.login.is_auth(), "We are not auth"
