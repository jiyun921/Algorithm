n = int(input()) 
point = []
point.append(0)
for i in range(n): 
    point.append(int(input()))

total=[0]*(n+1)
def totalmax(i):
    if i<2 : 
        total[i] = point[i]
        return total[i] 
    if i==2: 
        total[i]= point[i]+point[i-1]
        return total[i]
    if (total[i]>0):
        return total[i]
    total[i] = point[i]+ max((point[i-1]+totalmax(i-3)),(totalmax(i-2)))
    return total[i]

print(totalmax(n))