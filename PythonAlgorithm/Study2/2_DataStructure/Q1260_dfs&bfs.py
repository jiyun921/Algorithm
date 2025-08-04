from collections import deque

N,M,V = map(int, input().split())

graph = [[] for i in range(N+1)]
visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)

for i in range(M) :
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph :
    g.sort()

def dfs(graph, V, visited) :
    visited[V] = True
    print(V, end=' ')

    for i in graph[V] :
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, V, visited) :
    queue = deque([V])
    visited[V] = True

    while queue :
        V = queue.popleft()
        print(V, end=' ')

        for i in graph[V] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True

dfs(graph, V, visited_dfs)
print()
bfs(graph, V, visited_bfs)
