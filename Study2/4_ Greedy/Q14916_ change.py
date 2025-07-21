import sys
input = sys.stdin.readline

def change(n): 
    count5 = 0 
    count2 = 0 

    while n>0 : 
        if n % 5 == 0: 
            count5 += n // 5
            n = n % 5 
            break 

        count2 += 1
        n -= 2
        

    if n == 0 : 
        print(count5 + count2)
        return  
    else : 
        print(-1)
        return 


def solve(): 
    n = int(input())
    change(n)
    
solve()