def a():
    phone = str(input('请输入手机号'))
    if len(phone) == 11 and phone.startswith('1') == True:
        print('输入正确')
    else:
        print('输入错误')
a()
