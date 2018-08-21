d = {'name':'翼泽','sex':'男','mz':'汉','age':16,'address':'河南','num':'411081200104036879'}
#遍历键
for i in d:
    print(d[i])
for i in d.keys():
    print(d[i])
#遍历值
for i in d.values():
    print(i)
#遍历键值对
for i in d.items():
    print(i)
    print(i[0])
    print(i[1])
for k,v in d.items():
    print(k)
    print(v)
