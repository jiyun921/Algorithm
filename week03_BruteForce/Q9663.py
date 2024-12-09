n = int(input())

result = 0 
l = [-1]*n  # l[x좌표] = y좌표

def queen(x):
    global result  
    if x == n : 
        result += 1 
        return 
    else : 
        for j in range(n): 
            if check(x,j): 
                l[x] = j      
                queen(x+1)
                      

def check(a,b): 
    for i in range(a): 
        if l[i] == b or a-b == i-l[i] or a+b == i+l[i]: 
            return False 
    return True 

queen(0)
print(result)