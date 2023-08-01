
def getNumberOfRows(): 
    
    try :
        row = int(input('enter the number of row ? ').strip())

        return row
    except :
        
        return 'enter a digits only'

for row in range(0, getNumberOfRows()+1) :
    for col in range((1 * row) + row-1) :
        print('*', end=' ')
    print()