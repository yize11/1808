def a(b,c=100):
    for i in range(b,c):
        if i%3 == 0 and i%5 == 0:
            print(i)
b = int(input('请输入数字'))
a(b)
