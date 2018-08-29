import time
print("欢迎来到房山宾馆".center(30,'*'))
list = []
all_money = 0
while True:
    print("1、住店")
    print("2、离店")
    print("3、统计")
    print("4、退出")
    num = int(input('请选择功能'))
    if num == 1:
        d = {}
        card = input('请输入身份证号')
        d['card'] = card
        d['time'] = int(time.time())
        d['zd'] = True
        list.append(d)
        print(list)
    elif num == 2:
        print('离店')
        card = input('请输入身份证号')
        for i in list:
            if i['card'] == card:
                i['zd'] = False
                endtime = int(time.time())
                swq = (endtime-i['time'])*10
                print('花了%.02f'%swq)
                #money = float('请输入金额,不找零')
                all_money += swq
                print('离店成功')
    elif num == 3:
        print('统计')
        account = input('请输入管理员账号')
        pwd = input('请输入管理员密码')
        if account == '123456' and pwd == '123456':
            print('欢迎老板进入使用')
            num = int(input('请选择功能'))
            count = 0
            if num == 3:
                print('今天住店人数%d'%len(list))
                for i in list:
                    if i['zd'] == False:
                        count+=1
                print('今天离店人数%d'%count)
                print('今天收益%.02f'%all_money)
    elif num == 4:
        print('退出系统')
        print('欢迎下次使用'.center(30,'*'))
        break
