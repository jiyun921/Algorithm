n,c = map(int,input().split())
x=[]
for i in range(n): 
    x.append(int(input()))
x.sort()

low = 1
high = x[-1]-x[0]

while low<=high: 
    mid= (low+high)//2
    count = 1 
    pre = 0
    for i in range(1,n): 
        if (x[i]-x[pre]) >= mid: 
            pre = i 
            count += 1 
    if count >= c : 
        result = mid 
        low = mid+1 
    else :
        high = mid-1 

print(result)
