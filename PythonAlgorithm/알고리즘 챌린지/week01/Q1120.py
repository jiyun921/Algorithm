a, b = input().split()

result = 50
for i in range(len(b)-len(a)+1): 
    n = 0 
    for j in range(len(a)): 
        if a[j]!=b[i+j]: 
            n += 1 
    result = min(n, result)

print(result)
