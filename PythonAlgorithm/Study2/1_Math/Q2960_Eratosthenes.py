N,K = map(int,input().split())

E= [True] * (N+1)
E[0], E[1] = False, False

removenum = []

while any(E):
    for i in range(2, N+1):
        if E[i] == True:
            P = i
            break
    
    for i in range(P, N+1, P):
        if E[i] == True:
            E[i] = False
            removenum.append(i)

print(removenum[K-1])
