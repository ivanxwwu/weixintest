#-*- coding:utf8 -*-
import time
import urllib2
from weixintest import core
import requests
import json
from weixintest.core import constants
class Tuling(object):
    def __init__(self):
        self.api_url = 'http://www.tuling123.com/openapi/api'
    def get_info(self):
        return "success"

class IdiomsSolitaire(Tuling):
    def __init__(self, info, userid):
        Tuling.__init__(self)
        self.info = info
        self.userid = userid

    def get_info(self):
        post_data = dict(
            info = '成语接龙' + self.info,
            userid = self.userid,
            key = constants.tuling_key
        )
        postHeaders = {
            'Content-Type':'application/json'
        }
        res = requests.post(self.api_url, json = post_data, headers = postHeaders)
        print res.text
        text = str(res.json().get('text').encode('utf8'))
        if text.startswith('进入成语接龙模式'):
            text = text[len('进入成语接龙模式'):]
            if text[:3] != self.info[9:]:
                text = '无此成语，客官请接：' + text
        if text == '你对错了，成语重复，退出成语接龙模式':
            text = '你对错了，成语重复'
        if text == '你接错了，退出成语接龙模式！':
            text = '你接错了'

        return text


if __name__ == '__main__':
    t = IdiomsSolitaire('中1囊', '2343')
    print t.get_info()

