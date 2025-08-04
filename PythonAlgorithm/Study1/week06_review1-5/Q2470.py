n = int(input())
l = list(map(int, input().split()))

l.sort()

goal1, goal2 = 0, 1
start = 0 
end = n - 1

while start < end: 
    sum = l[start] + l[end]
    
    if abs(l[goal1] + l[goal2]) > abs(sum): 
        goal1, goal2 = start, end
    
    if sum > 0:
        end -= 1 
    elif sum < 0: 
        start += 1 
    else: 
        goal1, goal2 = start, end 
        break

print(l[goal1], l[goal2])

    


# 완전 탐색 풀이 -> 시간초과 
# goal1, goal2 = 0,1
# for i in range(n): 
#     for j in range(i+1,n): 
#         if abs(l[goal1]+l[goal2]) > abs(l[i]+l[j]): 
#             goal1, goal2 = i,j

# print(goal1, goal2)

            