list = [10,100,49,2,56,3,1,37]
for i in range(0,len(list)-1):
    for j in range(i+1,len(list)):
        if list[i] > list[j]:
            list[i],list[j]=list[j],list[i]
    print(list)
