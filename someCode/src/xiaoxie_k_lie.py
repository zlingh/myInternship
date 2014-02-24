import sys
def fun(infile, outfile,k):
    fp = open(infile,'r')
    out = open(outfile, 'w')
    n =int(k)
    for line in fp:
        tmp = line.strip().split('\t')
        tmp[n] =tmp[n].lower()
        s =tmp[0]
        for i in range(1, len(tmp)):
            s += '\t' +tmp[i]
        out.write(s+ '\n')
if __name__=='__main__':
    fun(sys.argv[1],sys.argv[2], sys.argv[3])
