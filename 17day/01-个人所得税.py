def shui():
    ans = 0
    if m > 3500:
        m1 = m - 3500
        if m1 < 1500:
            ans = 0.03 * m1
        elif m1 < 4500:
            ans = 0.1 * m1
        elif m1 < 9000:
            ans = 0.2 * m1
        elif m1 < 35000:
            ans = 0.25 * m1
        elif m1 < 55000:
            ans = 0.3 * m1
        elif m1 < 80000:
            ans = 0.35 * m1
        else:
            ans = 0.45 * m1
    else:
        ans = 0
        print("%.0f"%ans)
m = int(input('请输入金钱'))
shui()
