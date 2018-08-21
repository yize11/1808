a = [31,28,31,30,31,30,31,31,30,31,30,31]#平年
s = [31,29,31,30,31,30,31,31,30,31,30,31]#闰年
year = int(input('请输入年'+'\n'))
month = int(input('请输入月'+'\n'))
day = int(input('请输入日'+'\n'))
arr =[31,28,31,30,31,30,31,31,30,31,30,31]
sum = day
for i in range(0,month-1):
    sum+=arr[i]
if year%4==0:
    if year%100==0 and year%400!=0:
        print('这是今年的第%d天'%sum)
    else:
        sum+=sum+1
        print('这是今年的第%d天'%sum)
else:
    print('这是今年的第%d天'%sum)
