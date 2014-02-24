#coding=utf8
#!/usr/bin/env python
"""
# Author: zhangping@umeng.com
# company: umeng
# Created Time : Wed May 29 10:45:45 2013
# File Name: getkerInfo.py
# Description:get the appkey, installNum, description, os, two name, two category

"""
import sys
import json
import datetime, time
from bson.objectid import ObjectId
appf=open('/home/xiarong/appDB/data/app_op_exts_mangoDB_'+sys.argv[1],'r')
kerInfof=open('/home/xiarong/appDB/data/appkey_opcate_'+sys.argv[1],'w')
appdt={}
osdt={'iphone':'ios','android':'android','ipad':'ios','wphone':'windowsphone'}
for line in appf:
    k=eval(line)
    if 'app_id' not in k or 'op_category' not in k :
        continue
    appdt["app_key"]=str(k['app_id'])
    appdt['op_category']=k['op_category']
    appdt['name']=k['name']
    appdt['dau']=k['dau']
    if 'platform' not in k:
        continue
    else:
        if k['platform'] not in osdt:
            continue
        else:
            appdt['os']=osdt[k['platform']]
    if 'name_on_market' not in k or k['name_on_market']==[] or len(k['name_on_market'])==0:
        appdt['marketname']='unknowMktName'
    else:
        appdt['marketname']=k['name_on_market']
    kerInfof.write(appdt["app_key"].encode('utf-8')+'\t'+appdt['op_category'].encode('utf-8')+'\t'+appdt['name'].encode('utf-8')+'\t'+appdt['marketname'].encode('utf-8')+'\t'+str(appdt["dau"])+'\t'+appdt["os"].encode('utf-8')+'\n')
kerInfof.close()


