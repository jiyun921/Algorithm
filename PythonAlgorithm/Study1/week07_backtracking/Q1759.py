l,c = map(int,input().split())
s = list(input().split())
s.sort()
result = [] 

def backtrack(num) : 
    if len(result) == l : 
        cnt = 0 
        for i in result : 
            if i in ['a','e','i','o','u']:
                cnt += 1 

        if 1<=cnt<=len(result)-2 : 
            for i in result : 
                print(i,end='')
            print()

    else : 
        for i in range(num,c): 
            result.append(s[i])
            backtrack(i+1)
            result.pop()

backtrack(0)
