@outputSchema("age:int")
def getUsrDay(date1,date2):
    try:
        tmp=date1.split('-')
        year1=int(tmp[0])
        month1=int(tmp[1])
        day1=int(tmp[2])
        tmp=date2.split('-')
        year2=int(tmp[0])
        month2=int(tmp[1])
        day2=int(tmp[2])
        if year1>2013 or year1< 2010:
            return -1
        age=(year2-year1)*12*30+(month2-month1)*30+(day2-day1)+1
        if age<1:
            return -1
        return age
    except Exception:
        return -1
