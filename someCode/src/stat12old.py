from string import atoi
import sys
import os
def profun(profile, osfile):
    rfp = open(profile, 'r')
    osfp = open(osfile, 'r')
    if not os.path.isdir('proaccessout'):
        os.mkdir('proaccessout')
    iosprofile = open ('proaccessout/iospro','w')
    andprofile = open ('proaccessout/andpro','w')
    iosaccessfile = open('proaccessout/iosaccess','w')
    andaccessfile = open('proaccessout/andaccess', 'w')
    wpprofile = open('proaccessout/wppro', 'w')
    wpaccessfile = open('proaccessout/wpaccess', 'w')
    iosdt ={}
    wpdt = {}
    iospro = {}
    andpro = {}
    wppro = {}
    iosaccess = {}
    andaccess = {}
    wpaccess = {}
    
    for line in osfp:#add the os info to dict dt
        tmp = line.strip('\n').split('\t')
        model1 =tmp[2].lower().replace(" ", "")
        os1 =tmp[0].lower().replace(" ", "")
        if len(tmp) <4:
            continue
        if os1 == 'windowsphone':
            wpdt[model1] =1
        if ((os1 == 'ios') or (os1 == 'iphoneos')):
            iosdt[model1] =1

    for line in rfp:
        tmp = line.strip().split('\t')
        if len(tmp)!=5:
            continue
        pro = tmp[0]
        model = tmp[1].lower().replace(" ", "")
        acc = tmp[2]
        num = atoi(tmp[4])        
        os2 = 'null'
       
        if model in iosdt:
            os2 = 'ios' #iphoneos ,ios
        elif model in wpdt:
            os2 = 'windowsphone'
        else:
            os2 = 'android'

        if os2 == 'android':#compute android
            andaccess[acc] = andaccess.get(acc, 0) +num
            andpro[pro] = andpro.get(pro, 0) +num
        elif os2 == 'windowsphone':
            wpaccess[acc] = wpaccess.get(acc, 0) +num
            wppro[pro] = wppro.get(pro, 0) +num
        else:
            iosaccess[acc] = iosaccess.get(acc, 0) +num
            iospro[pro] = iospro.get(pro, 0) +num
    
    for k,v in andaccess.items():
        andaccessfile.write(k+'\t'+str(v)+'\n')
    for k,v in andpro.items():
        andprofile.write(k+'\t' + str(v) +'\n')
    
    for k,v in iosaccess.items():
        iosaccessfile.write(k +'\t' +str(v) +'\n')
    for k,v in iospro.items():
        iosprofile.write(k +'\t' +str(v) +'\n')

    for k,v in wpaccess.items():
        wpaccessfile.write(k +'\t' +str(v) +'\n')
    for k,v in wppro.items():
        wpprofile.write(k +'\t' +str(v) +'\n')

if __name__ =='__main__':
    profun(sys.argv[1], sys.argv[2])#input the province file and os file

