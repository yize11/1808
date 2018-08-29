def calu(x,y,z):
    if c == '+':
        print(x+y)
    elif c == '-':
        print(x-y)
    elif c == '*':
        print(x*y)
    elif c == '/':
        if y != 0:
            print(x/y)
a = int(input('请输入数字'))
b = int(input('请输入数字'))
c = input('请输入:+-*/')
calu(a,b,c)
