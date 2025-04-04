n,m = map(int,input().split())
result = [] 

def backtrack(): 
    if len(result) == m : 
        for i in result : 
            print(i, end =' ')
        print()
        
    else : 
        for i in range(1,n+1): 
            if i not in result: 
                result.append(i)
                backtrack() 
                result.pop() 
                
backtrack() 

