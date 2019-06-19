import json
import requests


class Unify (object):

    jar = []

    def login(self, url):

        ses = requests.Session()

        user = 'api'
        password = 'api'
        payload = '{"username":"%s","password":"%s"}' % (user, password)
        headers = {
            'Content-Type': "application/json",
            'User-Agent': "PostmanRuntime/7.13.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'accept-encoding': "gzip, deflate",
            'content-length': "36",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }

        response = ses.post(url, data=payload, headers=headers)

        self.jar = ses.cookies

        response = self.create_token()

        return response

    def create_token(self):

        ses = requests.session()

        url = 'https://wifi.livrariacultura.com.br:8443/api/s/default/cmd/hotspot'
        payload = '''{"cmd":"create-voucher",
                        "expire":60,
                        "n":1}'''
        headers = {
            'Content-Type': "application/json",
            'User-Agent': "PostmanRuntime/7.13.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'accept-encoding': "gzip, deflate",
            'content-length': "36",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }

        response_json = ses.post(url, data=payload, headers=headers, cookies=self.jar)

        response_json = json.loads(response_json.content)

        create_time = response_json['data'][0]['create_time']

        response = self.show_token(create_time)

        return response

    def show_token(self, create_time):
        ses = requests.session()

        url = 'https://wifi.livrariacultura.com.br:8443/api/s/default/stat/voucher'
        payload = '{"create_time": %d}' % create_time
        headers = {
            'Content-Type': "application/json",
            'User-Agent': "PostmanRuntime/7.13.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'accept-encoding': "gzip, deflate",
            'content-length': "36",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }

        response_json = ses.post(url, data=payload, headers=headers, cookies=self.jar)

        response_json = json.loads(response_json.content)

        response = response_json['data'][0]['code']

        return response
