import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.audience import AudPage
from pages.base import BasePage
from pages.home import HomePage


@pytest.fixture(scope='function')
def base_page(driver):
    return BasePage(driver)


@pytest.fixture(scope='function')
def home_page(driver):
    return HomePage(driver)


@pytest.fixture(scope='function')
def aud_page(driver):
    return AudPage(driver)


@pytest.fixture(scope='function')
def driver(config):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': f'en,en-us'})
    manager = ChromeDriverManager(version=config['version'])

    browser = webdriver.Chrome(executable_path=manager.install(), options=options)
    browser.maximize_window()
    browser.get(config['url'])
    yield browser
    browser.close()


@pytest.fixture(scope='function')
def auto_log(driver, config):
    page = BasePage(driver)
    page._log_in(config['kenny'], config['kenny_pas'])
    return HomePage(page.driver)
