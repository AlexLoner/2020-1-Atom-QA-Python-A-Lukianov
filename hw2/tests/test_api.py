import pytest


class TestAPI():

    @pytest.mark.API
    def test(self, api_client):
        loc = api_client.login()
        assert loc == api_client.links['check_auth']
