
n = 5

for i in range(0, n +1) :
    for j in range(i + 1) : 
        string = ' ' * (n - i) 
        string += '*' * (i)
        
    print(string,)
    
 
        