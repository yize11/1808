def wangzhe(yx):
    if yx == '亚瑟':
        return '黑暗骑士'+yx
    elif yx == '鲁班':
        return '电玩小子'+yx
    elif yx == '王昭君':
        return '爱情王昭君'+yx
    else:
        return '不知道'








yx = input('请输入英雄')
ret = wangzhe(yx)
print(ret)

