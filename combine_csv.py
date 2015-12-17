#test.py
#encoding: utf-8
__author__ = 'DELL'
import csv
import glob
import datetime
import sys
import os
reload(sys)
#中文错误
sys.setdefaultencoding( "utf-8" )
'''
@author likehua
    CSV批处理
'''
class BatchProcessCSV:
    def __init__(self,inputfolder="c:\\input\\",outputfolder="c:\\output\\"):
        self.inputfolder=inputfolder
        self.outputfolder=outputfolder
    #批处理
    def doBatchAction(self):
        startTime=datetime.datetime.now()
        print(u"开始处理...")
        if (os.path.exists(self.outputfolder)==False):
            #pass
            os.makedirs(self.outputfolder)
        list_dirs = os.walk(self.inputfolder)
        for root, dirs, files  in list_dirs:
            #print i
             for file in files:
                otput=self.outputfolder+file
                self.readcsv2csv(self.inputfolder+file,otput)
                print(u"Running.........................\n")
 
        endTime=datetime.datetime.now()
        print(u"处理完成，耗时：%f秒"%(endTime-startTime).seconds)
 
    #读取一个csv提取部分信息生成新的CSV
    def readcsv2csv(self,inputfile,outputfile):
      with open(inputfile, 'rb') as csvfile:
        o=open(outputfile,"wb")
  #解决csv浏览乱码问题
        o.write('\xEF\xBB\xBF');
        writer=csv.writer(o)
        #读取列 将字符串转为数组
        column=csvfile.readline().split(",")
        #print(column.index('App Release Date'))
        #print(column)
        writer.writerow(['Rank' ,'Category', 'Country ','App Name', 'Value', 'Unit' , 'App Release Date', 'Publisher Name', 'Company Name', 'Parent Company Name'])
        reader = csv.reader(csvfile)
        #table = reader[0]
        #Rank, Category, Store, Device, Type, Country, Period,Version, App_ID, App_Name, Value, Unit, Value_Type, AppURL, App_IAP, App_Category, App_Device, Current_Price, App_Release_Date, Publisher_ID, Publisher_Name, CompanyName, ParentCompanyName, AppNameUnified, AppFranchise, UnifiedAppID, AppFranchiseID, CompanyID, ParentCompanyID
        for row in reader:
            lenth=len(row)
            if lenth>10:
                writer.writerow([row[column.index("Rank")],row[column.index("Category")],row[column.index("Country")],row[column.index("App Name")],row[column.index("Value")],row[column.index("Unit")],row[column.index("App Release Date")],row[column.index("Publisher Name")],row[column.index("Company Name")],row[column.index("Parent Company Name")]])
 
#process
if __name__=="__main__":
    csvProcess=BatchProcessCSV("e:\\ugc\\input\\","e:\\ugc\\output\\")
    csvProcess.doBatchAction()