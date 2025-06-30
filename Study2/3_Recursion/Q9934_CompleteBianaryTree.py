import sys
input = sys.stdin.readline 

def div_tree(start, end, level):
    if start>end:
        return 
    else : 
        mid = (end-start+1) // 2
        tree[level].append(visit[start+mid])
        
        div_tree(start, start+mid-1, level+1)
        div_tree(start+mid+1, end, level+1)

def solve(): 
    k = int(input())
    global visit, tree 
    visit = list(map(int,input().split()))
    tree = [[] for i in range(k)]

    div_tree(0, 2**k-2, 0)

    for i in tree: 
        print(*i)
    
solve()
