L = input().split('-')

result = 0
check = 0
for i in L: 
    i = sum(map(int, i.split('+')))
    if check==0 :
        result += i
        check = 1
        continue
    result -= i


print(result)