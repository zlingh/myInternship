

#we donot use getversion,verRes,don't add * between height,width.because the input raw file just have
#model, resolution, flag, id, launches
import sys
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

#modify the os_version,add * between resolution
def verRes(line):
        l = line.split('\t')
        l[1] = getVersion(l[1])
        s = l[0]
        if len(l) <6:#if len<6 that mean cannot find resolution field,so we print it to view the problem
            print l
        else:
            #add * between height and width ,let the biger show first
            tmp = l[4] 
            #if cmp(l[4], l[5]) <0:
#            try: 
#                if int(l[4]) <int(l[5]):
#                    l[4] =l[5]
#                    l[5] =tmp     
#            except:#if cannot change to int ,print it
#                 print l[4]+'\t'+l[5] 
            for i in range(1,5):
                s +='\t'+l[i].strip('\n')
            if l[4]!='':
                s += '*'+ l[5]
            else:#if resolution field is null,don't add * 
                s +=l[5]
            for j in range(6,len(l)):
                s +='\t'+l[j].strip('\n')
        return s


#fun is the main function ,it calls verRes( modify the os_version,add * between resolution) and add os to data 
def fun(osfile, data, out):
    fp1 = open (osfile, 'r')
    fp2 = open (data, 'r')
    fpout = open (out, 'w')
    wpdt ={}
    iosdt ={}
    dt = {}
    dt2 = {} #use to compute the data file
#    for line in fp1:#add the os info to dict dt
#        tmp = line.strip('\n').split('\t')
#        model1 =tmp[2].lower().replace(" ", "")
#        if len(tmp)<4:
#            continue
#        if model1 not in dt:
#            dt[model1]=[tmp[0], tmp[3]]#tmp[2] is model,tmp[0] and tmp[3] is os and cpu
#
    for line in fp1:#add the os info to dict dt
        tmp = line.strip('\n').split('\t')
        model1 =tmp[2].lower().replace(" ", "")
        os1 =tmp[0].lower().replace(" ", "")
        if ((len(tmp) <5) or (os1 == '') or (model1 =='')):#8
            continue
        if os1 == 'windowsphone':
            wpdt[model1] =1
        if ((os1 == 'ios') or (os1 == 'iphoneos')):
            iosdt[model1] =1
#            print model1

   
    for line in fp2:
         tmp = line.strip().split('\t')
         if len(tmp)!=5:
             continue
#         if int(tmp[2]) < int(tmp[3]):
#             swapn = tmp[2]
#             tmp[2] = tmp[3]
#             tmp[3] = swapn
                                                
         key1 = tmp[0]+'\t'+tmp[1]#let model  height*width be the key
         v = [0, 0]#value is idnums and launchnums,if the key is the same,sum them
         if key1 not in dt2:
             v[0] = int(tmp[3])
             v[1] = int(tmp[4])
         else:
             v1= dt2[key1]
             v[0] = int(tmp[3])+ v1[0]
             v[1] = int(tmp[4]) + v1[1]
         dt2[key1] = v
    for key2 in dt2:#bianli data and add os,cpu from dt
        tmp = key2.strip().split('\t')
       # s =tmp[0] +'\t'+ dt.get(tmp[0].lower(),'\t')
#        if len(tmp)<7:
#            continue

#            s =tmp[0]
#            s=verRes(s)
#            fpout.write(s+'\n')
#            continue
#
        value = dt2[key2]
        model = tmp[0].lower().replace(" ", "")
        resolution =tmp[1]
        if model in iosdt:
            os = 'ios'
            cpu = 'unknowcpu'
        elif model in wpdt:
            os = 'windowsphone'
            cpu = 'unknowcpu'
        else:
            os ='android'
            cpu = 'unknowcpu'
      
        
        s = os+ '\t'+ model+ '\t'+ cpu+'\t'+resolution+'\t'+str(value[0]).strip('\n')+'\t'+str(value[1]).strip('\n')
#        for i in range(len(value)):
#            s +='\t'+tmp[i].strip('\n')
#        s=verRes(s)
        fpout.write(s+'\n')


if __name__=='__main__':
    fun(sys.argv[1], sys.argv[2], sys.argv[3])
#argv[1]:input the file with os,argv[2]:input the raw file,sys.argv[3]:the out file to pig
