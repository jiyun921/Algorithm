t = int(input())

for i in range(t): 
    n = int(input())
    l = [] 
    l.append(list(map(int,input().split())))
    l.append(list(map(int,input().split())))

    dp = [[0]*n for i in range(2)]
    dp[0][0] = l[0][0]
    dp[1][0] = l[1][0]
    if n>1 : 
        dp[0][1] = l[0][1] + l[1][0] 
        dp[1][1] = l[1][1] + l[0][0]   

    for i in range(2,n): 
        dp[0][i] = l[0][i]+max(dp[1][i-1], dp[1][i-2])
        dp[1][i] = l[1][i]+max(dp[0][i-1], dp[0][i-2])

    print(max(dp[0][n-1],dp[1][n-1]))    
