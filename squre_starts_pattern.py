

def squreStart(row) :
    
    try : 
        
        for i in range(1, row+1) :
            for j in range(i+1) :
                string = row * '*'
            print(string)
    except :
        print('only digit allowed.') 
    
squreStart(7)