# coding: utf8
#
# weixintest - version
#
# Author: ilcwd
# Create: 14/11/12
#

import flask
import hashlib
from ..core import success_response, normal_success_response
from ..core import config
from decorators import check_weixin_sig
import time
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import sys

app = flask.Blueprint('weixintest', __name__)


@app.route('/', strict_slashes=False, methods=['GET', 'POST'])
#@check_weixin_sig
def index():
    #echostr = flask.request.args.get('echostr', '')
    tree = ET.fromstring(flask.request.data)
    tousername = tree.find('ToUserName').text
    fromusername = tree.find('FromUserName').text
    create_time = tree.find('CreateTime').text
    content = tree.find('Content').text
    msgid = tree.find('MsgId').text
    msgtype = tree.find('MsgType').text
    fromusername.text, tousername.text = tousername.text, fromusername.text
    create_time.text = str(int(time.time()))
    return normal_success_response(ET.tostring(tree))
