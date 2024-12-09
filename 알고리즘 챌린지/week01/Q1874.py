from collections import deque 
s = deque()
n = int(input())
l = [] 
result = [] 
now = 1 
for i in range(n):
    x = int(input()) 
    while now <= x : 
        s.append(now)
        result.append('+')
        now += 1 
       
    if s[-1] == x : 
        s.pop()
        result.append('-')
    else : 
        print('NO')
        exit(0)

for i in result : 
    print(i)
