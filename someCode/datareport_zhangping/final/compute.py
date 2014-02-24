
import sys
import re
from string import atoi
import os

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

def getdevicels(osfile):
    osfp = open(osfile, 'r')
    iosdev = open ('iosdevice','w')
    wpdev = open ('wpdevice', 'w')
    iosdt ={}
    wpdt = {}    
    for line in osfp:#add the os info to dict dt
        tmp = line.strip('\n').split('\t')
        if len(tmp) !=6:
            continue 
        model1 =tmp[2].lower().replace(" ", "")
        os1 =tmp[0].lower().replace(" ", "")
        if ((os1 == '') or (model1 =='')):
            continue
        if os1 == 'windowsphone':
            wpdt[model1] =1
        if ((os1 == 'ios') or (os1 == 'iphoneos')):
            iosdt[model1] =1
    for k in iosdt:
        iosdev.write(k+'\n')
    for j in wpdt:
        wpdev.write(j +'\n')
    iosdev.close()
    wpdev.close()

def provAccessVer(profile):#get province ,access, osversion report
    rfp = open(profile, 'r')
    iosdevice = open ('iosdevice', 'r')
    wpdevice = open('wpdevice', 'r')
    if not os.path.isdir('dataout'):
        os.mkdir('dataout')
    iosprofile = open ('dataout/IOS_province_Distribution','w')
    andprofile = open ('dataout/Android_province_Distribution','w')
    iosaccessfile = open('dataout/IOS_access_Distribution','w')
    andaccessfile = open('dataout/Android_access_Distribution', 'w')
    wpprofile = open('dataout/Windowsphone_province_Distribution', 'w')
    wpaccessfile = open('dataout/Windowsphone_access_Distribution', 'w')
    iosverfile = open('dataout/IOS_osversion_Distribution','w')
    andverfile = open('dataout/Android_osversion_Distribution','w')
    wpverfile = open('dataout/Windowsphone_osversion_Distribution','w')
    iosdt ={}
    wpdt = {}
    iospro = {}
    andpro = {}
    wppro = {}
    iosaccess = {}
    andaccess = {}
    wpaccess = {}
    andver ={}
    iosver ={}
    wpver ={}

    for line in iosdevice:
        tmp =line.strip('\n').split('\t')
        if len(tmp)!=1:
            continue
        model1 =tmp[0].lower().replace(" ","")
        iosdt[model1] =1

    for line in wpdevice:
        tmp =line.strip('\n').split('\t')
        if len(tmp)!=1:
            continue
        model1 =tmp[0].lower().replace(" ","")
        wpdt[model1] =1
       
    for line in rfp:
        tmp = line.strip().split('\t')
        if len(tmp)!=7:
            continue
        version = getVersion(tmp[0].lower().replace(" ",""))
        pro = tmp[1]
        model = tmp[2].lower().replace(" ", "")
        acc = tmp[3]+ '\t' +tmp[4]
        modelNum =atoi(tmp[5])
        num = atoi(tmp[6])        
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
            andver[version] =andver.get(version, 0) +modelNum
        elif os2 == 'windowsphone':
            wpaccess[acc] = wpaccess.get(acc, 0) +num
            wppro[pro] = wppro.get(pro, 0) +num
            wpver[version] =wpver.get(version, 0) +modelNum
        else:
            iosaccess[acc] = iosaccess.get(acc, 0) +num
            iospro[pro] = iospro.get(pro, 0) +num
            iosver[version] =iosver.get(version, 0) +modelNum
    for k,v in andaccess.items():
        andaccessfile.write(k+'\t'+str(v)+'\n')
    for k,v in andpro.items():
        andprofile.write(k+'\t' + str(v) +'\n')
    for k,v in andver.items():
        andverfile.write(k+'\t' + str(v) +'\n')
    
    for k,v in iosaccess.items():
        iosaccessfile.write(k +'\t' +str(v) +'\n')
    for k,v in iospro.items():
        iosprofile.write(k +'\t' +str(v) +'\n')
    for k,v in iosver.items():
        iosverfile.write(k+'\t' + str(v) +'\n')

    for k,v in wpaccess.items():
        wpaccessfile.write(k +'\t' +str(v) +'\n')
    for k,v in wppro.items():
        wpprofile.write(k +'\t' +str(v) +'\n')
    for k,v in wpver.items():
        wpverfile.write(k+'\t' + str(v) +'\n')
    iosaccessfile.close()
    iosprofile.close()
    iosverfile.close()
    andaccessfile.close()
    andprofile.close()   
    andverfile.close() 
    wpaccessfile.close()
    wpprofile.close()
    wpverfile.close()

def provAccessVer2(profile):#get province ,access, osversion report
    rfp = open(profile, 'r')
    iosdevice = open ('iosdevice', 'r')
    wpdevice = open('wpdevice', 'r')
    if not os.path.isdir('dataout'):
        os.mkdir('dataout')
    iosprofile = open ('dataout/IOS_province_Distribution','w')
    andprofile = open ('dataout/Android_province_Distribution','w')
    iosaccessfile = open('dataout/IOS_access_Distribution','w')
    andaccessfile = open('dataout/Android_access_Distribution', 'w')
    wpprofile = open('dataout/Windowsphone_province_Distribution', 'w')
    wpaccessfile = open('dataout/Windowsphone_access_Distribution', 'w')
    iosverfile = open('dataout/IOS_osversion_Distribution','w')
    andverfile = open('dataout/Android_osversion_Distribution','w')
    wpverfile = open('dataout/Windowsphone_osversion_Distribution','w')
    iosdt ={}
    wpdt = {}
    iospro = {}
    andpro = {}
    wppro = {}
    iosaccess = {}
    andaccess = {}
    wpaccess = {}
    andver ={}
    iosver ={}
    wpver ={}

    for line in iosdevice:
        tmp =line.strip('\n').split('\t')
        if len(tmp)!=1:
            continue
        model1 =tmp[0].lower().replace(" ","")
        iosdt[model1] =1

    for line in wpdevice:
        tmp =line.strip('\n').split('\t')
        if len(tmp)!=1:
            continue
        model1 =tmp[0].lower().replace(" ","")
        wpdt[model1] =1
       
    for line in rfp:
        tmp = line.strip().split('\t')
        if len(tmp)!=5:
            continue
        #version = getVersion(tmp[0].lower().replace(" ",""))
        version ='4.1'
        pro = tmp[0]
        model = tmp[1].lower().replace(" ", "")
        acc = tmp[2]+ '\t' +tmp[3]
        modelNum =0
        #modelNum =atoi(tmp[5])
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
            andver[version] =andver.get(version, 0) +modelNum
        elif os2 == 'windowsphone':
            wpaccess[acc] = wpaccess.get(acc, 0) +num
            wppro[pro] = wppro.get(pro, 0) +num
            wpver[version] =wpver.get(version, 0) +modelNum
        else:
            iosaccess[acc] = iosaccess.get(acc, 0) +num
            iospro[pro] = iospro.get(pro, 0) +num
            iosver[version] =iosver.get(version, 0) +modelNum
    for k,v in andaccess.items():
        andaccessfile.write(k+'\t'+str(v)+'\n')
    for k,v in andpro.items():
        andprofile.write(k+'\t' + str(v) +'\n')
    for k,v in andver.items():
        andverfile.write(k+'\t' + str(v) +'\n')
    
    for k,v in iosaccess.items():
        iosaccessfile.write(k +'\t' +str(v) +'\n')
    for k,v in iospro.items():
        iosprofile.write(k +'\t' +str(v) +'\n')
    for k,v in iosver.items():
        iosverfile.write(k+'\t' + str(v) +'\n')

    for k,v in wpaccess.items():
        wpaccessfile.write(k +'\t' +str(v) +'\n')
    for k,v in wppro.items():
        wpprofile.write(k +'\t' +str(v) +'\n')
    for k,v in wpver.items():
        wpverfile.write(k+'\t' + str(v) +'\n')
    iosaccessfile.close()
    iosprofile.close()
    iosverfile.close()
    andaccessfile.close()
    andprofile.close()   
    andverfile.close() 
    wpaccessfile.close()
    wpprofile.close()
    wpverfile.close()

def jailfun(infile):#get the ios jail distribution report
    infil =open(infile, 'r')
    if not os.path.isdir('dataout'):
        os.mkdir('dataout')
    jailfil =open("dataout/IOS_jailbreak_distribution", 'w')
    jailmodelfil =open("dataout/IOS_jailbreak_model_Distribution", 'w')
    jailosverfil =open("dataout/IOS_jailbreak_osversion_Distribution", 'w')
    jaildt ={}
    jailModel ={}
    jailOsver ={}
    for line in infil:
        tmp =line.strip('\n').split('\t')
        if len(tmp) !=6:
            continue
        os1 =tmp[0].lower().replace(" ","")
        if (os1 !='ios') and (os1 !='iphoneos'):
            continue
        jail =tmp[3].lower().replace(" ","")
        model =tmp[2].lower().replace(" ","")
        version =getVersion(tmp[1].lower().replace(" ",""))
        jail_model =jail +'\t' +model
        jail_version =jail +'\t' +version
        num =atoi(tmp[5])
        jaildt[jail] =jaildt.get(jail, 0) +num
        jailModel[jail_model] =jailModel.get(jail_model, 0) +num
        jailOsver[jail_version] =jailOsver.get(jail_version, 0)+num
    for k in jaildt:
        jailfil.write(k +'\t' +str(jaildt[k])+'\n')
    for k in jailModel:
        jailmodelfil.write(k +'\t' +str(jailModel[k]) +'\n')
    for k in jailOsver:
        jailosverfil.write(k +'\t' +str(jailOsver[k]) +'\n')
    jailfil.close()
    jailmodelfil.close()
    jailosverfil.close()



def modelResfun(modelResData):# get the model , resolution report
    iosdevice = open ('iosdevice', 'r')
    wpdevice = open('wpdevice', 'r')
    datafil = open (modelResData, 'r')
    if not os.path.isdir('dataout'):
        os.mkdir('dataout')
    andModelfil = open("dataout/Android_model_Distribution",'w')
    andResofil = open("dataout/Android_resolution_Distribution",'w')
    iosModelfil = open("dataout/IOS_model_Distribution",'w')
    iosResofil = open("dataout/IOS_resolution_Distribution",'w')    
    wpModelfil = open("dataout/Windowsphone_model_Distribution",'w')
    wpResofil = open("dataout/Windowsphone_resolution_Distribution",'w')    
    wpdt ={}
    iosdt ={}
    andModeldt ={}
    andResodt ={}
    iosModeldt ={}
    iosResodt ={}
    wpModeldt ={}
    wpResodt ={} 
    for line in iosdevice:
        tmp =line.strip('\n').split('\t')
        if len(tmp)!=1:
            continue
        model1 =tmp[0].lower().replace(" ","")
        iosdt[model1] =1

    for line in wpdevice:
        tmp =line.strip('\n').split('\t')
        if len(tmp)!=1:
            continue
        model1 =tmp[0].lower().replace(" ","")
        wpdt[model1] =1
   
    for line in datafil:
        tmp = line.strip('\n').split('\t')
        if len(tmp)!=5:
            continue
        model = tmp[0].lower().replace(" ","")
        reso =tmp[1].lower().replace(" ","")
        os1 = 'null'
        modelNum = atoi(tmp[3])
        if model in iosdt:
            os1 ='ios'
        elif model in wpdt:
            os1 ='windowsphone'
        else:
            os1 ='android'
            
        if os1 == 'ios':
            iosModeldt[model] = iosModeldt.get(model, 0)+modelNum
            iosResodt[reso] = iosResodt.get(reso, 0) +modelNum
        if os1 == 'windowsphone':
            wpModeldt[model] = wpModeldt.get(model, 0)+modelNum
            wpResodt[reso] = wpResodt.get(reso, 0) +modelNum      
        if os1 == 'android':
            andModeldt[model] = andModeldt.get(model, 0)+modelNum
            andResodt[reso] = andResodt.get(reso, 0) +modelNum                       
            
    for k,v in iosModeldt.items():
        iosModelfil.write(k +'\t' +str(v)+ '\n')
    for k,v in iosResodt.items():
        iosResofil.write(k +'\t' +str(v) +'\n')
        
    for k,v in andModeldt.items():
        andModelfil.write(k +'\t' +str(v)+ '\n')
    for k,v in andResodt.items():
        andResofil.write(k +'\t' +str(v) +'\n')
        
    for k,v in wpModeldt.items():
        wpModelfil.write(k +'\t' +str(v)+ '\n')
    for k,v in wpResodt.items():
        wpResofil.write(k +'\t' +str(v) +'\n')
                      
    iosModelfil.close()
    iosResofil.close()
    andModelfil.close()
    andResofil.close()
    wpModelfil.close()
    wpResofil.close()           


if __name__=='__main__':
    model_reso = sys.argv[1] #the file from a moth's dlilog, modelreso. #model ,reso ,flag, modelNum, laucnchNum
    pro_acc_osv =sys.argv[2] #the file from 6days' dlilog,verprovacc #os_version ,pro, model ,access, subtype, modelNum, launchNum
    os_model =sys.argv[3]# the file from the last of rawlog, osmodeljail. #os, os_version, model ,jailbreak, flag, modelNum
    getdevicels(os_model)
    provAccessVer(pro_acc_osv)
    modelResfun(model_reso)
    jailfun(os_model)
    
    
    
#input the two file iosdevice and wpdevice file at the same directory,argv[1]:input the raw file,sys.argv[2]:the out file to pig
