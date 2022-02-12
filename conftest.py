import logging

import allure
import pytest
from selenium import webdriver

from config import LOGIN
from config import PASSWORD
from config import URL
from models.auth import AuthData
from pages.application.application import Application

logger = logging.getLogger('test_platform')

capabilities_chrome = {
    'browserName': 'chrome',
    'browserVersion': '98.0',
    'selenoid:options': {'enableVNC': True, 'enableVideo': False},
}

driver_chrome = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    desired_capabilities=capabilities_chrome.copy(),
)

capabilities_firefox = {
    'browserName': 'firefox',
    'browserVersion': '96.0',
    'selenoid:options': {
        'enableVNC': True,
        'enableVideo': False,
    },
}

driver_firefox = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    desired_capabilities=capabilities_firefox.copy(),
)

driver_list = [driver_chrome, driver_firefox]


@pytest.fixture(scope='session', params=driver_list)
def app(request):
    base_url = request.config.getoption('--base-url')
    fixture = Application(request.param, base_url)
    yield fixture
    fixture.quit()


@pytest.fixture
def auth(app, request):
    username = request.config.getoption('--username')
    password = request.config.getoption('--password')
    app.open_main_page()

    auth_data = AuthData(login=username, password=password)
    app.login.auth(auth_data)
    assert app.login.is_auth(), 'You are not auth'
    return auth_data


def pytest_addoption(parser):
    parser.addoption(
        '--headless',
        action='store',
        default='true',
        help="enter 'true' if you want run tests in headless mode of browser,\n"
             "enter 'false' - if not",
    ),
    parser.addoption(
        '--base-url',
        action='store',
        default=URL,
        help='enter base_url',
    ),
    parser.addoption(
        '--username',
        action='store',
        default=LOGIN,
        help='enter username',
    ),
    parser.addoption(
        '--password',
        action='store',
        default=PASSWORD,
        help='enter password',
    ),


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        try:
            if 'app' in item.fixturenames:
                web_driver = item.funcargs['app']
            else:
                logger.error('Fail to take screen-shot')
                return
            logger.info('Screen-shot done')
            allure.attach(
                web_driver.driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG,
            )
        except Exception as e:
            logger.error(f'Fail to take screen-shot: {e}')
