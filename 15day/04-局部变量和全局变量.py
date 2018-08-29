list = []
name = '翼泽'
def s():
    global name
    name = '等等'
    list.append(1)
    print(list)
s()
print(list)
