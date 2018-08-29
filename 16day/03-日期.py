def calu():
    days = 0
    dete = '20180827'
    year = int(date[0:4])
    month = int(date[4:6])
    day = int(date[6:])
    big_month = [1,3,7,8,12]
    small_month = [4,6,9,11]
    for i in range(1,month):
        if i in big_month:
            days+=31
        elif i in small_month:
            days+=30
        else:
            if checkyear(year):
                days+=29
            else:
                days+=28
                else:
                    if (year%4==0 and year%100!=0) or year%400 == 0:
                        return True
                    else:
                        return False
    days+=day
    print(days)
def checkyear(year):
    if (year%4==0 and year%100!=0) or year%400 == 0:
        days+=29
    else:
        days+=28
calu()    
