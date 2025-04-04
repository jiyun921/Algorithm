import sys 
sys.setrecursionlimit(10 ** 6)

n =int(input())
map = [list(map(int,input().split())) for i in range(n)]
visited = [[-1]*n for i in range(n)]

def dfs(x,y): 
    if visited[x][y] != -1 : 
        return visited[x][y]

    visited[x][y] = 1
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if 0<=nx<n and 0<=ny<n and map[x][y]<map[nx][ny]:
            visited[x][y]= max(visited[x][y], 1+dfs(nx,ny))
    return visited[x][y]

maxdistance = 0
for i in range(n):
    for j in range(n): 
        maxdistance= max(maxdistance,dfs(i,j))

print(maxdistance)
