n = int(input())
m = int(input())
g = [[] for i in range(n+1)]

for i in range(m) : 
    a,b= map(int,input().split())
    g[a].append(b)
    g[b].append(a) 

visited = [0 for i in range(n+1)]

def dfs (node) : 
    visited[node]= 1 

    for next in g[node] : 
        if visited[next] == 1 : 
            continue
        dfs(next) 

dfs(1)
print(sum(visited)-1)
