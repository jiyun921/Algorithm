n = int(input())
l = [0] 
for i in range(n): 
    l.append(int(input()))

dp=[0]*(n+1)

dp[1] = l[1]
if n>=2 : 
    dp[2] = l[1]+l[2]

for i in range(3,n+1):
    dp[i] = max(dp[i-1], dp[i-2]+l[i], dp[i-3]+l[i-1]+l[i])

print(dp[n])

# top down 방식 : 시간 초과, recursion error(재귀 너무 깊음)
# def total(n): 
#     if n<2: 
#         dp[n] = l[n]
#         return dp[n]
    
#     if n==2 : 
#         dp[n] = l[n]+l[n-1]
#         return dp[n]
    
#     if dp[n]>0: 
#         return dp[n]
    
#     dp[n] = max(total(n-1), total(n-2)+l[n], total(n-3)+l[n-1]+l[n])
#     return dp[n]

# print(total(n))