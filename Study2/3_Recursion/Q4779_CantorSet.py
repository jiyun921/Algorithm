import sys


def div_line(n, start, end):
    if n == 0:
        return  
    else:
        mid = (end-start+1) // 3

        #가운데 문자열을 공백으로 바꿈 
        result[start+mid:start+mid+mid] = ' '*mid 

        div_line(n - 1, start, start+mid-1)
        div_line(n - 1, start+mid+mid, end)
        
def solve():
    for line in sys.stdin:
        n = int(line.strip())  
        global result
        result = ['-'] * (3**n) 
        div_line(n, 0, 3**n - 1)
        print(''.join(result))

solve()