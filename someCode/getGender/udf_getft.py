@outputSchema ("gender:chararray")
def getFGen(bag):
    try:
        if len(bag) ==1:
            first =bag[0][0]
        else:
            first ='gender-collision'
    except Exception:
        return 'error'
    return first

@outputSchema ("age:chararray")
def getFAg(bag):
    try:
        if len(bag) ==1:
            first =bag[0][0]
        else:
            first ='age-collision'
    except Exception:
        return 'error'
    return first


