print('欢迎来到学生管理系统'.center(30,'-'))
box = []
while True:
    print('1、添加')
    print('2、修改')
    print('3、查找')
    print('4、删除')
    print('5、退出')
    num = int(input('请选择功能'))
    if num == 1:
        xjb = {}
        name = input('请输入名字:')
        age = int(input('请输入年龄:'))
        sex = input('请输入性别:')
        phone = input('请输入手机号:')
        xjb['name'] = name
        xjb['age'] = age
        xjb['sex'] = sex
        if len(phone) == 11 and phone.startswith('1') == True:
            xjb['phone'] = phone
        else:
            print('输入不合法,请重新输入')
            continue
        box.append(xjb)
        print(box)
    elif num == 2:
        print('修改')
        name = input('请输入修改的名字')
        for xjb in box:
            if xjb['name'] == name:
                print('1、修改名字')
                print('2、修改年龄')
                print('3、修改性别')
                print('4、修改手机号')
                num = int(input('请选择功能:'))
                if num == 1:
                    name = input('请输入新的名字:')
                    xjb['name'] = name
                elif num == 2:
                    age =int(input('请输入新的年龄:'))
                    xjb['age'] = age
                elif num == 3:
                    sex = input('请输入新的性别:')
                    xjb['sex'] = sex
                elif num == 4:
                    phone = input('请输入新的手机号')
                    if len(phone) == 11 and phone.startswith('1') == True:
                        xjb['phone'] = phone
                        print('修改成功')
                    else:
                        print('修改失败')
                        break
    elif num == 3:
        name = input('请输入要查找的名字')
        flag = False
        for xjb in box:
            if xjb['name'] == name:
                print('学生姓名:%s\n学生年龄:%d\n学生性别:%s\n学生手机号:%s\n'%(xjb['name'],xjb['age'],xjb['sex'],xjb['phone']))
                flag= True                
                break
        if flag:
            print('查到了')
        else:
            print('查无此人')
        '''
        if not flag:
            print('查无此人')
        '''
    elif num == 4:
        name = input('请输入删除的名字')
        for xjb in box:
            if xjb['name'] == name:
                num = int(input('是否删除:1:yes 2:No'))
                if num == 1:
                    box.remove(xjb)
                    print('删除成功')
    elif num == 5:
        print('欢迎下次使用'.center(30,'-'))
        break





























