

rows = 5

for i in range(rows) :
    
    for j in range(rows - i - 1) :
        print(end=' ') 
    
    for k in range(0, i+1) :
        print('*', end=' ')
    print('\n')