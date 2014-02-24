#contrast the rate of two file
#@author: zhangping
#@company:umeng
import sys
from string import atoi
def contrastfun(file1,file2,outfile):
     fil1 =open(file1, 'r')
     fil2 =open(file2, 'r')
     outfil =open(outfile, 'w')
     dt1 ={}
     dt2 ={}
     sum1 =0
     sum2 =0
     num =0
     for line1 in fil1:
         tmp1 =line1.strip('\n').split('\t')
         if len(tmp1) !=2:
             continue
         try:
             num =atoi(tmp1[1])
         except:
             continue
         dt1[tmp1[0].lower()] =num
         sum1 +=num
     print sum1
     for model1 in dt1:
         dt1[model1] =float(dt1[model1])/sum1
         if model1 =='gt-i9300':
             print dt1[model1]

     for line2 in fil2:
         tmp2 =line2.strip('\n').split('\t')
         if len(tmp2) !=2:
             continue
         try:
             num =atoi(tmp2[1])
         except:
             continue
         dt2[tmp2[0].lower()] =num
         sum2 +=num
     for model2 in dt2:
         dt2[model2] =float(dt2[model2])/sum2
     
     for key in dt1:
         if key =='gt-i9300':
             print key +'\t' +str(dt1[key])
         outfil.write(key +'\t' +str(round(dt1[key],4)) +'\t'+str(round(dt2.get(key, 0),4))+'\n')

if __name__ =='__main__':
    contrastfun(sys.argv[1], sys.argv[2], sys.argv[3])



