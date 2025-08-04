import sys
sys.setrecursionlimit(10**5)

n = int(input())
g = [] 
visited = [[0]*n for i in range(n)]
for i in range(n): 
    g.append(list(input()))
    
cnt1 = 0 
cnt2 =0 

def dfs(x,y,color):
    visited[x][y] = 1 
    dx=[-1,0,1,0]
    dy=[0,-1,0,1]
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if (0<=nx<n-1) and (0<=ny<n-1) and visited[nx][ny]==0:
            if g[ny][nx]== color:
                dfs(nx,ny,color)

for c in ['R', 'G', 'B'] : 
    for i in range(n) : 
        for j in range(n) : 
            if visited[i][j] == 0  and g[i][j]==c : 
                dfs(i,j,c) 
                cnt1 +=1 


for i in range(n):
    for j in range(n):
        if g[i][j] == 'G':
            g[i][j] = 'R'

visited = [[0]*n for i in range(n)]

for c in ['R', 'B'] : 
    for i in range(n) : 
        for j in range(n) : 
            if visited[i][j] == 0  and g[i][j]==c : 
                dfs(i,j,c) 
                cnt2 +=1 

print(cnt1,cnt2)