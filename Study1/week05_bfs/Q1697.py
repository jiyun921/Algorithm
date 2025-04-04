from collections import deque 
n,k = map(int,input().split())
distance = [-1]*100001 

def bfs(v) :
    q = deque()
    q.append(v)
    distance[v] = 0 
    while q : 
        x = q.popleft()

        if x==k : 
            break 

        dx = [1,-1,x]
        for i in dx : 
            nx = x + i 
            if 0<=nx<=100000 and distance[nx] == -1: 
                q.append(nx)
                distance[nx] = distance[x]+1 

    return distance[k]

print(bfs(n))
