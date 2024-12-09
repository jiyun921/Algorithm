from collections import deque

L = []
for i in range(5): 
    L.append(list(map(int, input().split())))
result = set()

def bfs(x, y):
    q = deque()
    q.append((x, y, str(L[x][y]))) 

    while q:
        a, b, num = q.popleft()

        if len(num) == 6:
            result.add(num)
            continue

        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5:
                q.append((nx, ny, num + str(L[nx][ny])))  


for i in range(5):
    for j in range(5):
        bfs(i, j)

print(len(result))
