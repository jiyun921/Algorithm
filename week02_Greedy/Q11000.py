n = int(input())
T = []
for i in range(n): 
    T.append(list(map(int,input().split())))

T.sort()
result = []
result.append(T[0][1])

for i in range(1,n): 
    check = False 
    for j in result : 
        if T[i][0] >= j: 
            result.remove(j)
            result.append(T[i][1])
            check = True
            break 
    if not check : 
        result.append(T[i][1])

print(len(result))
