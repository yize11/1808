def test(a):
    a+=a
    print(a)#[1,1]
x = [1]
test(x)
print(x)#[1,1]





def test1(a):
    a=a+a#先算等号右边，然后把值赋值一个新的变量来指向
    print(a)#[1,1]
x = [1]
test1(x)
print(x)#[1]




'''
def test2(a):
    a+=a
    print(a)#[1,1] 如果可变类型数据，是指a指向上的变量上修改
'''
