import itertools 
n,m = map(int,input().split())
l = list(map(int,input().split()))

a = itertools.combinations(l,3);
r= []
for i in a : 
    if sum(i)<=m: 
        r.append(sum(i))

print(max(r)) 
        
