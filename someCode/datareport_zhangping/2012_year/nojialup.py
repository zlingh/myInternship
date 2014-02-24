import sys
import os
from string import atoi
def modelfun(modelResData):# get the model , resolution report
    datafil = open (modelResData, 'r')
    if not os.path.isdir('dataout'):
        os.mkdir('dataout')
    iosModelfil = open("dataout/IOS_nojailup_Distribution",'w')
    iosModeldt ={}
   
    for line in datafil:
        tmp = line.strip('\n').split('\t')
        if len(tmp)!=3:
            continue
        model = tmp[0].lower().replace(" ","")
        modelNum = atoi(tmp[2])
        iosModeldt[model] = iosModeldt.get(model, 0)+modelNum
            
    for k,v in iosModeldt.items():
        iosModelfil.write(k +'\t' +str(v)+ '\n')
                      
    iosModelfil.close()

if __name__=='__main__':
    modelfun(sys.argv[1])
