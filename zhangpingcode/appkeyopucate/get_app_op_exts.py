#!/usr/bin/python
import sys
import datetime,time
from pymongo import Connection


def getMango(ym):    
    conn=Connection('10.18.10.41', 27018)
    print conn.alive()
    db=conn.op_production
    print db.collection_names()
    col = db.app_op_exts
    docs=col.find()
    print docs.count()
    wfile = open('/home/xiarong/appDB/data/app_op_exts_mangoDB_'+ym,'w')
    for k in docs:
        try:
            wfile.write(str(k).encode('utf-8')+'\n')
        except:
            print k
            continue
    wfile.close()

if __name__=='__main__':
    print("start:"+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    getMango(sys.argv[1])
    print("end:"+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
