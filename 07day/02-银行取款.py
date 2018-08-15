pwd = 123456
account = '123'
money = 9999
zhanghao = input('请输入账号:')
mima = int(input('请输入密码:'))
if zhanghao == account and mima == pwd:
    print('登录成功')
    my = float(input('请输入取款金额:'))
    if my > money:
        print('余额不足')
    else:
         print('取款成功')
else:
    print('账号密码错误')

