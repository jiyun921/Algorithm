n = int(input())
l = []
for i in range(n) :
    l.append(list(map(int,input().split())))


result = [] 
for i in range(100,999) : 
    ia = i//100
    ib = i//10%10 
    ic = i%10 
    if (ia!=ib and ia!=ic and ib!=ic and ib!=0 and ic!=0) : 
        check = 0 
        for j in l :
            s=0
            b=0 
            
            ja = j[0]//100
            jb = j[0]//10%10
            jc = j[0]%10 

            if (ia==ja) : 
                s += 1 
            if (ib==jb): 
                s+= 1 
            if (ic==jc): 
                s+= 1 
            
            if (ia == jb or ia == jc) : 
                b += 1 
            if (ib == ja or jb == jc) : 
                b += 1
            if (ic == ia or ic == ib) : 
                b += 1 

            if (not (j[1]==s and j[2]==b)) : 
                check = 1
                break
        if check==0: 
            result.append(i) 

print(len(result))
            

        
