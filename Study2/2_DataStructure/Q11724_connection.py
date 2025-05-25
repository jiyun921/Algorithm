import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int,input().split())
graph = [[] for i in range(N+1)]

for i in range(M): 
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N+1)
cnt = 0

def dfs(graph, u, visited) : 
    visited[u] = True 

    for v in graph[u] : 
        if not visited[v] : 
            dfs(graph,v,visited) 
            

for i in range(1, N+1) :
    if not visited[i] : 
        dfs(graph, i, visited)
        cnt += 1

print(cnt)
