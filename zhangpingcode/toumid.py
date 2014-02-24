#change imei(android),udid(ios) to umid
import sys
import md5 

def to_umid(s):
  res=md5.new(s).hexdigest().lower()
  if len(res)<32:
    return res 
  i=0
  nres=[]
  for e in res:
    if i%2 == 0:
      if e != '0':
        nres.append(e)
    else:
      nres.append(e)
    i+=1
  return ''.join(nres)
def ff(in1,outf):
    inf=in1+".udid"
    infi=open(inf, 'r')
    outfi=open(outf, 'w')
    for line in infi:
        line1=line.strip('\n')
        line2=to_umid(line1)+'\t'+in1+'\n'
        outfi.write(line2)
if __name__=='__main__':
    ff(sys.argv[1],sys.argv[2])


