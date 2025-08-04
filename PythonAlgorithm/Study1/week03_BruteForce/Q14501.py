n = int(input())
L = []
for i in range(n):
    L.append(list(map(int,input().split())))

def profit(t,p):
    if t>=n: 
        return p 
    
    add=0 
    if t+L[t][0]<=n:
        add = profit(t+L[t][0], p+L[t][1])
    skip = profit(t+1, p)

    return max(add,skip)

result = []
for i in range(n):
    result.append(profit(i,0))    

print(max(result))


