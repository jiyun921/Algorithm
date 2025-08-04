k,n = map(int, input().split())
len = []
for i in range(k) : 
    len.append(int(input()))

high = max(len)
low = 1

while low <= high : 
    mid = (low+high)//2
    num = 0
    for i in len : 
        num += i//mid
    if num >= n :
        result = mid
        low = mid + 1 
    else :  
        high = mid -1
print(result)