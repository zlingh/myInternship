import urllib2
import json
import sys
import time

def getGeo(lng, lat, key):
    try: 
        req = urllib2.Request("http://api.map.baidu.com/geocoder?output=json&location="+lat+",%20"+lng+"&key="+key)
        opener = urllib2.build_opener()
        f = opener.open(req)
        addr = json.loads(f.read())
        return addr["result"]["business"].encode('UTF-8')+'\t'+addr["result"]["formatted_address"].encode('UTF-8')
    except:
        print lat, lng
        return 'null'

def getAllGeo(filename,outf):
    keylist=['9916cbcb365b5d3b252f9d58ae0ee3b4','dcfb4e0b42a19e806d1262ee5d9809aa','e9e3f20a4c6ba1482976b722e5b9e4c1']
    ifile = open(filename,'r')
    outfi = open(outf, 'w')
    i=0
    for line in ifile:
        i +=1
        if i==100:
            break
        if i%100 ==1:
            time.sleep(0.01)
        l = line.strip('\n').split('\t')
        address =getGeo(l[0], l[1], keylist[i%3])
        outfi.write(address+'\t'+l[0]+'\t'+l[1]+'\t'+l[2]+'\t'+l[3]+'\n')
    outfi.close()

if __name__=='__main__':
    getAllGeo(sys.argv[1],sys.argv[2])
