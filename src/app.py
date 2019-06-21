from flask import Flask
from flask import request
from src.classes import DefenceCode
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/v1/*": {"origins": "*"}})


@app.route('/<version>/<path:extra_args>', methods=['GET', 'POST'])
def api_selector(version, extra_args):

    df = DefenceCode()
    response = df.checks(version, extra_args, request.method)
    return '%s' % response


if __name__ == '__main__':
    app.run()
