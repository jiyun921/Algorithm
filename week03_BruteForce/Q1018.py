n,m = map(int, input().split()) 
a = []
result = []

for i in range(n) : 
    a.append(list(input()))

for i in range(n-7):
    for j in range(m-7):
        check1 = 0 # B먼저 
        check2 = 0 # W먼저 
       
        for k in range(i,i+8) : 
            for l in range(j,j+8) : 
                if (k+l)%2==0: 
                    if a[k][l] != 'B' : 
                        check1 += 1 
                    else : 
                        check2 += 1 
                else : 
                    if a[k][l] != 'W' :
                        check1 += 1 
                    else : 
                        check2 += 1 
    
        result.append(min(check1,check2))

print(min(result))
                        