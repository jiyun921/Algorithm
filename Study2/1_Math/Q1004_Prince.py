def check_in_circle(circle, point):
    result = 0 
    for c in circle: 
        for p in point: 
            if ( (p[0]-c[0])**2 + (p[1] -c[1])**2 < c[2]**2 ) :
                result += 1 
    
    print(result)

T = int(input())
for i in range(T) : 
    pointinput = list(map(int,input().split()))
    point = [pointinput[:2], pointinput[2:]]

    n = int(input())
    circle = [] 
    for i in range(n): 
        circle.append(list(map(int,input().split()))) 
    check_in_circle(circle, point)
   