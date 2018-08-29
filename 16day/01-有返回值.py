def login(phone):
    if checkphone(phone):
        print('登录')
    else:
        print('不合法')
def register(phone):
    if checkphonen(phone):
        print('注册')
    else:
        print('不合法')
def checkphone(phone):
    if phone.starswith('1') and len(phone) == 11:
        return True
    else:
        return False
a = input('请输入手机号')
login(a)

