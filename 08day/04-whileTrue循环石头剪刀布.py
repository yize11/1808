while True:
    import random
    cp = random.randint(1,3)
    wj = int(input('请输入:1、石头 2、剪刀 3、布'))
    if (wj == 1 and cp == 2) or (wj == 2 and cp == 3) or (wj == 3 and cp == 1):
        print('玩家赢')
    elif wj == cp:
        print('平局')
    else:
        print('电脑赢')
