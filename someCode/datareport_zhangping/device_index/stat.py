from string import atoi
dfp = open('ios_device', 'r')
rfp = open('nov_res','r')

ios ={}

iospro = {}
andpro = {}
iosaccess = {}
andaccess = {}

for line in dfp:
    ios[line.strip()]=1

for line in rfp:
    
    tmp = line.strip().split('\t')
    if len(tmp)!=4:
        continue
    pro = tmp[0]
    os = 'null'
    acc = tmp[2]
    num = atoi(tmp[3])
   
    if tmp[1] in ios:
        os = 'iOS'
        if acc not in iosaccess:
            iosaccess[acc]=0
        iosaccess[acc]+=num
        if pro not in iospro:
            iospro[pro]=0
        iospro[pro]+=num
    else:
        os = 'Android'
        if acc not in andaccess:
            andaccess[acc]=0
        andaccess[acc]+=num
        if pro not in andpro:
            andpro[pro]=0
        andpro[pro]+=num

for k,v in andaccess.items():
    print k+'\t'+str(v)

