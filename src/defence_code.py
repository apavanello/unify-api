import json

from .connectors import Unify

LOGIN_URL = 'https://wifi.livrariacultura.com.br:8443/api/login'


class DefenceCode(object):

    def __init__(self):
        self.error_code = '0'

    def checks(self, version, extra_args, request_method):

        v_code = self.chk_version(version)

        ex_code = self.chk_extra_args(extra_args)

        m_type = self.chk_request_method(request_method)

        data = {
            'responses': {
                'Version': version,
                'Extra': extra_args,
                'Method': request_method,
            },
            'return code': self.error_code
        }
        response = json.dumps(data)

        if self.error_code == "0":

            connector = Unify()
            login_code = connector.login(LOGIN_URL)

            response = str(login_code)
        return response

    def chk_version(self, version):

        if str(version).upper() == 'V1':

            response = '1'

        else:

            response = '0'

            self.error_code = 'ERR-1'

        return response

    def chk_extra_args(self, extra_args):

        if str(extra_args).upper() == 'TOKEN':

            response = 'T'

        else:

            response = '0'

            self.error_code = 'ERR-2'

        return response

    def chk_request_method(self, request_method):

        if request_method == 'GET':

            response = 'GET'

        else:
            response = '0'

            self.error_code = 'ERR-3'

        return response
