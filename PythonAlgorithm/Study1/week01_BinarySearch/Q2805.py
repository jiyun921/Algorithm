n,m = map(int, input().split())

height = list(map(int, input().split()))

high = max(height)
low = 1
result = 0

while low<=high: 
    sum=0
    mid = (low+high)//2
    for i in height : 
        if i-mid>0:
            sum += i-mid 
    if sum >= m : 
        result = mid 
        low = mid+1
    else : 
        high = mid-1
        
print(result)