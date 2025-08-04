
s = input() 
t = input() 

l=[]
l.append(t)
idx = 0 

while idx < len(l): 

    now = l[idx]
    idx += 1 

    if (len(now) == len(s) ) : 
        if now == s: 
            print(1)
            exit() 

    if(len(now)>len(s)) : 
        if (now[-1]=='A'): 
            r = now[:len(now)-1]
            l.append(r)

        if now[0] == 'B' : 
            tmp = now[1:]
            r = tmp[::-1]
            l.append(r)

print(0)
    
