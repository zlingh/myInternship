#coding=utf8
#!/usr/bin/env python
"""
# Author: zhangping@umeng.com
# company: umeng
# Created Time : Wed May 29 10:45:45 2013
# File Name: getkerInfo.py
# Description:get the appkey, installNum, description, os, two name, two category

"""
import json
import os
import datetime, time
from bson.objectid import ObjectId
appf=open('../data/app_op_exts_mangoDB_20130614','r')
kerInfof=open('../data/appFound_201306','w')
iosnof = open('../data/iosNotFoud_201306','w')
andnof = open('../data/androidNotFound_201306','w')
#find the appkey not have aid or package_name in op app
for line in appf:
    appdt={}
    #k=json.loads(line)
    k=eval(line)
    if 'app_id' not in k or 'dau' not in k:
        continue
    if 'name' not in k or k['name']==[]:
        appdt['name']='unknoname'
    else:
        appdt['name']=k['name']
    appdt["app_key"]=str(k['app_id'])
    if appdt['app_key']=='4e2562a9431fe3485b0002cd':
        print k
    appdt["dau"]=k['dau']
    if 'platform' not in k:
        #print k
        continue
    appdt["os"]=k["platform"]
    if appdt["os"]=='android':
        if 'package_name' not in k:
            appdt['patch']='unknow'
        else:
            appdt['patch']=k['package_name']
    if appdt["os"]=='iphone' or appdt['os']=='ipad':
        if 'aid' not in k:
            appdt['patch']='unknow'
        else:
            appdt['patch']=k['aid']
    if appdt['os']!='android' and appdt['os']!='iphone':
        #print appdt['os']
        continue
    if appdt['os']=='android' and appdt['patch']=='unknow':
        andnof.write(appdt["app_key"].encode('utf-8')+'\t'+str(appdt["dau"])+'\t'+appdt["os"].encode('utf-8')+'\t'+str(appdt['patch']).encode('utf-8')+'\t'+appdt['name'].encode('utf-8')+'\n')
    if (appdt['os']=='iphone' or appdt['os']=='ipad')and appdt['patch']=='unknow':
        iosnof.write(appdt["app_key"].encode('utf-8')+'\t'+str(appdt["dau"])+'\t'+appdt["os"].encode('utf-8')+'\t'+str(appdt['patch']).encode('utf-8')+'\t'+appdt['name'].encode('utf-8')+'\n')


    kerInfof.write(appdt["app_key"].encode('utf-8')+'\t'+str(appdt["dau"])+'\t'+appdt["os"].encode('utf-8')+'\t'+str(appdt['patch']).encode('utf-8')+'\t'+appdt['name'].encode('utf-8')+'\n')
kerInfof.close()
