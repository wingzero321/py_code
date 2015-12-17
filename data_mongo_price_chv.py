# data_mongo_price_chv.py
# -*- coding: utf8 -*- 


import csv

reader = csv.reader(file('D:\project\project-carNew\csv\\apo_veh_20151022.csv', 'rb'))


data_list = []
row_nm=0
for line in reader:
	row_nm+=1
	print row_nm