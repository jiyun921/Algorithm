import sys
input = sys.stdin.readline 

def z_div(n, z_list, xy):
    global order
    if (n==2): 
        for i in range(2):
            for j in range(2):
                z_list[xy[0]+i][xy[1]+j] = order
                order += 1 
    
    else : 
        xy_list = [[0,0], [0,n//2], [n//2,0], [n//2,n//2]]

        for offset in xy_list:
            new_x = xy[0] + offset[0]
            new_y = xy[1] + offset[1]
            z_div(n//2, z_list, [new_x,new_y])

def solve():
    n,r,c = map(int,input().split())

    z_list =  [[0]*(2**n) for i in range(2**n)]
    global order
    order = 0 
    
    z_div(2**n, z_list, [0,0])
    print(z_list[r][c])

solve()