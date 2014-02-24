#get some sample from the input file by flag's second char is in wantflag
import sys
from string import atoi

def getsample(infile,outfile):
    infil = open(infile, 'r')
    outfil = open(outfile, 'w')
    wantflag ={'1':1, '9':1, '5':1, 'a':1, 'd':1}
    for line in infil:
        tmp =line.strip('\n').split('\t')
        if len(tmp) !=5:
            continue
        flaglis =list(tmp[2].lower())
        if len(flaglis) !=2:
            continue
        keyf =flaglis[1]
        if keyf in wantflag:
            outfil.write(line)

if __name__ =='__main__':
    getsample(sys.argv[1], sys.argv[2])
