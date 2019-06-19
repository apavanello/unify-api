from flask import Flask
from flask import request
from src.classes import DefenceCode

app = Flask(__name__)


@app.route('/<version>/<path:extra_args>', methods=['GET', 'POST'])
def api_selector(version, extra_args):

    df = DefenceCode()
    response = df.checks(version, extra_args, request.method)
#   response = DefenceCode.checks(version=version, extra_args=extra_args, request_method=request.method)
    return '<h2> %s </h2>' % response


if __name__ == '__main__':
    app.run()
