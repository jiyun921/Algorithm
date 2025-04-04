n = int(input())
good=[]

def backtrack():
    if len(good)==n :
        goodstr = ''.join(good)
        print(goodstr)
        exit(0)
    
    else : 
        for i in ['1','2','3'] : 
            good.append(i)
            if check() : 
                backtrack()
            good.pop() 

def check() : 
    for i in range(1,len(good)//2+1) : 
        if good[-i:] == good[-2*i:-i]:
            return False 
    return True 
    
backtrack() 
