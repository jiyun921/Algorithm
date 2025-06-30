import sys 
input= sys.stdin.readline 

def compression(s, start, end):
    length = 0
    i = start
    while i <= end:
        
        if s[i].isdigit() and i+1 <= end and s[i+1] == '(':
            k = int(s[i])

            count = 1
            find_close = 0 
            for j in range(i+2, end+1): 
                if s[j] == '(':
                    count += 1
                elif s[j] == ')':
                    count -= 1
                if count == 0:
                    find_close = j 
                    break 
            
            length += k * compression(s, i+2, find_close-1)
            i = find_close + 1
        else:
            length += 1
            i += 1
    return length
    

def solve(): 
    s = input().rstrip() 
    print(compression(s, 0, len(s)-1))

solve()