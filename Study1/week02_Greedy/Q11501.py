t = int(input())
for i in range(t): 
    day = int(input())
    L = list(map(int,input().split()))
    
    result = 0 
    
    max= 0 
    for i in range(len(L)-1,-1,-1):
        if L[i]> max: 
            max = L[i] 
        result += max-L[i] 
    # 시간 초과 
    # while len(L)>0: 
    #     idx = L.index(max(L))
    #     result += L[idx] * idx - sum(L[:idx])
    #     L = L[idx+1:]
    
    print(result)
