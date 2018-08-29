def test(x,y,z,*args,a=99,**kwargs):
    print(x)
    print(y)
    print(z)
    print(a)
    print(args)
    print(kwargs)
    sum = 0
    c = 0
    for i in args:
        sum=sum+i
    print(sum)
    for j in kwargs.values():
        c=c+j
    b = x+y+z+a+sum+c
    print(b)
test(1,2,3,4,5,a=99,phone=13,age=12)
