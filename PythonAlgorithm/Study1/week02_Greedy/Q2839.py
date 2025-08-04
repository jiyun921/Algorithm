n = int(input())
cnt = 0 

while n>0 :
    if n%5 ==0: 
        cnt += n//5 
        n = n%5 
        break 

    if n>=3 : 
        n -= 3 
        cnt += 1 
    else : 
        print(-1)
        exit(0)

print(cnt)
