#group the infile data by it's flag field's second char ,and compute the Nums and laungchNums


from string import atoi
import sys

def comflag(infile,out):
    flag_dit ={}
    outfil =open(out, 'w')
    infil =open(infile, 'r')
    for line in infil:
        tmp = line.strip('\n').split('\t')
        if len(tmp) != 5:
            continue
        flag2 =tmp[2].lower()
        flagli = list(flag2)
        if len(flagli) !=2:
            continue
            print flagli
        key = flagli[1]
        vlist= [0, 0]
        if key not in flag_dit:
            vlist [0] = atoi(tmp[3])
            vlist [1] = atoi(tmp[4])
            flag_dit[key] = vlist
        else:
            vlist [0] =flag_dit[key][0] +atoi(tmp[3])
            vlist [1] =flag_dit[key][1] +atoi(tmp[4])
            flag_dit[key] = vlist
    for k in flag_dit:
        outfil.write(k+ '\t' +str(flag_dit[k][0]) +'\t' +str(flag_dit[k][1]) +'\n')

if __name__ == '__main__':
    comflag(sys.argv[1], sys.argv[2])

