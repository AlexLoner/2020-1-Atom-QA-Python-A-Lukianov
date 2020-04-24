import pytest


class TestAPI():

    @pytest.mark.API
    def test_auth(self, api_client):
        resp = api_client.login()
        assert resp.status_code == 200

    @pytest.mark.API
    def test_create(self, api_client):
        api_client.login()
        resp = api_client.creation()
        assert resp.status_code == 200

    @pytest.mark.API
    def test_createDelete(self, api_client):
        api_client.login()
        resp = api_client.delete_segment()
        assert resp.status_code == 204
