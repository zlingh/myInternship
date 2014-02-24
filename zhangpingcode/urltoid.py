import sys
import re
from string import atoi
import os

def getAid(str1):
    reg1 = re.compile(r'[\D]*[\d]{9}')
    match = reg1.search(str1)
    if match:
        tmp = match.group()
        result = tmp[-9:]
    else:
        result = 'no'
    return result

urlf = open('ad_url.csv', 'r')
appurlid = open('ad_urlid', 'w')
for line in urlf:
    tmp = line.strip('\n').split('\t')
    if len(tmp)!=2:
        print line.strip('\n')
        continue
    appkey=tmp[0]
    str1 = tmp[1]
    aid = getAid(str1)
    if aid =='no':
        print line.strip('\n')
        continue
    appurlid.write(appkey+'\t'+aid+'\n')

appurlid.close()
