import sys
def ff(infile, outfile):
    infil =open(infile,'r')
    outfil =open(outfile, 'w')
    for line in infil:
        line1 =line.lower()
        outfil.write(line1)

if __name__=='__main__':
    ff(sys.argv[1],sys.argv[2])
