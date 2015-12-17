# data_importCsv.py
# -*- coding: utf8 -*-
import csv
from openpyxl import Workbook


# 创建新的excel文件
wt_wb = Workbook(write_only=True)
wt_ws = wt_wb.create_sheet()

file = open('E:/project-CAC/csv/new/ttt.csv')
reader = csv.reader(file)
index=0
for line in reader:
	# if index>3:
		# index=0
	index+=1
	if index <=3:
		if index==1:
			data_list=[]
			data_list.append(line[0])
			data_list.append(line[1])
			data_list.append(line[2])
		if index==2:
			data_list.append(line[0])
		if index==3:
			data_list.append(line[0])
			data_list.append(line[1])
			data_list.append(line[2])
		wt_ws.append(data_list)
		# for m in data_list:
		# 	print m

# 保存输出文件
wt_wb.save('E:/project-CAC/csv/new/output.xlsx')