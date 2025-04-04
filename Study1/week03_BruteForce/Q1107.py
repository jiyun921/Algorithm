import itertools 
now = 100 
n = input() 
m = int(input())
x = [str(i) for i in range(10)]

if m==0 : 
    if n==100 : 
        print(0)
    else : 
        print(min(abs(now-int(n)),len(n)))
    exit(0)

l = list(map(int,input().split()))
for j in l : 
    x.remove(str(j))

m = 5000001
for l in range(len(n)-1,len(n)+2):
    if l==0 : 
        continue
    for i in itertools.product(x,repeat=l): 
        num = int(''.join(i))
        m = min(abs(num-int(n))+l,m) 

if m > abs(now-int(n)): 
    m = abs(now-int(n))

print(m)
    
