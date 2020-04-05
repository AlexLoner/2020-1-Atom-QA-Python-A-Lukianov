import pytest
from api.client_api import ClientAPI


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, config_api, request):
        self.config = config_api
        self.api_client: ClientAPI = request.getfixturevalue('api_client')
