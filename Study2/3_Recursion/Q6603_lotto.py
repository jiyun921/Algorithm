import sys 
input = sys.stdin.readline
from itertools import combinations

while (True):
    S = list(map(int,input().split()))
    k = S[0]
    if k == 0:
        break
    S = S[1:]
    pick = list(combinations(S, 6))
    for i in pick :
        print(*i)
    print() 