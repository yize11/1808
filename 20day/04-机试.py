import time
print('欢迎来到房山宾馆'.center(30,'*'))
list=[]
money = 0
while True:
    print('1、住店')
    print('2、离店')
    print('3、统计')
    print('4、退出')
    num = int(input('请选择功能'))
    if num == 1:
        d = {}
        name = input('请输入姓名')
        sfzh = str(input('请输入身份证号'))
        d['name'] = name
        d['time'] = int(time.time())
        list.append(d)
        print(list)
        if len(sfzh) == 18:
            print('输入成功')
            continue
        else:
           print('请重新输入')    
    elif num == 2:
        name =input('请输入离店人的名字')
        for i in list:
            if i['name'] == name:
                endtime = int(time.time())
                swq = (endtime - i['time'])*10
                print('花了%.02f'%swq)
                money += swq
                print('离店成功')
    elif num == 3:
        count = 0
        print('今天住店人数%d'%len(list))
        for i in list:
                count+=1
        print('今天离店人数%d'%count)
        print('今天收益%.02f'%money)
    elif num == 4:
        print('谢谢使用'.center(30,'*'))
        break
