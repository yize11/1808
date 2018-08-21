d = {'name':'翼泽','sex':'男','mz':'汉','age':16,'address':'河南','num':'411081200104036879'}
#添加
d ['edu'] = '高中'
print(d)
#修改
d ['age'] = '17'
print(d)
#删除
d.pop('name')
#del d['name']
print(d)
#查
#print(d['name'])#没有键会报错
print(d.get('name'))#没有键  返回None
