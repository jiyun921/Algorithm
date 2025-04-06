from math import sqrt 
def LeastMove(x,y):
    # 두 점 사이의 거리 
    len = y-x 
    # 최소 이동 횟수 
    result = 0 
    
    max = int(sqrt(len))
    
    if (len == max**2) :
        result = 2*max-1 
    elif (len <= max*(max+1)) :
        result = 2*max
    else :
        result = 2*max+1 
    
    print(result)
    

T = int(input())
for i in range(T):
    x,y = map(int,input().split())
    LeastMove(x,y)