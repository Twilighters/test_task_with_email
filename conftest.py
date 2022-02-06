import logging

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.application.application import Application
from models.auth import AuthData

logger = logging.getLogger("test_platform")


@pytest.fixture(scope="session")
def app(request):
    base_url = request.config.getoption("--base-url")
    headless_mode = request.config.getoption("--headless").lower()
    logger.info(f"Start test platform {base_url} with headless={headless_mode} mode")
    if headless_mode == "true":
        chrome_options = Options()
        chrome_options.headless = False
        fixture = Application(
            webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options),
            base_url,
        )
    elif headless_mode == "false":
        fixture = Application(
            webdriver.Chrome(ChromeDriverManager().install()),
            base_url,
        )
    else:
        raise pytest.UsageError("--headless should be true or false")
    yield fixture
    fixture.quit()


@pytest.fixture
def auth(app, request):
    username = request.config.getoption("--username")
    password = request.config.getoption("--password")
    app.open_auth_page()

    auth_data = AuthData(login=username, password=password)
    app.login.auth(auth_data)
    assert app.login.is_auth(), "You are not auth"


def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store",
        default="true",
        help="enter 'true' if you want run tests in headless mode of browser,\n"
        "enter 'false' - if not",
    ),
    parser.addoption(
        "--base-url",
        action="store",
        default="https://mail.yandex.ru/",
        help="enter base_url",
    ),
    parser.addoption(
        "--username",
        action="store",
        default="task.testing@yandex.ru",
        help="enter username",
    ),
    parser.addoption(
        "--password",
        action="store",
        default="Username1",
        help="enter password",
    ),