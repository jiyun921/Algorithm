import sys
input = sys.stdin.readline 

unheard = set()
unseen = set()

N,M = map(int,input().split())
for i in range(N) : 
    unheard.add(input().strip())

for i in range(M) : 
    unseen.add(input().strip())

bothunknown = sorted(unheard&unseen) 
print(len(bothunknown))
for i in bothunknown : 
    print(i)
