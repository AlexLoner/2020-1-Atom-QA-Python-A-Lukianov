from urllib.parse import urljoin
import requests

class ClientAPI:

    def __init__(self, links):
        self.url = 'https://target.my.com/'
        self.email = 'mccor44ick.kenny@yandex.ru'
        self.password = 'ewlkj897H'
        self.links = links
        self.session = requests.Session()


    def login(self):
        data = {'email': self.email, 'password': self.password}
        headers = {'Referer': self.url}

        url = urljoin(self.url, self.links['auth'])
        response = self.session.request('POST', url, data=data, headers=headers, allow_redirects=False)
        headers = response.headers
        return headers['Location']
