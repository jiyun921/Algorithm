n = int(input())
t = []
for i in range(n) : 
    s,e = map(int,input().split())
    t.append([s,e])

t.sort(key = lambda x: (x[1], x[0])) #1번째 인덱스 기준 오름차순 정렬, 동일한 경우 0번째 인덱스 기준

result = []
result.append(t[0])

cnt = 0
for i in t[1:] : 
    if (i[0]>=result[cnt][1]) : 
        cnt+=1
        result.append(i)

print(len(result))
    
