import math

@outputSchema("tagscore:bag{score:tuple(tag:chararray, tfidf1:double, tfidf2:double, tfidf3:double)}")
def calcScore(log):
    tot1 = 0
    tot2 = 0
    tot3 = 0
    tagdt = {}
    lenlog = len(log)
    for l in log:
        s2 = 0
        s3 = 0
        s4 = 0
        if l[2]!=None:
            s2=l[2]
        if l[3]!=None:
            s3=l[3]
        if l[4]!=None:
            s4=l[4]
        tot1 += s2
        tot2 += s3
        tot3 += s4
        tag = l[6]
        if tag==None:
            continue
        if tag not in tagdt:
            tagdt[tag]=[0.0,0.0,0.0]
        tagdt[tag][0]+=s2#tfidf1
        tagdt[tag][1]+=s3#tfidf2
        tagdt[tag][2]+=s4#tfidf3
    if tot1==0:
        tot1 = 1
    if tot2==0:
        tot2 = 1
    if tot3==0:
        tot3 = 1
    outBag=[]
    for ktag in tagdt:
        tup=(ktag, tagdt[ktag][0]/(tot1), tagdt[ktag][1]/(tot2), tagdt[ktag][2]/(tot3))
        outBag.append(tup)
    return outBag


