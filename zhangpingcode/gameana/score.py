import math

@outputSchema("tagscore:bag{score:tuple(tag:chararray, tfidf1:double, tfidf2:double, tfidf3:double, bm251:double, bm252:double, bm253:double)}")
def calcScore(log, allappNum, allusrNum):
    tot1 = 0
    tot2 = 0
    tot3 = 0
    k = 2
    b = 0.75
    tagdt = {}
    lenlog = len(log)
    avgLen = float(allappNum)/float(allusrNum)
    for l in log:
        w = math.log(float(allusrNum+1)/float(l[7]+1))#index 7 is appuserNum
        l2 = 0
        l3 = 0
        l4 = 0
        if l[2]!=None:
            s2 = l[2]*w
            l2=l[2]
        if l[3]!=None:
            s3 = l[3]*w
            l3=l[3]
        if l[4]!=None:
            s4 = l[4]*w
            l4=l[4]
        tot1 += s2
        tot2 += s3
        tot3 += s4
        tag = l[6]
        if tag==None:
            continue
        if tag not in tagdt:
            tagdt[tag]=[0.0,0.0,0.0,0.0,0.0,0.0]
        tagdt[tag][0]+=s2#tfidf1 += s2*w
        tagdt[tag][1]+=s3#tfidf2 += s3*w
        tagdt[tag][2]+=s4#tfidf3 += s4*w
        tagdt[tag][3]+=w*(l2*(1+k))/(l2+(1-b+b*(float(lenlog)/avgLen)))
        tagdt[tag][4]+=w*(l3*(1+k))/(l3+(1-b+b*(float(lenlog)/avgLen)))
        tagdt[tag][5]+=w*(l4*(1+k))/(l4+(1-b+b*(float(lenlog)/avgLen)))
    if tot1==0:
        tot1 = 1
    if tot2==0:
        tot2 = 1
    if tot3==0:
        tot3 = 1
    #return tfidf1/(tot1**0.5), tfidf2/(tot2**0.5), tfidf3/(tot3**0.5), bm251, bm252, bm253
    outBag=[]
    for ktag in tagdt:
        tup=(ktag, tagdt[ktag][0]/(tot1), tagdt[ktag][1]/(tot2), tagdt[ktag][2]/(tot3), tagdt[ktag][3],tagdt[ktag][4],tagdt[ktag][5])
        outBag.append(tup)
    return outBag


