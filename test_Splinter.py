# test_Splinter.py
#coding=utf-8

import time
from splinter import Browser
from splinter import request_handler



def splinter(url):
    browser = Browser()
    #login 126 email websize
    browser.visit(url)
    time.sleep(1)
    browser.find_by_id('text').fill(text)
    browser.find_by_id('go').click()
    time.sleep(1)
    # print browser.find_by_id('download-png')
    browser.find_by_id('download-png').click()
    browser.attach_file('transparent shrinkToFit', 'C:\\somefile.jpg')
    
    time.sleep(1)
    #close the window of brower
    # browser.quit()

if __name__ == '__main__':
    websize3 ='http://www.jasondavies.com/wordcloud/'
    text = u'sjdlajsldjsa sadjlsa sadjslaj asdjlas asdjljslad sadjlasdj sadjsaldj'
    splinter(websize3)
    