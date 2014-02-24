
pridt={}
pricef = open('price_history.csv', 'r')
for line in pricef:
    tmp=line.strip('\n').split('\t')
    modelid=int(tmp[1])
    price=int(tmp[2])
    uptime = int(tmp[3])
    if modelid not in pridt:
        pridt[modelid]=[price,uptime]
    elif (pridt[modelid][1]<uptime and price>0) or (pridt[modelid][1]<0 and price>0):
        pridt[modelid]=[price,uptime]

modelpf = open('modelprice.csv', 'w')        
modelf = open('mobilephonemapping.csv', 'r')
for line in modelf:
    tmp = line.strip('\n').split('\t')
    modelid=int(tmp[5])
    devicename= tmp[1]
    if modelid in pridt:
        modelpf.write(devicename+'\t'+str(pridt[modelid][0])+'\n')
