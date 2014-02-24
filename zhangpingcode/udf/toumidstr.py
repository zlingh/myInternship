#!/usr/bin/env python

import sys
import json
import string
import md5
# input comes from STDIN (standard input)

for line in sys.stdin:
    try:
        EMPTY_MD5="d41d8cd98f00b204e9800998ecf8427e"
        EMPTY_UMID="d41d8cd98f0b24e980998ecf8427e"
        line = line.strip()
        tmp = line.split('\t')
        if tmp[1]!='':
            #print '%s\t%s\t%s' %(tmp[0],tmp[1],tmp[1])
            res=tmp[1]
        elif tmp[0]==''or tmp[0]=='unkonown':
            print '%s\t%s\t%s' %(tmp[0],tmp[1],EMPTY_UMID)
            continue
        else:
            res=md5.new(tmp[0].encode('utf-8')).hexdigest().lower()
        if len(res)<32:
            usr=res 
        else:
            i=0 
            nres=[]
            for e in res:
                if i%2  == 0:
                    if e != '0':
                        nres.append(e)
                else:
                    nres.append(e)
                i+=1
            usr= ''.join(nres)
        print '%s\t%s\t%s' % (tmp[0],tmp[1],usr)
    except Exception:
        continue

