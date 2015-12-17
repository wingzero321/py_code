# data_csv_trans.py
# -*- coding: utf8 -*-

# csv文件从utf8 转为 gbk
import pymongo
import pandas as pd
from bson.son import SON
import csv
import os
from datetime import date
import datetime
# import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')
reload(sys)


def csv_trans_gbk(in_file,out_file):

	print '>>>in_file is :',in_file

	reader = csv.reader(file(in_file, 'rb'))
	writer = csv.writer(file(out_file, 'wb'))
	rowNum=0
	for line in reader:
		# print line
		data_row = []
		for item in line:
			# data_row.append(str(item).decode('string-escape').decode("gbk"))
			data_row.append(str(item).encode('gb18030'))
		writer.writerow(data_row)


		rowNum+=1
		# if rowNum == 5:break
	
	print 'rowNum is:',rowNum



def trans_all():
	
	start_date = date(2015,10,21)
	print str(start_date)

	gap = datetime.date.today() - start_date
	print gap.days

	count = 0
	while (count<=gap.days):

		day = start_date + datetime.timedelta(days = count)
		print 'The count is:', count,day


		in_file = 'D:\project\project-carNew\price_malibu\pirice_Malibu_%s.csv' %day
		out_file = "D:\project\project-carNew\price_malibu\\trans\pirice_Malibu_t_%s.csv" %day

		if os.path.isfile(out_file)==False:
			csv_trans_gbk(in_file,out_file)

		count = count + 1


def downloadfile():
	import ssh

	# New SSHClient
	client = ssh.SSHClient()
	 
	# Default accept unknown keys
	client.set_missing_host_key_policy(ssh.AutoAddPolicy())
	 
	# Connect
	client.connect("120.26.38.147", port=22, username="minkedong", password="mkd")
	 
	# Execute shell remotely
	stdin, stdout, stderr = client.exec_command("cd price_malibu;ls")
	# stdin, stdout, stderr = client.exec_command("ls -alh")
	print stdout.read()

	sftp = client.open_sftp()

	sftp.get('/home/minkedong/price_malibu/price_Malibu_2015-10-29.csv', 'D:\\price_Malibu_2015-10-29.csv')


def dataExport(data_dict,out_file,limit):
	# print type(limit)
	writer = csv.writer(file(out_file, 'wb'))
	rowNum=0
	for row in data_dict:

		if rowNum==0:
			print 'data head',row.keys()
			writer.writerow(row.keys())
		row_encode = []

		for value in row.values():
			# print value
			row_encode.append(str(value).encode('gb18030'))
		writer.writerow(row_encode)

		rowNum +=1
		if str(rowNum) == limit:break
		print 'rowNum is ',rowNum
		# text.insert('1.0', 'rowNum is '+ str(rowNum) + '\n')
	print 'NOTES:exprot finish!!'
	print 'export  file is :',out_file


def download_bbs():
	
	# client = pymongo.MongoClient('120.26.38.147', 27019)
	# client = pymongo.MongoClient('10.0.0.200', 27017)
	# db = client['social_survey_test']
	# db.authenticate("ugc","a1b2c3d4")
	# 
	query_car = "迈锐宝"

	client = pymongo.MongoClient('10.0.0.200', 27017)
	db = client['social_survey']
	cursor = db.bbs_auto.find({"carType":query_car,'bbs_type':0})

	print cursor.count()

	# out_file = 'D:\project\project-carNew\csv\l_bbs_Q5_s.csv'
	# dataExport(cursor,out_file,10000000000000000)




if __name__=='__main__':

	# in_file = 'D:\project\project-carNew\price_malibu\pirice_Malibu_2015-10-25.csv'
	# out_file = "D:\project\project-carNew\price_malibutrans\pirice_Malibu_t_2015-10-25.csv"

	# csv_trans_gbk(in_file,out_file)

	# trans_all()
	
	# downloadfile()
	# 
	# 
	download_bbs()
	
	# db_ip = '120.26.38.147'
	# db_port = 27019
	# database = 'social_survey_test'
	# user = "ugc"
	# password = "a1b2c3d4"
	# query_date = str(datetime.date.today()+ datetime.timedelta(days=0))
	# out_file = 'D:\project\project-carNew\\test.csv'

	# client = pymongo.MongoClient(db_ip, db_port)
	# db = client[database]
	# db.authenticate(user,password)
	
	# print 'query_date is:',query_date
	# cursor = db.price_report.find({'crawl_date':query_date})

	# print 'data count is :',cursor.count()

	# pipeline = [
	# {"$group" : {"_id" : "$crawl_date", "num_count" : {"$sum" : 1}}},
	# {"$sort": SON([("count", -1), ("_id", -1)])}
	# ]


	# print list(db.price_report.aggregate(pipeline))

	# dataExport(cursor,out_file,100000000000000)


	# df =  pd.DataFrame(list(cursor))
	# print df[1]

	# list = df.tolist()

	# print list

