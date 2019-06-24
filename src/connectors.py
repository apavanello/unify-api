import json
import requests


BASE_URL = 'https://wifi.livrariacultura.com.br:8443/api/s/default'


class Unify(object):
    jar = []

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'Content-Type': "application/json",
            'User-Agent': "PostmanRuntime/7.13.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'accept-encoding': "gzip, deflate",
            'content-length': "36",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }

        self.voucher_url = f'{BASE_URL}/stat/voucher'
        self.hotspot_url = f'{BASE_URL}/cmd/hotspot'

        self.user = 'api'
        self.password = 'api'

    def login(self, url):
        data = {
            'username': self.user,
            'password': self.password
        }
        payload = json.dumps(data)

        response = self.session.post(
            url,
            data=payload,
        )

        response = self.create_token()

        return response

    def create_token(self):
        data = {
            'cmd': 'create-voucher',
            'expire': 60,
            'n': 1,
        }
        payload = json.dumps(data)

        response = self.session.post(
            self.hotspot_url,
            data=payload,
        )

        response_json = response.json()

        create_time = response_json['data'][0]['create_time']

        response = self.show_token(create_time)

        return response

    def show_token(self, create_time):
        data = {
            'create_time': create_time
        }
        payload = json.dumps(data)

        response = self.session.post(
            self.voucher_url,
            data=payload,
        )

        response_json = response.json()

        response = response_json['data'][0]['code']

        return response
