import pytest

from api.client_api import ClientAPI
from fixtures_ui import *

def pytest_addoption(parser):
    parser.addoption('--url', default='https://target.my.com/')
    parser.addoption('--browser', default='chrome')
    parser.addoption('--browser_ver', default='80.*')
    parser.addoption('--selenoid', default=False)


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    browser = request.config.getoption('--browser')
    version = request.config.getoption('--browser_ver')
    selenoid = request.config.getoption('--selenoid')

    kenny = 'mccor44ick.kenny@yandex.ru'
    kenny_pas = 'ewlkj897H'

    return {'browser': browser, 'version': version, 'url': url, 'kenny': kenny,
            'kenny_pas': kenny_pas, 'selenoid': selenoid}


@pytest.fixture(scope='session')
def config_api():
    settings = {
        'auth': 'https://auth-ac.my.com/auth?lang=ru&nosavelogin=0',
        'check_auth': 'http://mail.my.com/'

    }
    return settings


@pytest.fixture(scope='function')
def api_client(config_api):
    return ClientAPI(config_api)
