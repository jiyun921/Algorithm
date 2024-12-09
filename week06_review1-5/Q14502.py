from collections import deque
from itertools import combinations 

n,m = map(int,input().split())
orginalmap=[list(map(int,input().split())) for i in range(n)]


def bfs(map,x,y) : 
    q = deque() 
    q.append((x,y)) 
    visited[x][y]=1

    while q : 
        a,b = q.popleft() 
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        for i in range(4) : 
            nx = a + dx[i]   
            ny = b + dy[i] 
            if (0<=nx<n and 0<=ny<m and visited[nx][ny]==0 and map[nx][ny]==0 ) : 
                visited[nx][ny]=1
                q.append((nx,ny))
                map[nx][ny] = 2 


blank = [(x,y) for x in range(n) for y in range(m) if orginalmap[x][y]==0]
newwall =  list(combinations(blank,3))
cntlist = []

for i in newwall : 
    visited = [[0]*m for i in range(n)]
    map = [row[:] for row in orginalmap]
    for x,y in i : 
        map[x][y]=1

    for k in range(n):
        for l in range(m): 
            if map[k][l]==2 : 
                bfs(map,k,l)
                
    cnt = 0 
    for k in range(n):
        for l in range(m):
            if map[k][l]==0 : 
                cnt += 1 
    cntlist.append(cnt)

print(max(cntlist))
                    


    