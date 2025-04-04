import itertools 

n,s = map(int,input().split())
l = list(map(int,input().split()))
cnt = 0 

for i in range(n) : 
    for j in itertools.combinations(l,i+1): 
        if sum(j) == s : 
            cnt += 1 

print(cnt)