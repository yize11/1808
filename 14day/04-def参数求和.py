def ss(x,y):
    sum = 0
    for i in range(x,y+1):
        if x < y:
            sum+=i
    print(sum)
a = int(input('请输入一个数字'))
b = int(input('请输入一个数字'))
ss(a,b)
