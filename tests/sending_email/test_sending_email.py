from common.constants import EmailConstants


class TestSendingEmail:
    def test_sending_email(self, app, auth, counting_emails):
        """
        Steps
            0. PreConditions: log in and count emails
            1. Click on the "Write" button -
            The transition to the letter creation page is completed
            2. In the "To" field, enter your email - email is displayed in the field
            3. In the "Subject" field, enter "Simbirsoft Test task. <Last Name>"-
            The entry is correctly displayed in the Subject field
            4. In the body of the letter, enter the number of sent letters in the format
            "Letters from the third step received. Now there are {0}" -
             The text is displayed correctly and the number of
            5. Click on the send button to make sure that the email has been sent
        """

        app.email.click_to_write_email_button()
        app.email.input_to_field(auth.login)
        app.email.input_subject_field("Simbirsoft Тестовое задание. Манаев")
        app.email.input_body_of_mail_field(
            "Письма с третьего шага получены. Сейчас их {0}".format(counting_emails)
        )
        app.email.click_send_email_button()
        assert app.email.is_success_send() == EmailConstants.SUCCESS_SEND_EMAIL_TEXT
