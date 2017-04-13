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
from ..models import receivce
from ..models import reply
import time
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import sys
from ..models import reply

app = flask.Blueprint('weixintest', __name__)


@app.route('/', strict_slashes=False, methods=['GET', 'POST'])
@check_weixin_sig
def index():
    #echostr = flask.request.args.get('echostr', '')
    msg = receivce.parse_xml(flask.request.data)
    if isinstance(msg, receivce.Msg):
        touser = msg.FromUserName
        fromuser = msg.ToUserName
        print msg.MsgType
        if msg.MsgType == 'text':
            content = 'test'
            replymsg = reply.TextMsg(touser, fromuser, content)
            return normal_success_response(replymsg.send())
        if msg.MsgType == 'image':
            mediaId = msg.MediaId
            replymsg = reply.ImageMsg(touser, fromuser, mediaId)
            return replymsg.send()
        else:
            return reply.Msg().send()
    else:
        return normal_success_response("success")
