# test.py

# from impala.dbapi import connect
# conn = connect(host='10.0.0.228', port=21080)
# cursor = conn.cursor()
# cursor.execute('SELECT * FROM mytable LIMIT 100')
# print cursor.description # prints the result set's schema
# results = cursor.fetchall()



# from pyhive import presto
# cursor = presto.connect('10.0.0.228',21080).cursor()
# cursor.execute('SELECT * FROM my_awesome_data LIMIT 10')
# print cursor.fetchone()
# print cursor.fetchall()


import ibis

impala_host ='10.0.0.228'
impala_port = 21000

webhdfs_host = '10.0.0.227'
webhdfs_port = 50010

hdfs = ibis.hdfs_connect(host=webhdfs_host, port=webhdfs_port)
con = ibis.impala.connect(host=impala_host, port=impala_port,
                          hdfs_client=hdfs)