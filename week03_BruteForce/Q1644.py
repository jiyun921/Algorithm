n= int(input())

import math
n= 4000000
array = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n))+1) : 
    if array[i] == True: 
        j = 2 
        while i*j <=n: 
            array[i*j] = False 
            j+=1 

prime = [] 
for i in range(2,n+1) : 
    if (array[i]) : 
        prime.append(i) 

sum = [0]*(len(prime)+1)
for i in range(len(prime)): 
    sum[i+1] = sum[i]+ prime[i]

start = 0 
end = 1 
cnt = 0 
while start < len(sum) and end < len(sum) : 
    if sum[end]- sum[start] > n : 
        start+= 1 
    elif sum[end]-sum[start] < n : 
        end += 1 
    else : 
        cnt += 1 
        start +=1 
        end = start 
print(cnt)