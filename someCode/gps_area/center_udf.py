@outputSchema("latcenter:double")
def getlatcenter(lat):
    left =39.68
    right =40.20
    if lat<left or lat>=right:
        return -1.0
    total =200
    step =(right-left)/total
    return (int((lat-left)/step))*step + left +(step/2)

@outputSchema("longcenter:double")
def getlongcenter(lng):
    bottom =116.08
    top =116.74
    if lng<bottom or lng>=top:
        return -1.0
    total =200
    step =(top-bottom)/total
    return (int((lng-bottom)/step))*step +bottom +(step/2)




