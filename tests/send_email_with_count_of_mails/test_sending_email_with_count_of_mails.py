from common.constants import EmailConstants
from models.auth import AuthData


class TestSendingEmailWithCountOfMails:
    def test_sending_email_with_count_of_mails_valid_data(self, app):
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
        7. In the "Search" field, enter the correct query "Simbirsoft Test task"
            - displayed in the field   #noqa
        8. Click on the "Find" button
            - five elements with the theme "Simbirsoft Test task" will be displayed   #noqa
        9. Compare the received number of emails from the selenium    #noqa
        10. Click on the "Write" button -
            The transition to the letter creation page is completed
        11. In the "To" field, enter your email - email is displayed in the field
        12. In the "Subject" field, enter "Simbirsoft Test task. <Last Name>"-
            The entry is correctly displayed in the Subject field
        13. In the body of the letter, enter the number of sent letters in the format
            "Letters from the third step received. Now there are {0}" -
             The text is displayed correctly and the number of
        14. Click on the send button to make sure that the email has been sent
        """
        app.open_auth_page()
        app.login.click_first_login_button()
        data = AuthData(login="task.testing@yandex.ru", password="Username1")
        app.login.input_email(data.login)
        app.login.click_submit_button()
        app.login.input_password(data.password)
        app.login.click_submit_button()
        assert app.login.is_auth(), "We are not auth"
        app.email.input_search_field("Simbirsoft Тестовое задание")  # noqa
        app.email.click_search_button()
        app.email.click_to_write_email_button()
        app.email.input_to_field(data.login)
        app.email.input_subject_field("Simbirsoft Тестовое задание. Манаев")
        app.email.input_body_of_mail_field(
            "Письма с третьего шага получены. Сейчас их {0}".format(
                app.email.find_list_of_mails()
            )
        )
        app.email.click_send_email_button()
        assert app.email.is_success_send() == EmailConstants.SUCCESS_SEND_EMAIL_TEXT
