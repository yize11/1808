import random
num = random.randint(1,100)
while True:
    num1 = int(input('请输入数字'))
    if num1 > num:
        print('猜大了')
    elif num1 < num:
        print('猜小了')
    else:
        print('猜中了')
        break
