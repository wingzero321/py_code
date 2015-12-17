# data_mongo_price.py
# -*- coding: utf8 -*- 

import pymongo
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
# from openpyxl import Workbook
import csv
import datetime
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


def connectDB(host,port,db_name):
    # connect to mongoDB
    client = pymongo.MongoClient(host, port)
    db = client[db_name]
    tables_list = db.collection_names()
    return db,tables_list

def dataExport(data_dict,out_file,limit):
    writer = csv.writer(file(out_file, 'wb'))
    rowNum=0
    for row in data_dict:

        if rowNum==0:
            print 'data head',row.keys()
            writer.writerow(row.keys())
        row_encode = []

        for value in row.values():
            row_encode.append(str(value).encode('gb18030'))
        writer.writerow(row_encode)
        rowNum +=1
        if str(rowNum) == limit:break
        print 'rowNum is ',rowNum

    print 'NOTES:exprot finish!!'
    print 'export  file is :',out_file



if __name__=='__main__':

    db,tables_list=connectDB('10.0.0.200',27017,'social_survey')
    print tables_list
    limit_nm = 100
    d = datetime.datetime(2015,10,21,0,0)
    date = datetime.datetime.strftime(d,'%Y-%m-%d')
    print date
    cursor = db.price_report.find({"crawl_date": {"$gt": date},"source":"autohome"} )
    # cursor = db.price_report.find({"crawl_date": {"$gt": date},"source":"autohome","b_name":"雪佛兰"} ).limit(limit_nm)
    print cursor.count()
    # limit_f = '100000000000000'
    # out_file = "D:\project\project-py\data\price.csv"
    # dataExport(cursor,out_file,limit_f)
    print 'xxxxxxxxxx'