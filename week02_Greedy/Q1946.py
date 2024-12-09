T = int(input())

for i in range(T) : 
    N = int(input())
    grade = []
    for i in range(N) : 
        a, b = map(int,input().split())
        grade.append((a, b))
    grade.sort()
   
    result = []
    result.append(grade[0])
    
    for i in range(1,N) :
        if grade[i][1] < result[-1][1] : 
            result.append(grade[i])
    
    print(len(result))

         
