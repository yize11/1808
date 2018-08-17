for i in range(1,100):
    i1 = int(input('请输入数字'))
    if i1 > i:
        print('你猜大了')
    elif i1 < i:
            print('你猜小了')
    else:
        print('你猜中了')
        break

