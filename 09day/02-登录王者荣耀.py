account = '123456'
password = 123456
i = 0
while i < 3:
    acc = input('请输入账号')
    pwd = int(input('请输入密码'))
    if acc == account and pwd == password:
        print('登录成功')
        yingxiong = input('请选择英雄1、ADC 2、肉盾 3、法师')
        if yingxiong == '1':
            print('鲁班七号')
        elif yingxiong == '2':
            print('程咬金')
        elif yingxiong == '3':
            print('王昭君')
    else:
        print('账号或密码错误')
    i+=1

