#!/usr/bin/env python

import MySQLdb
import datetime

dbh = MySQLdb.connect(host="localhost", user="root", passwd="", db="test")

time=datetime.datetime.now().time()
print time
print "Connection succeed"
cur = dbh.cursor()
rows = (('jjvein', 23, 1, time), ('jjvein', 23, 1, time), ('jjvein', 23, 1, time))
query = 'insert into test values (null, %s, %s, %s, %s)'
for i in rows:
    cur.execute(query, i)
    
dbh.commit()
dbh.close()
print "Insert Success"

