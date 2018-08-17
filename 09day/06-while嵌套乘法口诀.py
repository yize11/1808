'''
i = 1
while i< 8:
    j = 1
    while j<5:
        print('*',end='\t')
        j+=1
    print('')
    i+=1
'''
'''
i = 1
while i < 8:
    j = 1
    while j <= i:
        print('*',end='\t')
        j+=1
    print('')
    i+=1
'''
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print('%d*%d=%d'%(i,j,i*j),end='\t')
        j+=1
    print('')
    i+=1
