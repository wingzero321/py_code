# test_forlily.py

import itertools

data = [1.1,3,5,10,20,22,14,16,22,15,1,1,1,2,14,13,17,25,67,22]

data2 = []

target = 90.2


for i in range(1,len(data)+1):
    iter = itertools.combinations(data,i)
    # print iter
    for item in iter:
    	# print item
    	data2.append([item,abs(sum(item)-target)])

print len(data),len(data2)
result=data2[1]

for i in data2:
	# print i
	if i[1]<=result[1]:
		result = i

print result
