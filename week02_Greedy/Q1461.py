n,m = map(int,input().split())
L = list(map(int,input().split()))

L.sort()
sum = 0 
cnt1 = 0 #음수 개수 

for i in L : 
    if i<0: 
        cnt1 += 1 

cnt2 = n-cnt1 # 양수 개수 

for i in range(0, cnt1, m) :
    sum += 2 * abs(L[i])

for i in range(-1, -cnt2-1, -m) :
    sum += 2 * L[i]

if abs(L[0]) < abs(L[-1]) : 
    sum -= abs(L[-1])
else : 
    sum -= abs(L[0])

print(sum)
