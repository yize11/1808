import random 
i2 = random.randint(1,100)
for i in range(1,10):
    i1 = int(input('请输入数字'))
    if i1 > i2:
        print('你猜大了')
    elif i1 < i2:
        print('你猜小了')
    elif i1 == i2:
        print('你猜中了')
        break

