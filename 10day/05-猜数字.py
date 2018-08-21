import random
count = random.randint(1,100)
for i in range(1,11):
    num = int(input('请输入一个数字'))
    if num > count:
        print('猜大了')
    elif num < count:
        print('猜小了')
    else:
        print('猜对了')
        break
