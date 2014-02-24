@outputSchema("word:chararray")
def helloworld():  
    return hk()
def hk():
    return "hello"

@outputSchema("word:chararray,num:long")
def complex(word):
    return str(word),len(word)

@outputSchemaFunction("squareSchema")
def square(num):
    return ((num)*(num))

@schemaFunction("squareSchema")
def squareSchema(input):
    return input

# No decorator - bytearray
def concat(str):
    return str+str

#######################
 # Data Type Functions #
 #######################
 #collectBag- collect elements of a bag into other bag
 #This is useful UDF after group operation
@outputSchema("y:bag{t:tuple(len:int,word:chararray)}") 
def collectBag(bag):
    outBag = []
    for word in bag:
        tup=(len(bag), word[1])
        outBag.append(tup)
    return outBag

@outputSchema("y:bag{t:tuple(id:chararray, gpsNum:long)}") 
def clust(bag):
    outBag = []
    tup=(bag[0][0], len(bag))
    outBag.append(tup)
    return outBag

@outputSchema("y:bag{t:tuple(m:int,n:int)}")
def testbg(bag):
    outBag =[]
    for word in bag:
        tup=(len(bag), int(word[1]))
        outBag.append(tup)
    return outBag

@outputSchema("y:bag{info:tuple(lng:float, lat:float, time:long)}")
def bjbag(bag):
    outBag=[]
    for w in bag:
        if w[2]>116.08 and w[2]<116.74 and w[3]>39.68 and w[3]<40.20:
            tup=(w[2],w[3],w[4])
            outBag.append(tup)
    return outBag

@outputSchema("bj:chararray")
def hasbj(bag):
    result='n'
    for w in bag:
        lng=w[2]
        lat=w[3]
        if lng>116.08 and lng<116.74 and lat>39.68 and lat<40.20:
            result='y'
            break
    return result

@outputSchema("date:int")
def getDate(num):
    return int(time.strftime('%Y%m%d',time.localtime(num/1000)))#ms

@outputSchema("timestamp:long)
def getTimestamp(t):
    nt = time.strptime( t, "%Y-%m-%d" )
    return time.mktime(datetime.datetime(*nt[:6]).timetuple())#s

@outputSchema("day:int")
def getTimestamp(t1,t2,num):
    nt1 = time.strptime(t1, "%Y-%m-%d")
    nt2 = time.strptime(t2, "%Y-%m-%d")
    s1= long(time.mktime(datetime.datetime(*nt1[:6]).timetuple()))
    s2= long(time.mktime(datetime.datetime(*nt2[:6]).timetuple()))
    s=(s2-s1)/86400
    c = int(num)
    if s>c:
        return c
    if s<0:
        return 0
    return s


@outputSchema("regin:chararray")
def getRegin(lat,lng):
    if lat<39.9412 and lat>39.9269 and lng<116.4616 and lng>116.444:
        return 'sanlitun'
    elif lat<39.9197 and lat>39.904 and lng< 116.4696 and lng>116.4507:
        return 'guomao'
    elif lat<40.05975 and lat>40.04627 and lng<116.31480 and lng>116.29718:
        return 'xierqi'
    elif lat<39.92005 and lat>39.90656 and lng<116.41989 and lng>116.40228:
        return 'wangfujin'
    elif lat<39.95640 and lat>39.94301 and lng<116.34951 and lng>116.33194:
        return 'beijiao'
    else:
        return 'other'




