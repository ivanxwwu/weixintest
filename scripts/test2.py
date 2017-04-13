#-*- coding:utf8 -*-

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import sys

msg = '''
<xml>
    <URL><![CDATA[http://weixin.xivan.cn/weixintest]]></URL>
    <ToUserName><![CDATA[ivan]]></ToUserName>
    <FromUserName><![CDATA[ivan123]]></FromUserName>
    <CreateTime>123123213232</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[1232]]></Content>
    <MsgId>3333</MsgId>
</xml>
'''

try:
    #tree = ET.parse("country.xml")     #打开xml文档
    tree = ET.fromstring(msg) #从字符串传递xml

    print tree
    ToUserName = tree.find('ToUserName')         #获得root节点
    FromUserName = tree.find('FromUserName')
    FromUserName.text, ToUserName.text = ToUserName.text, FromUserName.text
    print ET.tostring(tree)
except Exception, e:
    print e
    sys.exit(1)
