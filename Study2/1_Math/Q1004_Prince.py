def check_in_circle(circle, point):
    result =0 
    for c in circle: 
        InCircle = 0
        for p in point: 
            if ( (p[0]-c[0])**2 + (p[1] -c[1])**2 < c[2]**2 ) :
                InCircle += 1
        # 현재 원 안에 1개 점이 있는 경우  
        if (InCircle == 1) : 
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
   