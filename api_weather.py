# api_weather.py
# -*- coding: utf-8 -*-
#
#
#req.add_header("apikey", "7794074d4d07d137dbdc60920212cfde")

import sys
import urllib
import urllib2
import json

url = 'http://apis.baidu.com/apistore/weatherservice/cityid?cityid=101010100'


req = urllib2.Request(url)

req.add_header("apikey", "7794074d4d07d137dbdc60920212cfde")

resp = urllib2.urlopen(req)
content = resp.read()
if(content):
    print(content)
