##****************************************
## UDF for generating the standard form of the model resolution 
##****************************************
@outputSchema("resolution:chararray")
def getreso(h, w):
    try:
        inth = int(h)
        intw = int(w)
    except Exception:
        return '0*0'
    if inth>intw:
        return str(inth)+'*'+str(intw)
    else:
        return str(intw)+'*'+str(inth)
