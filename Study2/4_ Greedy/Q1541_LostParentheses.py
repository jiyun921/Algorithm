import sys
input = sys.stdin.readline

def plus_parentheses(n): 
    result = 0 
    
    minus_split = n.split('-')

    for i in range(len(minus_split)): 
        if '+' in minus_split[i] : 
            in_parentheses = sum(map(int, minus_split[i].split('+')))
        else : 
            in_parentheses = int(minus_split[i])

        if i == 0 : 
            result += in_parentheses
        else : 
            result -= in_parentheses

    print(result)

def solve(): 
    n = input().rstrip()
    plus_parentheses(n)

solve()