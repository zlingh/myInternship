# Author: HongYihong, zhangping
# Description: parse the log 
######################################################
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
        if len(l) <2: 
            print l[0]                      
            return l[0]
        l[1] = getVersion(l[1])
        s = l[0]
        if len(l) <6:
            print l
            for i in range(1,len(l)):
                s +='\t'+l[i].strip('\n')
        else:
            #add * between height and width ,let the biger show first
#            tmp = l[4] 
#            #if cmp(l[4], l[5]) <0:
#            try: 
#                if int(l[4]) <int(l[5]):
#                    l[4] =l[5]
#                    l[5] =tmp     
#            except:
#                 print 're'
            for i in range(1,5):
                s +='\t'+l[i].strip('\n')
            if l[4]!='':
                s += '*'+ l[5]
            else:
                s +=l[5]
            for j in range(6,len(l)):
                s +='\t'+l[j].strip('\n')
        return s


#fun is the main function ,it calls verRes( modify the os_version,add * between resolution) and add os to data 
def fun(osfile, data, out):
    fp1 = open (osfile, 'r')
    fp2 = open (data, 'r')
    fpout = open (out, 'w')
    dt = {}
    dt2 = {} #use to compute the data file
    for line in fp1:
        tmp = line.strip('\n').split('\t')
        if len(tmp)<4:
            continue
        dt[tmp[2].lower()]=[tmp[0], tmp[3]]
   
    for line in fp2:
         tmp = line.strip().split('\t')
         if len(tmp)<7:
             continue
         key1 = tmp[0]+'\t'+tmp[1]+'\t'+tmp[2]+'\t'+tmp[3]
         v = [0, 0]
#wenti         if tmp[5] == 'f':
#             print line
         try:
             if key1 not in dt2:
                 v[0] = int(tmp[5])
                 v[1] = int(tmp[6])
             else:
                 v1= dt2[key1]
                 v[0] = int(tmp[5])+ v1[0]
                 v[1] = int(tmp[6]) + v1[1]
         except:
             continue 
         dt2[key1] = v

    for key2 in dt2:
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
        key = tmp[0].lower()
        if key in dt:
            os = dt[key][0]
            cpu = dt[key][1]
        else:
            os = ''
            cpu = ''
        s = os+ '\t'+ tmp[1]+ '\t'+ tmp[0]+ '\t'+ cpu+'\t'+tmp[2]+'\t'+tmp[3].strip('\n')+'\t'+str(value[0]).strip('\n')+'\t'+str(value[1]).strip('\n')
#        for i in range(len(value)):
#            s +='\t'+tmp[i].strip('\n')
        s=verRes(s)
        fpout.write(s+'\n')


if __name__=='__main__':
    fun(sys.argv[1], sys.argv[2], sys.argv[3])
#argv[1]:input the file with os,argv[2]:input the raw file,sys.argv[3]:the out file to pig
