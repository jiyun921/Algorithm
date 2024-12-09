from collections import deque 
n,m = map(int,input().split())
l = list(map(int,input().split()))
q = deque([i for i in range(1,n+1)])

cnt = 0 
for i in l : 
    while True: 
        if i==q[0] :
            q.popleft()
            break 
        elif q.index(i) <= len(q)//2 : 
            q.append(q.popleft())
            cnt += 1 
        else : 
            q.appendleft(q.pop())
            cnt += 1 

print(cnt)

