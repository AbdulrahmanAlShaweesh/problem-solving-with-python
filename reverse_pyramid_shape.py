

rows = int(input('enter the number of rows ? ').strip())

for row in range(rows, 0, -1) :
    for col in range((rows - row)) : 
        print(end=' ')
    for star in range(row) : 
        print('*', end=' ') 
    print() 
        
    