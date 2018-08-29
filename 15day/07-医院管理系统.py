#今天要写的是一个简单的医院挂号系统，你是挂号管理员
#这两行不参与循环，所以放在外边
print('*='*25)
print("尊敬的挂号管理员您好,欢迎您再次使用本系统")
list_guahao = []#定义一个列表，用来存放数据
def menu ():#这是菜单
    print("1.录入病人信息")
    print("2.显示录入列表")
    print("3.查找病人房房号")
    print("4.修改录入信息")
    print("5.删除病人信息")
    print("6.退出挂号系统")
    print("×="*25)

def luru():#这是需要录入的信息
    print("开始录入信息")
    name = input("请输入名字")
    sex = input("请输入性别")
    fanghao = input("请输入病房号")
    dic = {"name":name,"sex":sex,"fanghao":fanghao}
    list_guahao.append(dic)#建立一个字典，用来存放数据，将字典追加到列表中
    print("信息录入成功！姓名是:%s\n性别是%s\n病房号是%s\n"%(dic["name"],dic["sex"],dic["fanghao"]))
    print(list_guahao)#然后显示一下列表
    print("显示完毕".center(25,"*"))
    print("姓名是:%s\n性别是:%s\n房号是:%s\n"%(dic["name"],dic["sex"],dic["fanghao"]))

def xianshi():
    for i in list_guahao:
        print("姓名是:%s\n性别是:%s\n病房号是:%s\n"%(i["name"],i["sex"],i["fanghao"]))
    if len(list_guahao) == 0:
        print("没有任何名片记录")

def find():
    print("前台的小姐姐打来电话，有家属要来探病，想问你一下他住在哪儿？")
    f = input("请输入要查找的姓名:")
    fin = 0#默认表示没有找到
    for i in list_guahao:
        if f == i["name"]:
            print("病人住在%s号"%i["fanghao"])
            fin = 1
            break
    if fin == 0:
        print("找不到这个人，你问一下家属确定是这个医院吗？")


def gai():
    #修改函数
    print("在整理录入信息中发现信息禹前台登记不符需要进行修改")
    ch = input("请输入需要修改信息的病人")
    for i in list_guahao:
        if i['name'] == ch:
            print('1、修改名字')
            print('2、修改性别')
            print('3、修改病房号')
            num =int(input('请选择功能'))
            if num == 1:
                name = input("请输入新的名字")
                i['name'] = name
                break
            elif num == 2:
                sex = input("请输入病人的性别")
                i['sex'] = sex
                
            elif num == 3:
                fanghao = input("请输入新病房号")
                i['fanghao'] = fanghao
                print("修改完毕".center(25,"*"))
            else:
                print("查无此人".center(25,"×"))
                break

def deln():#删除函数
    print("信息录入系统需要每隔三个月进行一次整理，需要删除已出院并且复查完毕的病人信息")
    de = input("请输入要删除的病人姓名")
    for i in list_guahao:
        if i["name"] == de :
            list_guahao.remove(i)
            break
    print("删除完毕".center(25,"*"))

def main():
    #完成对整个模块的调用

    while True:
        menu()
        #获取用户输出
        user = input("请选择你要进行的操作编号:")
        if user == "1":
            luru()
        elif user == "2":
            xianshi()
            print("显示完毕".center(25,"x"))
        elif user == "3":
            find()
        elif user == "4":
            gai()
        elif user == "5":
            deln()
        elif user == "520":
            佛祖镇楼.佛祖镇楼()
        elif user == "6":
            print("感谢您的使用,再见。".center(30,'*'))
            break
        else:
            print("输入有误，请重新输入")
main()#主函数执行

