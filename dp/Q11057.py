n = int(input())

dp = [[0]*10 for i in range(n+1)]
for i in range(10): 
    dp[1][i] = 1 

for i in range(2,n+1):
    for j in range(10): 
        k = j 
        while k<=9 : 
            dp[i][k] += dp[i-1][j]  
            k+=1 

print(sum(dp[n])%10007)
