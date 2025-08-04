n = int(input())
num = list(map(int,input().split()))

af= min(num[0],num[-1])
be = min(num[1],num[-2])
cd = min(num[2],num[-3])

sum3 = af + be + cd
sum2= sum3 - max(af,be,cd)

result =0 
if n==1 : 
    for i in num: 
        result += i
    result -= max(num)
elif n==2 : 
    result += sum3*4 + sum2*4  
else :
    result += sum3*4
    result += sum2*(4*(n-1)+4*(n-2))
    result += min(num) * ((n-2)*(n-2) + 4*(n-2)*(n-1))

print(result)