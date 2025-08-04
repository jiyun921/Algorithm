n,k = map(int,input().split())
l = []
for i in range(n): 
    l.append(int(input()))

dp = [0]*(k+1)
dp[0]=1

for i in l : 
    for j in range(i,k+1): 
        if j>=i : 
            dp[j] += dp[j-i]

print(dp[k])