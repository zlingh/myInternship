#!/usr/bin/python
import sys
import datetime,time
from pymongo import Connection
from bson.objectid import ObjectId

def getMango():    
    conn=Connection('10.18.10.41', 27018)
    print conn.alive()
    db=conn.op_production
    print db.collection_names()
    #col = db.app_op_exts
    col = db.marketinfos
    obid= ['5130123f527015019e00001e','4ded91c2431fe33688000402']
#    obid= ObjectId('4e2562a9431fe3485b0002cd')
    docs=col.find({'appkey':obid[1]})
    print docs.count()
    for k in docs:
        try:
            print k
        except:
            print k
            continue

if __name__=='__main__':
    print("start:"+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    getMango()
    print("end:"+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
