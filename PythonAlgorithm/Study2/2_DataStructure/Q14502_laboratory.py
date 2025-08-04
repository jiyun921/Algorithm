import sys 
input = sys.stdin.readline 
from collections import deque 
from itertools import combinations 

N,M = map(int,input().split()) 
graph = []
for i in range(N) : 
    graph.append(list(map(int,input().split())))

def bfs(graph, x, y) : 
    queue = deque([(x,y)])
    visited[x][y] = True 

    while queue : 
        x,y = queue.popleft()
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]

        for i in range(4) : 
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 0 : 
                queue.append((nx,ny))
                visited[nx][ny] = True
                graph[nx][ny] = 2 


ableWall = []        
for i in range(N) :
    for j in range(M) : 
        if graph[i][j] == 0 : 
            ableWall.append((i,j))

Wall = list(combinations(ableWall,3))

maxSafeCnt = 0 
for i in Wall :
    copygraph = [row[:] for row in graph]
    visited = [[False]*M for i in range(N)] 
    
    # 벽 3개 세우기 
    for (x,y) in i : 
        copygraph[x][y] = 1
    
    # 바이러스 퍼뜨리기 
    for i in range(N) :
        for j in range(M) : 
            if copygraph[i][j] == 2 and not visited[i][j] : 
                bfs(copygraph,i,j)
    
    # 안전영역 개수 세기 
    SafeCnt = 0 
    for i in range(N) :
        for j in range(M) : 
            if copygraph[i][j] == 0 : 
                SafeCnt += 1
    
    maxSafeCnt = max(maxSafeCnt, SafeCnt)

print(maxSafeCnt)



