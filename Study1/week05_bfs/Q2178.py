from collections import deque 

n,m = map(int,input().split())
g = [[] for i in range(n)] 
distance = [[0]*m for i in range(n)] 

for i in range(n) : 
    num = input()
    for j in num : 
        g[i].append(int(j))

def bfs(x,y) : 
    q = deque()
    q.append((x,y))
    distance[x][y] = 1 

    while q: 
        a,b = q.popleft()
        if (a,b) == (n-1,m-1):
            break

        dx=[-1,0,1,0]
        dy=[0,-1,0,1]
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if (0<=nx<n) and (0<=ny<m) and distance[nx][ny]==0 and g[nx][ny]==1:
                q.append((nx,ny))
                distance[nx][ny] = distance[a][b] + 1  

    return distance[n-1][m-1] 

print(bfs(0,0))




                

            
