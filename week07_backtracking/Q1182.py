n,s = map(int,input().split())
l = list(map(int,input().split()))
result = []
cnt = 0 

def backtrack(idx): 
    global cnt
    if len(result)>0 and sum(result) == s : 
        cnt += 1 
    
    for i in range(idx,n):
        result.append(l[i])
        backtrack(i+1)
        result.pop()

backtrack(0)
print(cnt)