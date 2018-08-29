def year():
    num = int(input('请输入年份'))
    if num%4 == 0 and num%100!=0:
        print('闰年')
    elif num%400 == 0:
        print('闰年')
    else:
        print('平年')
year()
