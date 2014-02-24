import sys
import os
from string import atoi
def modelfun(modelResData):# get the model , resolution report
    datafil = open (modelResData, 'r')
    if not os.path.isdir('dataout'):
        os.mkdir('dataout')
    andModelfil = open("dataout/Android_model_Distribution",'w')
    iosModelfil = open("dataout/IOS_model_Distribution",'w')
    wpModelfil = open("dataout/Windowsphone_model_Distribution",'w')
    andModeldt ={}
    iosModeldt ={}
    wpModeldt ={}
   
    for line in datafil:
        tmp = line.strip('\n').split('\t')
        if len(tmp)!=4:
            continue
        model = tmp[1].lower().replace(" ","")
        os1 = tmp[0].lower()
        modelNum = atoi(tmp[3])
            
        if ((os1 == 'ios') or (os1 == 'iphoneos')):
            iosModeldt[model] = iosModeldt.get(model, 0)+modelNum
        if os1 == 'windowsphone':
            wpModeldt[model] = wpModeldt.get(model, 0)+modelNum
        if os1 == 'android':
            andModeldt[model] = andModeldt.get(model, 0)+modelNum
            
    for k,v in iosModeldt.items():
        iosModelfil.write(k +'\t' +str(v)+ '\n')
        
    for k,v in andModeldt.items():
        andModelfil.write(k +'\t' +str(v)+ '\n')
        
    for k,v in wpModeldt.items():
        wpModelfil.write(k +'\t' +str(v)+ '\n')
                      
    iosModelfil.close()
    andModelfil.close()
    wpModelfil.close()


if __name__=='__main__':
    modelfun(sys.argv[1])
