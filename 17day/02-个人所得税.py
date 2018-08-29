def grsds(money):
    if money > 0 and money <=1500:
        s = money*0.03
    elif money > 1500 and money <= 4500:
        s = money*0.1
    elif money > 4500 and money <= 9000:
        s = money*0.2
    else:
        s = money*0.5
    return s
ret = grsds(10000)
print(ret)
