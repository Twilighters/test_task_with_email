import pytest


@pytest.fixture()
def counting_emails(app):
    app.email.input_search_field("Simbirsoft Тестовое задание")  # noqa
    app.email.click_search_button()
    count_of_mails = app.email.find_list_of_mails()
    return count_of_mails
