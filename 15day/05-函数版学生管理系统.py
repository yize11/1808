list = []
def l():
    d = {}
    name = input('请输入姓名')
    age = input('请输入年龄')
    sex = input('请输入性别')
    d['name'] = name
    d['age'] = age
    d['sex'] = sex
    list.append(d)
    print(list)
def l1():
    name = input('请输入你要查找的学生的姓名')
    for i in list:
        if i['name'] == name:
            print('姓名%s\n年龄%d\n性别%d\n'%(i['name'],i['age'],i['sex']))
            break
def l2():
    name = input('请输入你要修改学生的名字')
def l3():
    name = input('请输入删除的姓名')
    pass
def gl():
    print('欢迎来到学生管理系统'.center(30,'*'))
    while True:
        print('1、添加学生')
        print('2、查找学生')
        print('3、修改学生')
        print('4、删除学生')
        print('5、退出程序')
        l4()
        
def l4():
    num = int(input('请选择功能'))
    if num == 1:
        l()#调用添加函数
    elif num == 2:
        l1()
    elif num == 3:
        l2()
    elif num == 4:
        l3()
    elif num == 5:
        print('谢谢使用'.center(30,'*'))
        exit()
gl()
