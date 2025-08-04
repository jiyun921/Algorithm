n,m = map(int,input().split())
l = [[] for i in range(n)]
for i in range(n): 
    s=input()
    for c in s : 
        l[i].append(int(c))

size = min(n,m)

for k in range(size,0,-1): 
    for i in range(n-k+1):
        for j in range(m-k+1):
            if l[i][j] == l[i+k-1][j] == l[i][j+k-1] == l[i+k-1][j+k-1]: 
                print(k*k)    
                exit(0)  
