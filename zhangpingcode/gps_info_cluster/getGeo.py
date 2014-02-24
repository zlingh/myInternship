import urllib2
import json
import sys
import time

def getGeogg(lng, lat, key):
    try: 
        req = urllib2.Request("http://maps.google.com/maps/api/geocode/json?latlng="+lat+","+lng+"&sensor=false&language=zh-CN")
        opener = urllib2.build_opener()
        f = opener.open(req)
        addr = json.loads(f.read())
        # print f.read()
        return addr["results"][0]["formatted_address"].encode('UTF-8')
    except:
        print lat, lng
        return 'null'

def getGeoaly(lng, lat, key):
    try: 
        req = urllib2.Request("http://gc.ditu.aliyun.com/regeocoding?l="+lat+","+lng+"&type=111")        
        opener = urllib2.build_opener()
        f = opener.open(req)
        addr = json.loads(f.read())
        # print f.read()
        return addr["addrList"][0]["admName"].encode('UTF-8')+','+addr["addrList"][0]["name"].encode('UTF-8')+','+addr["addrList"][1]["name"].encode('UTF-8')+','+addr["addrList"][2]["name"].encode('UTF-8')
    except:
        print lat, lng
        return 'null'

def getGeobd(lng, lat, key):
    try: 
        req = urllib2.Request("http://api.map.baidu.com/geocoder?output=json&location="+lat+",%20"+lng+"&key="+key)
        opener = urllib2.build_opener()
        f = opener.open(req)
        addr = json.loads(f.read())
        # print f.read()
        return addr["result"]["business"].encode('UTF-8')+'\t'+addr["result"]["formatted_address"].encode('UTF-8')
    except:
        print lat, lng
        return 'null'

def getGeobdjson(lat, lng, key):
    try: 
        req = urllib2.Request("http://api.map.baidu.com/geocoder?output=json&location="+lat+",%20"+lng+"&key="+key)
        opener = urllib2.build_opener()
        f = opener.open(req)
        addr = json.loads(f.read())
        # print f.read()
        return json.dumps(addr["result"],ensure_ascii=False).encode('UTF-8')
    except:
        print lat, lng
        return 'null'


def getAllGeo(outf):
    keylist=['3abce7bdee5d581d2b3b5c618f001','3abd08580bfbd21988e4d7d42f2f','3ab6943780ff0610be956b10de879b','3abb7c90895ae73d7577b4654e5c3','3ab6904270ff010be956b10de879b','3ab9916cb5d3b25f9d58ae0ee3b4','3abdcfb4eb4e0d1262ee5d9809aa','3abe3f20ac6ba4976b722e5b9e4c1']
    outfi = open(outf, 'w')
    i=0
    key="1"
    xnum=200
    ynum=200
    left=39.68
    right=40.20
    bottom=116.08
    top=116.74
    stepx=(right-left)/xnum
    stepy=(top-bottom)/ynum
    for lat in [str(ix*stepx+left+stepx/2) for ix in range(xnum)]:
        for lng in [str(jx*stepy+bottom+stepy/2) for jx in range(ynum)]:
            i +=1
            if i<28500:
                continue
            if i%50==0:
                print i
                time.sleep(8)
            ti=(i/3)%8
             # print ti
            address =getGeobdjson(lat, lng, keylist[ti])
            outfi.write(lat+'\t'+lng+'\t'+address+'\n')
    outfi.close()

if __name__=='__main__':
    getAllGeo(sys.argv[1])
    #jso=getGeobdjson(sys.argv[1],sys.argv[2],sys.argv[3])
    #print jso
