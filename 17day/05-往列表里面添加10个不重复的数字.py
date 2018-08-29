'''
list = []
import random
def addnum():
    while True:
        num = random.randint(1,100)
        if num not in list:
            list.append(num)
            list.sort()
        if len(list) == 10:
            break
    print(list)
    a=list[6]
    print(a)
    b = list.index(a)
    print(b)
addnum()
'''
list = []
import random
def addnum():
    while True:
        num = random.randint(1,100)
        if num not in list:
            list.append(num)
        if len(list) == 10:
            break
    print(list)
    a = list[6]
    print(a)
    list.sort()
    print(list)
    b = list.index(a)
    print(b)
addnum()
