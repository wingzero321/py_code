# test.py
# -*- coding: utf8 -*-
import csv
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')

from snownlp import SnowNLP

# writer = csv.writer(file('D:\project\project-py\data\your.csv', 'wb'))

# writer.writerow(['SR_NUM','START_TIME','SPEAKER_ID','CONTENTS'])

# writer.writerow(['1-11111','2014/8/1 0:48','Customer','客户说的话,或者短句'])
# writer.writerow(['1-11111','2014/8/1 0:51','Services','客服说的话,或者短句'])
# writer.writerow(['1-11111','2014/8/1 0:57','Customer','客户说的话,或者短句'])
# writer.writerow(['1-11111','2014/8/1 0:59','Services','客服说的话,或者短句'])


# reader = csv.reader(file('D:\project\project-py\data\\aa.csv', 'r'))
# print reader.line_num
# for line in reader:
#     print line[3]


s = u'我太厉害了'
ss = s.split('。')
key_words = u"我"
words_list = [x.lower() for x in key_words.split()]

out_words=''
for item in ss:
    if all([word in item.lower() and True or False for word in words_list]):
    	out_words+='///'+item
        print item

print out_words


s1 = SnowNLP(s)
print s1.sentiments