from collections import deque 

n= int(input())
g= [] 
result = [] 

for i in range(n) :
    g.append(list(map(int,input().split())))

def bfs(x,y, depth) : 
    global cnt

    q = deque() 
    q.append((x,y))
    visited[x][y] = 1 

    while q : 
        a,b = q.popleft() 
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        for i in range(4) :
            nx = a + dx[i] 
            ny = b + dy[i]  
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0 and g[nx][ny]>depth:
                q.append((nx,ny))
                visited[nx][ny]=1 
    cnt +=1


for depth in range(101) : 
    cnt = 0 
    visited = [[0]*n for i in range(n)]
    for i in range(n) : 
        for j in range(n) : 
            if visited[i][j] == 0 and g[i][j]>depth : 
                bfs(i,j,depth)
                

    result.append(cnt)

print(max(result))

