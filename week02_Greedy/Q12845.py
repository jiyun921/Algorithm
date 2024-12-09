n = int(input())
L = list(map(int,input().split()))
L.sort(reverse=True)

gold = 0
for i in range(1,n): 
    gold += L[0]+L[i]

print(gold)


    