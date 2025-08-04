n = int(input())

dp = [[0]*10 for i in range(n+1)]

for i in range(1,10):
    dp[1][i]=1

for i in range(2,n+1):
    for j in range(10):
        if dp[i-1][j]>=1 : 
            if j==0 : 
                dp[i][j+1] += dp[i-1][j]
            elif j==9 : 
                dp[i][j-1] += dp[i-1][j] 
            else : 
                dp[i][j+1] += dp[i-1][j]
                dp[i][j-1] += dp[i-1][j] 
        

print(sum(dp[n])%1000000000)
