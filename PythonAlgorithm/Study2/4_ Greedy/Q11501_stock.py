import sys
input = sys.stdin.readline

def max_profit(prices): 
    profit = 0 
    while len(prices)>0 :
        max_price = max(prices)
        for i in range(len(prices)-1, -1, -1):
            if prices[i] == max_price: 
                max_idx = i 
                break 

        if max_idx != 0:
            profit += max_price * max_idx - sum(prices[:max_idx])
        prices = prices[max_idx+1:]
    print(profit)

def solve(): 
    t = int(input())
    for i in range(t): 
        n = int(input())
        prices = list(map(int,input().split()))
        max_profit(prices)

solve() 