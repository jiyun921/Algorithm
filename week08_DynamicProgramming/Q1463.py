n = int(input())
dp = [0]*(n+1) 
dp[1]=0

for i in range(2,n+1): 
    findmin = [] 
    findmin.append(dp[i-1]+1)
    if i%3==0:
        findmin.append(dp[i//3]+1)
    if i%2==0:
        findmin.append(dp[i//2]+1)
    dp[i]=min(findmin)
    
print(dp[n])
