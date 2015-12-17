# data_mongo_export.py
# -*- coding: utf8 -*- 


import pymongo
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
# from openpyxl import Workbook
import csv
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
from Tkinter import *

def connectDB(host,port,db_name):
	# connect to mongoDB
	client = pymongo.MongoClient(host, port)
	db = client[db_name]
	tables_list = db.collection_names()
	print tables_list
	return db

def convert( filename, in_enc ="utf-8",out_enc="gbk"):  
    try:  
        print "convert " + filename,  
        content = open(filename).read()  
        new_content = content.decode(in_enc).encode(out_enc)  
        open(filename, 'w').write(new_content)  
        print " done"
    except:
        print " error"


def dataExport(data_dict,out_file,limit):
	print type(limit)
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


def dataExportFile(file,data_table,limit):
	print '输出文件',file,'导出数据',data_table,'数据限制行数',limit
	
	db=connectDB('10.0.0.200',27017,'test')
	# wheres_query = 
	cursor = db[data_table].find()
	print 'data counts is :',cursor.count()
	dataExport(cursor,file,limit)


def view():
	root = Tk()
	root.title("mongo数据导出工具")
	root.geometry('500x450')        
	root.resizable(width=True, height=True)


	topFrame=Frame(root)
	contentFrame=Frame(root)
	bottomFrame=Frame(root)
	bottomallFrame=Frame(root)
	topFrame.pack(side=TOP)
	contentFrame.pack(side=TOP)
	bottomFrame.pack(side=TOP)
	bottomallFrame.pack(side=TOP)

	var1 = StringVar()
	var1.set("D:\project\project-py\data\data.csv")
	var2 = StringVar()
	var2.set('buyer_list')
	var3 = StringVar()
	var3.set('1000')

	Label(topFrame, text=u'<<<<<<<<测试版本>>>>>>>>>').pack()


	Label(contentFrame, text=u'导出数据集',height=2).pack(side=TOP)
	Entry(contentFrame, textvariable = var2,width=40).pack(side=TOP)
	Label(contentFrame, text=u'本地文件地址',height=2).pack(side=TOP)
	Entry(contentFrame, textvariable = var1,width=40).pack(side=TOP)
	Label(contentFrame, text=u'数据输出限制行数',height=2).pack(side=TOP)
	Entry(contentFrame, textvariable = var3,width=40).pack(side=TOP)

	# Label(bottomFrame, text=u'').pack(side=TOP)
	# Button(bottomFrame, text="CSV数据导出",command = lambda:dataExportFile(var1.get(),var2.get(),var3.get())).pack(side=LEFT,pady=30)
	Button(bottomFrame, text="QUIT",command = quit).pack(side=LEFT,pady=30,padx=10)
	t=Text(bottomallFrame,height=5)
	t.pack(side=TOP)
	Button(bottomFrame, text="CSV数据导出",command = lambda:dataExportFile(var1.get(),var2.get(),var3.get())).pack(side=LEFT,pady=30)
	Label(bottomallFrame, text=u'Power by mathartsys.').pack(side=TOP)

	# help(Button.pack)

	root.mainloop()



if __name__=='__main__':

	view()