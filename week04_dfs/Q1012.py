import sys
sys.setrecursionlimit(50000)
t = int(input())

for i in range(t):
    m,n,k = list(map(int,input().split()))
    g = [[0]* m for i in range(n)]
    for i in range(k): 
        y,x = list(map(int,input().split()))
        g[x][y] = 1 
    
    def dfs(x,y):
        dx=[-1,0,1,0]
        dy=[0,-1,0,1]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if (0<=nx<m) and (0<=ny<n):
                if g[ny][nx]==1:
                    g[ny][nx]=-1
                    dfs(nx,ny)


    result = 0 
    for i in range(m):
        for j in range(n): 
            if graph[j][i]==1:
                dfs(i,j)
                result += 1 
    print(result)