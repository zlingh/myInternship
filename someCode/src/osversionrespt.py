#use this to get the province and access distribution

from string import atoi
import sys
import os
import re

def getVersion(version):
    result = version
    reg1 = re.compile(r'android[\.]?[\d]+\.[\d]+')
    match = reg1.search(version)
    if match:
        result = match.group()
        version = result

    reg2 = re.compile(r'[\d]+\.[\d]+')
    match = reg2.search(version)
    if match:
        result = match.group()
    return result

def profun(osfile, profile):
    rfp = open(profile, 'r')
    osfp = open(osfile, 'r')
    if not os.path.isdir('osversion_dis'):
        os.mkdir('osversion_dis')
    iosverfile = open ('osversion_dis/iosversion','w')
    andverfile = open ('osversion_dis/andversion','w')
    wpverfile = open('osversion_dis/wpversion', 'w')
#    iosdev = open ('iosdevice10','w')
#    wpdev = open ('wpdevice10', 'w')
    iosdt ={}
    wpdt = {}
    iosver = {}
    andver = {}
    wpver = {}
    
    for line in osfp:#add the os info to dict dt
        tmp = line.strip('\n').split('\t')
        model1 =tmp[2].lower().replace(" ", "")
        os1 =tmp[0].lower().replace(" ", "")
        if ((len(tmp) !=8) or (os1 == '') or (model1 =='')):
            continue
        if os1 == 'windowsphone':
            wpdt[model1] =1
        if ((os1 == 'ios') or (os1 == 'iphoneos')):
            iosdt[model1] =1
#    for k in iosdt:
#        iosdev.write(k+'\n')
#    for j in wpdt:
#        wpdev.write(j +'\n')
    for line in rfp:
        tmp = line.strip().split('\t')
        if len(tmp)!=7:
            continue
        version = getVersion(tmp[1].lower().replace(" ",""))
        model = tmp[0].lower().replace(" ", "")
        num = atoi(tmp[5])        
        os2 = 'null'
       
        if model in iosdt:
            os2 = 'ios' #iphoneos ,ios
        elif model in wpdt:
            os2 = 'windowsphone'
        else:
            os2 = 'android'

        if os2 == 'android':#compute android
            andver[version] = andver.get(version, 0) +num
        elif os2 == 'windowsphone':
            wpver[version] = wpver.get(version, 0) +num
        else:
            iosver[version] = iosver.get(version, 0) +num
    
    for k,v in andver.items():
        andverfile.write(k+'\t'+str(v)+'\n')
    
    for k,v in iosver.items():
        iosverfile.write(k +'\t' +str(v) +'\n')

    for k,v in wpver.items():
        wpverfile.write(k +'\t' +str(v) +'\n')

if __name__ =='__main__':
    profun(sys.argv[1], sys.argv[2])#input the os file and  province file

