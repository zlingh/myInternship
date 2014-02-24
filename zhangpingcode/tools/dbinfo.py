#!/usr/bin/python
import sys
import datetime,time
from pymongo import Connection
import json
def insertMango(ym):
    year=ym[:4]
    month=ym[4:]
    conn=Connection('10.18.10.41', 27018)
    print conn.alive()
    db=conn.op_production
    print db.collection_names()
#    col = db.monthly_stats
    col = db.marketinfos
#    col.remove({"year":"2013"})
    docs = col.find()
    count = docs.count()
    print count
    for k in docs:
        print k
        break

if __name__=='__main__':
    print("start:"+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    insertMango(sys.argv[1])
    print("end:"+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
