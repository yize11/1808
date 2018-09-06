list = []
for i in range(0,101):
    if i%2 == 0:
        list.append(i)
list.sort(reverse=True)
print(list)
list.insert(10,99)
print(list)
list.pop(11)
print(list)
print(sum(list))

