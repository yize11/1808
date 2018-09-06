def test(x,y,*args,f=12,**kwargs):
    print(x)
    print(y)
    print(f)
    print(args)
    print(kwargs)
    sum = 0
    c = 0
    for i in args:
        sum=sum+i
    print(sum)
    for j in kwargs.values():
        c=c+j
    b = x+y+f+sum+c
    print(b)
#test(1,2,3,4,5,a=99,phone=13,age=12)
t =(4,5,6)
d = {'age':12,'weight':200}
test(1,2,*t,f=11,**d)
