# 반복문 
# n = 3
# for i in range(n): 
#     for j in range(n): 
#         if (i==j):
#             continue 
#         for k in range(n): 
#             if (k==i or k==j): 
#                 continue 
#             print(i,j,k)
            
#  파이썬 함수 
# import itertools 
# l = [1,2,3]
# result = list(itertools.permutations(l))
# print(result)

# result = list(itertools.permutations(l,2))
# print(result)

# 재귀함수 
n = 3 
r = 2  

l = [1,2,3]
result = [0] * r 
check = [ False ] * n

def per(n,r,idx) : 
    if idx==r: 
        print(result)
        return 
    else : 
        for i in range(n): 
            if not check[i] :
                check[i] = True 
                result[idx] = l[i]

                per(n,r,idx+1)
    
                check[i] = False 

per(n,r,0)