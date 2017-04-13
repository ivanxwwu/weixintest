#-*- coding:utf8 -*-

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import sys

country_string = '''
  <data>
    <country name="Singapore">
      <rank>4</rank>
      <year>2011</year>
      <gdppc>59900</gdppc>
      <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
      <rank>68</rank>
      <year>2011</year>
      <gdppc>13600</gdppc>
      <neighbor name="Costa Rica" direction="W"/>
      <neighbor name="Colombia" direction="E"/>
    </country>
  </data>
'''

try:
    #tree = ET.parse("country.xml")     #打开xml文档
    tree = ET.fromstring(country_string) #从字符串传递xml

    print tree
    root = tree.find('data')         #获得root节点
except Exception, e:
    print "Error:cannot parse file:country.xml."
    sys.exit(1)
print root.tag, "---", root.attrib
for child in root:
    print child.tag, "---", child.attrib

print "*"*10
print root[0][1].text   #通过下标访问
print root[0].tag, root[0].text
print "*"*10

for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print name, rank

#修改xml文件
for country in root.findall('country'):
    rank = int(country.find('rank').text)
if rank > 50:
    root.remove(country)

tree.write('output.xml')
