
rows = int(input('enter the numbers of rows ? ').strip()) 

for i in range(rows) : 
    string = ' ' * (rows - i - 1)
    string += '* ' * (i + 1)
    print(string)
for i in range(rows-1, 0, -1) : 
    string = ' ' * (rows - i)
    string += '* ' * i 
    
    print(string)