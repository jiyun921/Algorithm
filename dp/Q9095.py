t = int(input())

def findsum(n): 
    dp=[0]*(n+1)
    dp[1]=1
    if n>=2:
        dp[2]=2
        if n>=3: 
            dp[3]=4
    
    for i in range(4,n+1): 
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    
    print(dp[n])

for i in range(t):
    findsum(int(input()))