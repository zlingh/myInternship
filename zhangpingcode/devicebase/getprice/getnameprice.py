
pridt={}
pricef = open('pad_price_history201305.csv', 'r')
for line in pricef:
    tmp=line.strip('\n').split('\t')
    modelid=int(tmp[1])
    price=int(tmp[2])
    uptime = int(tmp[3])
    if modelid not in pridt:
        pridt[modelid]=[price,uptime]
    elif (price>0 and (pridt[modelid][1]<uptime or pridt[modelid][0]<0)):
        pridt[modelid]=[price,uptime]

modelpf = open('pad_nameprice201305.csv', 'w')        
modelf = open('pad201305.csv', 'r')
for line in modelf:
    tmp = line.strip('\n').split('\t')
    modelid=int(tmp[0])
    devicename= tmp[1]
    namepinyin=tmp[2]
    brand=tmp[3]
    if modelid in pridt and pridt[modelid][0]>0:
        modelpf.write(str(modelid)+'\t'+devicename+'\t'+namepinyin+'\t'+brand+'\t'+str(pridt[modelid][0])+'\n')
