# coding: utf8
#
# weixintest - version
#
# Author: ilcwd
# Create: 14/11/12
#

import flask

from ..core import success_response, normal_success_response

app = flask.Blueprint('weixintest', __name__)


@app.route('/', strict_slashes=False, methods=['GET', 'POST'])
def index():
    args = flask.request.args
    echostr = args.get('echostr', '')
    print echostr
    return normal_success_response(echostr)
