import pytest
import requests
from faker import Faker

from part3.mock import total_data

fake = Faker("en_US")


# ------------------------------------------------------------------------------------------------------------------
class TestServer:

    # ------------------------------------------------------------------------------------------------------------------
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mock_server):
        self.host, self.port = mock_server

    # ------------------------------------------------------------------------------------------------------------------
    @pytest.mark.mock
    def test_get_data(self):
        url = f"http://{self.host}:{self.port}/get_data"
        new_data = {}
        for i in range(4):
            new_data.update({str(i): {fake.email(): fake.first_name()}})
        total_data.update(new_data)
        res = requests.get(url=url)
        assert res.json() == total_data

    # ------------------------------------------------------------------------------------------------------------------
    @pytest.mark.mock
    def test_post_data(self):
        url = f"http://{self.host}:{self.port}/post_data"
        some_data = {'2': {fake.email(): fake.first_name()},
                     '3': {fake.email(): fake.first_name()}}

        res = requests.post(url=url, json=some_data)
        assert res.status_code == 200



