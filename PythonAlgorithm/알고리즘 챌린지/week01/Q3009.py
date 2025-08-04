L = []
for i in range(3):
    L.append(list(map(int,input().split())))

if L[0][0] == L[1][0] : 
    print(L[2][0], end=' ')
elif L[0][0] == L[2][0]: 
    print(L[1][0], end=' ')
else : 
    print(L[0][0], end=' ')

if L[0][1] == L[1][1] : 
    print(L[2][1])
elif L[0][1] == L[2][1]: 
    print(L[1][1])
else : 
    print(L[0][1])

