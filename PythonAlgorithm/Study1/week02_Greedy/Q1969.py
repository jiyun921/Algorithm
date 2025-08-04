N, M = map(int, input().split())
dna = []

for i in range(N):
    dna.append(list(input()))

result = []
sum=0
for i in range(M):
    count = [0, 0, 0, 0] 
    for j in range(N):
        if dna[j][i] == 'A':
            count[0] += 1
        elif dna[j][i] == 'C':
            count[1] += 1
        elif dna[j][i] == 'G':
            count[2] += 1
        else:
            count[3] += 1
    
    if count.index(max(count)) == 0:
        result.append('A')
    elif count.index(max(count)) == 1:
        result.append('C')
    elif count.index(max(count)) == 2:
        result.append('G')
    else:
        result.append('T')
    
    sum += N-max(count)

print(''.join(result))
print(sum)
