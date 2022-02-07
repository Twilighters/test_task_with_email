import pytest


class TestCountingEmails:
    @pytest.mark.xfail
    def test_counting_emails(self, app, auth):
        """
        Steps
            0. PreConditions - completed authorization test
        1. In the "Search" field, enter the correct query "Simbirsoft Test task"
        - displayed in the field   #noqa
        2. Click on the "Find" button
        - five elements with the theme "Simbirsoft Test task" will be displayed   #noqa
        3. Compare the received number of emails from the selenium
         method with the Yandex system    #noqa
        """

        app.email.input_search_field("Simbirsoft Тестовое задание")  # noqa
        app.email.click_search_button()
        assert app.email.find_list_of_mails() == app.email.yandex_number_of_mails(), (
            "The number of emails with " "the Yandex system does not match"
        )
