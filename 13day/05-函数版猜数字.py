import random
def shuzi():
    while True:
        num = random.randint(1,101)
        num1 = int(input('请输入数字'))
        if num1 > num:
            print('猜大了')
        elif num1< num:
            print('猜小了')
        elif num1 == num:
            print('猜中了')
            break
shuzi()
       

