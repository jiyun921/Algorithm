import sys
input = sys.stdin.readline

def count_NewEmployee(rank):
    rank.sort()

    pass_cnt = 1
    prev_pass_interview_rank = rank[0][1]
    
    for i in range(1, len(rank)): 
        if rank[i][1] < prev_pass_interview_rank: 
            pass_cnt += 1
            prev_pass_interview_rank = rank[i][1]

    print(pass_cnt)


def solve(): 
    t = int(input())
    for i in range(t): 
        n = int(input())
        rank = []
        for i in range(n): 
            rank.append(list(map(int, input().split())))
        count_NewEmployee(rank)

solve()