def cal(num):
    if num == 1:
        return 1
    else:
        return num*cal(num-1)
ret = cal(5)
print(ret)
