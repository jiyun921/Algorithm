import sys 
input = sys.stdin.readline

def pick_lotto(S, pick, S_idx):
    if len(pick) == 6:
        print(*pick)
        
    else: 
        for i in range(S_idx, len(S)):
            pick.append(S[i])    
            pick_lotto(S, pick, i+1)
            pick.pop()


def solve():
    while (True):
        S = list(map(int,input().split()))
        k = S[0]
        if k == 0:
            break
        S = S[1:]

        pick = [] 
        pick_lotto(S, pick, 0)
        print() 

solve() 