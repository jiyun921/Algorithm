def LeastMove(x,y):
    # 현재 위치에서 y 지점까지 남은 거리 (마지막 한칸 제외)
    len = y-x-1
    # 이동횟수 
    result = 0
    # k 광년만큼 이동 
    k = 0 

    while (len > 0):
        len -= k
        if (k!=0):
            result+=1    
        
        if (len == k+1 or len >= 2*k): 
            k+=1
        elif (len == k or len >= 2*k-1):
            continue
        else :
            k-=1 

    # +1은 마지막 한칸 
    print(result+1)

T = int(input())
for i in range(T):
    x,y = map(int,input().split())
    LeastMove(x,y)
    