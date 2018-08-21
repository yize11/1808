import time
print('欢迎来到麒麟网咖'.center(30,'*'))
list = []
all_money = 0
while True:
    print('1、上机')
    print('2、下机')
    print('3、管理员登录')
    num = int(input('请选择功能'))
    if num == 1:
        d = {}
        card = input('请输入身份证号')
        if len(card) == 18:
            print('输入正确')
        else:
            print('输入错误,请重新输入')
            continue
        money = float(input('请输入金额'))
        d['card'] = card
        d['money'] = money
        d['time'] = int(time.time())
        d['sj'] = True
        list.append(d)
        print(list)
    elif num == 2:
        print('下机')
        card = input('请输入身份证号')
        for i in list:
            if i['card'] == card:
                i['sj'] = False
                endtime = int(time.time())
                diff_money = (endtime-i['time'])*10
                all_money +=diff_money#统计总钱
                diff = i['money'] - diff_money
                if diff < 0:
                    print('您欠了%.02f'%diff)
                    while True:
                            money = float(input('请输入金额'))
                            if money >= abs(diff):
                                print('找零%d'%(money+diff))
                                break
                            else:
                                print('输入的钱不足,欠了%.02f'%diff)
                                continue
                    print('上网花了%.02f元,还剩%.02f元'%(diff_money,0))
                else:
                    print('上网花了%.02f元,还剩%.02f元'%(diff_money,diff))
                    break
    elif num == 3:
        account = input('请输入管理员账号')
        pwd = input('请输入管路员密码')
        if account == 'admin' and pwd == 'admin':
            print('欢迎老板进入系统')
            num = int(input('请选择功能'))
            count = 0
            if num == 1:
                print('今天上机%d'%len(list))
                for i in list:
                    if i['sj'] == False:
                        count+=1
                print('今天下机%d'%count)
                print('今天收益%.02f'%all_money)
        break
        
        



















