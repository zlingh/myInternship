#coding=utf8
#!/usr/bin/env python
"""
# Author: zhangping@umeng.com
# Created Time : Fri Jun 14 13:21:56 2013
# File Name: active_eval.py
# Description:

"""
acf = open('../Android/data/androidAppInfo_201306','r')
nof = open('../data/appFound_201306xu','r')
dpf = open('../Android/data/appkey_packname_201306','r')
#nof = open('../data/androidNotFound_201306','r')
outf = open('../data/activ_eval2','w')
appdt={}
appdtdp={}
for line in dpf:
    tmp=line.strip('\n').split('\t')
    appdtdp[tmp[0]]=1
for line in acf:
    k=eval(line)
    appkey=k['appkey']
    name=k['name']
    packname=k['package_name']
    appdt[appkey]=1
i=0
for line in nof:
    tmp = line.strip('\n').split('\t')
    if tmp[2]!='android':
        continue
    i+=1
    if i>1000:
        break
    if tmp[0] not in appdtdp:
        print line.strip()

