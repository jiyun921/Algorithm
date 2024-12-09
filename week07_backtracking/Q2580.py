
l = [list(map(int,input().split())) for i in range(9)]
blank = []
for i in range(9): 
    for j in range(9):
        if l[i][j] == 0 : 
            blank.append([i,j])

def backtrack(idx): 
    if idx==len(blank): 
        for i in l:
            for j in i : 
                print(j,end=' ')
            print() 
        exit(0)

    else : 
        i = blank[idx][0]
        j = blank[idx][1]
        for ans in range(1, 10):
            if check(i, j, ans):    
                l[i][j] = ans
                backtrack(idx + 1)
                l[i][j] = 0   



def check(i,j,ans): 

    for a in range(9): 
        if l[a][j] == ans or l[i][a]==ans: 
            return False 

    boxi = i//3 * 3 
    boxj = j//3 * 3 
    for x in range(3):
        for y in range(3):
            if l[boxi + x][boxj + y] == ans:
                return False 
    
    return True

backtrack(0)