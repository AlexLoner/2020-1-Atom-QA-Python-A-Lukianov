import json
import requests

class ClientAPI:

    def __init__(self, links):
        self.email = 'mccor44ick.kenny@yandex.ru'
        self.password = 'ewlkj897H'
        self.links = links
        self.session = requests.Session()

    def get_csrftoken(self):
        r = self.session.request('GET', self.links['csrf'])
        print(r.status_code)
        print(r.headers)
        return r.headers['Set-Cookie'].split('=')[1].split(';')[0]


    def login(self):
        data = {'email': self.email, 'password': self.password,
                "continue": self.links['login'],}

        headers = {'Referer': 'https://target.my.com/',
                   "Content-Type": "application/x-www-form-urlencoded"}

        r = self.session.request('POST', self.links['auth'], data=data, headers=headers, allow_redirects=False)
        while r.status_code != 200:
            r = self.session.request('GET', r.headers['Location'], allow_redirects=False)
        self.csrf = self.get_csrftoken()
        return r

    def creation(self):
        data = {"name": 'kenni', "pass_condition": 2,
                "relations": [{"params": {"type": "positive", "left": 365, "right": 0},
                               "object_type": "remarketing_payer",
                               "object_id": 569990},
                               {"params": {"type": "positive", "left": 365, "right": 0},
                               "object_type": "remarketing_player",
                               "object_id": 4792690}
                               ],
                }
        headers = {
            'Content-Type': 'application/json',
            'Referer': 'https://target.my.com/segments/segments_list/new',
            'X-CSRFToken': self.csrf,
            'X-Requested-With': 'XMLHttpRequest',
        }
        r = self.session.request('POST', self.links['create_segment'], headers=headers, json=data)
        return r

    def delete_segment(self):
        r = self.creation()
        headers = {
            'Referer': 'https://target.my.com/segments/segments_list',
            'X-CSRFToken': self.csrf,
            'X-Requested-With': 'XMLHttpRequest',
        }
        link = f"{self.links['delete_segment']}{r.json()['id']}.json"
        new_r = self.session.request('DELETE', link, headers=headers)
        return new_r