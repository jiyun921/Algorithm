import sys
sys.setrecursionlimit(10**3)

n = int(input())
g = [list(map(int,input().strip())) for i in range(n)] 
visited = [[0]*n for i in range(n)]
result = []
cnt = 0 

def dfs(a,b):
    global cnt 
    if a<0 or a>=n or b<0 or b>=n : 
        return 
    g[a][b]= 0 
    visited[a][b] =1
    cnt += 1 

    dfs(a+1,b)
    dfs(a-1,b)
    dfs(a,b+1)
    dfs(a,b-1)

for i in range(n): 
    for j in range(n): 
        if visited[i][j] == 0 and g[i][j] ==1: 
            cnt =0 
            dfs(i,j)
            result.append(cnt)
            

print(len(result))
result.sort()
for i in result : 
    print(i)


