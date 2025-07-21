import sys
input = sys.stdin.readline 

def min_distance(n): 
    global X,A

    result = []

    sum_distance = 0 

    for i in range(n):     
        for j in range(n): 
            sum_distance += abs(X[i]-X[j]) * A[j]
        result.append(sum_distance)
        sum_distance = 0
    print(X[result.index(min(result))])
    

def solve(): 
    global X,A
    X = []
    A = [] 
    n = int(input())
    for i in range(n): 
        x,a = map(int, input().split())
        X.append(x)
        A.append(a)
    min_distance(n)

solve() 