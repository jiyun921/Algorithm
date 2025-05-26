import sys
input = sys.stdin.readline 

def z_div(n, xy):
    global order, r,c 

    if (n==2): 
        for i in range(2):
            for j in range(2):
                now_r = xy[0]+i
                now_c = xy[1]+j 
                if (now_r==r and now_c==c): 
                    print(order)
                    exit(0)
                order += 1 
    
    else : 
        xy_list = [[0,0], [0,n//2], [n//2,0], [n//2,n//2]]

        for offset in xy_list:
            new_x = xy[0] + offset[0]
            new_y = xy[1] + offset[1]
            z_div(n//2, [new_x,new_y])

def solve():
    global r,c
    n,r,c = map(int,input().split())

    global order
    order = 0 
    
    z_div(2**n, [0,0])

solve()