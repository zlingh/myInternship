import time
@outputSchema("day:long")
def getuseday(t1,t2,num):
    nt1 = time.strptime(t1, "%Y-%m-%d")
    nt2 = time.strptime(t2, "%Y-%m-%d")
    s1= long(time.mktime(nt1))
    s2= long(time.mktime(nt2))
    s=long((s2-s1)/86400+1)
    c = long(num)
    if s>c:
        return c
    if s<0:
        return 1
    return s
