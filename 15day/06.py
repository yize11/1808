list = []
def add():#添加功能
    stu = {}
    while True:
        name = input("请输入学生姓名")
        age = input("请输入学生年龄")
        sex = input('请输入学生性别')
        stu['name'] = name
        stu['age'] = age
        stu['sex'] = sex
        list.append(stu)
        print(list)
def find():#查找功能
    name = input("请输入要查找的名字")
    name = name.strip()
    for stu in list:
        if stu["name"] == name:
            print("学生姓名:%s\n学生年龄:%d\n学生性别%s\n"%(stu["name"],stu["age"],atu['sex']))
            break
def change():#修改功能
    name = input("请输入要修改的名字")
    name = name.strip()
    for stu in list:
        if stu["name"] == name:
            print("1、修改名字")
            print("2、修改年龄")
            print('3、修改性别')
            num = int(input("请选择功能"))
            if num == 1:
                name = input("请输入新的名字")
                stu["name"] = name
            elif num == 2:
                age = int(input("请输入新的年龄"))
                stu["age"] = age
            elif num == 3:
                sex = input('请输入新的性别')
                stu['sex'] = sex
def delete():#删除功能
	name = input("请选择要删除的名字")
	for stu in list:
		if stu["name"] == name:
			list.remove(stu)
			print("删除成功")
			break
def print_menu():
	print("欢迎来到学生管理系统".center(30,"*"))
	while True:
		print("1、添加学生信息")
		print("2、查找学生信息")
		print("3、修改学生信息")
		print("4、删除学生信息")
		print("5、退出学生系统")
		input_info()#调用选择功能函数
def input_info():
    num = input("请选择功能")
    if num == 1:
        add()#调用添加函数
    elif num == 2:
        find()
    elif num == 3:
        change()
    elif num == 4:
        delete()
    elif num == 5:
        exit()
print_menu()
