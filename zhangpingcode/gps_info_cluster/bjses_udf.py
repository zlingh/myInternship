@outputSchema("y:bag{info:tuple(lng:float, lat:float, time:long)}")
def bjbag_start(bag):
    outBag=[]
    for w in bag:
        if w[2]>116.08 and w[2]<116.74 and w[3]>39.68 and w[3]<40.20:
            tup=(w[2],w[3],w[4])
            outBag.append(tup)
    return outBag

def bjbag_end(bag):
    outBag=[]
    for w in bag:
        if w[4]>116.08 and w[4]<116.74 and w[5]>39.68 and w[5]<40.20:
            tup=(w[4],w[5],w[6])
            outBag.append(tup)
    return outBag

@outputSchema("bj:chararray")
def hasbj(bag):
    result='n'
    for w in bag:
        lng=w[2]
        lat=w[3]
        if lng>116.08 and lng<116.74 and lat>39.68 and lat<40.20:
            result='y'
            break
    return result

