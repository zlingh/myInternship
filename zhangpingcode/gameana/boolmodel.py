import math
@outputSchema("tagscore:bag{score:tuple(tag:chararray, bol:double)}")
def calcScore(log):
    tagdt = {}
    totalapp = len(log)
    for l in log:
        tag = l[3]
        if tag==None:
            continue
        if tag not in tagdt:
            tagdt[tag]=0.0
        tagdt[tag]+=1#tfidf1 += s2*w
    outBag=[]
    for ktag in tagdt:
        tup=(ktag, tagdt[ktag]/totalapp)
        outBag.append(tup)
    return outBag
