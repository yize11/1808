list = []
for i in range(1,13):
    all = 0#每月花的钱
    if i == 1 or i== 12:
        diz = 32
    elif i ==2 or i == 11:
        diz = 18
    elif i == 3 or i == 10:
        diz = 9
    elif i == 4 or i == 9:
        diz == 14
    elif i == 5 or i == 8:
        diz == 32
    elif i == 6 or i == 7:
        diz == 70
    for j in range(60):
        if diz <= 6:
            price = 3
        elif diz > 6 and diz <= 12:
            price = 4
        elif diz > 12 and diz <= 22:
            price = 5
        elif diz > 22 and diz <= 32:
            price = 6
        elif diz > 32:
            if (diz-32)%20 == 0:
                price = 6+int((diz-32)/20)+1
            else:
                price = 6+int((diz-32)/20)+1
        if all>=100 and all <=150:
            price = price*0.5
        all+=price
        d ={}
    d[i] = all
    list.append(d)
money = 0
for i in list:
    for k,v in i.items():
        print('%d月花了%.02f'%(k,v))
        money+=v
print('一共花了%.02f'%money)
