# data_parse_xml.py
# -*- coding: UTF-8 -*-

from xml.dom.minidom import parse
import xml.dom.minidom

# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse("D:\project\project-iproduct\UGC.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("rules"):
   print "Root element : %s" % collection.getAttribute("rules")

# # 在集合中获取所有电影
rules = collection.getElementsByTagName("rules")

# # 打印每部电影的详细信息
for rule in rules:
   print "*****rules*****"
   type = rule.getElementsByTagName('Comments')[0]
   print "Comments: %s" % type.childNodes[0].data

print dir(rule)

   # if rule.hasAttribute("Comments"):
   #    print "Title: %s" % rule.getAttribute("Comments")

#    type = movie.getElementsByTagName('type')[0]
#    print "Type: %s" % type.childNodes[0].data
#    format = movie.getElementsByTagName('format')[0]
#    print "Format: %s" % format.childNodes[0].data
#    rating = movie.getElementsByTagName('rating')[0]
#    print "Rating: %s" % rating.childNodes[0].data
#    description = movie.getElementsByTagName('description')[0]
#    print "Description: %s" % description.childNodes[0].data