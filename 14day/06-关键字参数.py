def a(name,age):
    print('我叫%s年龄是%d'%(name,age))
#a('小明',12)#位置参数
a(name='小明',age=12)#关键字参数
a(age=12,name='小明')#关键字参数
a('小明',age=12)#关键字参数

#错误
#关键字参数必须在位置参数后面
#a(age=12,'小明')
#a(name='小明',age=12)

#12对应的是name
#小明对应的也是name
#a(12,name='小明')
