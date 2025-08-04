import sys
input = sys.stdin.readline 

def div_paper(n, paper):
    global cnt_white, cnt_blue

    if all(value == 0 for row in paper for value in row):
        cnt_white += 1
    elif all(value == 1 for row in paper for value in row):
        cnt_blue += 1    
    else: 
        smallpaperlst = [
            [row[:n//2] for row in paper[:n//2]],
            [row[n//2:] for row in paper[:n//2]],
            [row[:n//2] for row in paper[n//2:]],
            [row[n//2:] for row in paper[n//2:]]
        ]

        for smallpaper in smallpaperlst:
            div_paper(n//2, smallpaper)

def solve(): 
    n = int(input())
    paper = []
    for i in range(n):
        paper.append(list(map(int, input().split())))
    
    global cnt_white, cnt_blue
    cnt_white = 0
    cnt_blue = 0
    
    div_paper(n, paper)
    print(cnt_white)
    print(cnt_blue)

solve() 