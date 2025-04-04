def Turret(x1,y1,r1,x2,y2,r2):
        result = 0 
        distance = (x1-x2)**2 + (y1-y2)**2 # 두 좌표 사이의 거리 
        sum_r = (r1+r2)**2 # 두 원의 반지름의 합의 제곱 
        diff_r = (r1-r2)**2 # 두 원의 반지름의 차의 제곱 
        
        if distance == 0 : 
            if r1==r2 : # 2개가 같은 원 
                result = -1 
            else : # 중심은 같지만 한 원이 다른 원 안에 있음 
                result = 0     
        else : 
            if distance == sum_r : # 외접 
                result = 1 
            elif distance > sum_r : # 두 원이 떨어져있음 
                result = 0
            elif distance == diff_r : # 내접 
                result = 1
            elif distance < diff_r : # 한 원이 다른 원 안에 있음 
                result = 0 
            else : # 두 원이 두 점에서 만남 
                result = 2
        print(result)

T = int(input())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    Turret(x1,y1,r1,x2,y2,r2) 
        