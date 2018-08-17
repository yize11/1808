i = 1
sum1 = 0#定义偶数和
sum2 = 0#定义奇数和
while i <= 100:
    if i%2 == 0:#偶数
        sum1 += i#加起来的一定是偶数
    else:
        sum2 += i#加起来的一定是奇数
    i+=1
print('偶数和是%d'%sum1)
print('奇数和是%d'%sum2)
