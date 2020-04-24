import pytest

from pages.audience import AudPage
from pages.base import BasePage
from pages.home import HomePage


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request):
        self.driver = driver
        self.config = config
        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.aud_page: AudPage = request.getfixturevalue('aud_page')
