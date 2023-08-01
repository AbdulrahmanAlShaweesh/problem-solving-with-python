
try : 
    row = int(input('enter number of rows ? ').strip())
    
    for i in range(1 , row+1) :
        for j in range(i) : 
            print('*', end='')
        print()
            # pattern = j * '*' 
        # print(pattern) 
except: 
    print('only digits allowed')
    