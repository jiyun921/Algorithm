from collections import deque 

m,n = map(int,input().split())
g=[]

for i in range(n): 
    g.append(list(map(int,input().split()))) 

def bfs(x,y) : 

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
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0 and g[nx][ny]==0:
                q.append((nx,ny))
                g[nx][ny] = 1 
                visited[nx][ny]=1

day = 0       
while any(0 in row for row in g) : 
    visited = [[0]*n for i in range(n)]
    for i in range(n) : 
        for j in range(n) : 
            if g[i][j] == 0 : # 토마토가 모두 익지 못할 때 
                dx = [-1,1,0,0]
                dy = [0,0,-1,1]
                check= False 
                for k in range(4) :
                    ni = i + dx[k] 
                    nj = j + dy[k]
                    if 0<=ni<n and 0<=nj<n and g[ni][nj]!=-1:
                        check = True
                        break
                if not check: 
                    print(-1)
                    exit(0)

            if visited[i][j] == 0 and g[i][j]==1 : 
                bfs(i,j)
    day +=1 

print(day)

