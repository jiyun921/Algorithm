# 재귀함수로 구현  
def binarysearch(arr, target, start, end): 
    if start>end : 
        return -1 

    mid = (start+end)/2

    if arr[mid] == target: 
        return mid 
    else if (arr[mid]>target) : 
        return binarysearch(arr, target, start, mid-1)
    else : 
        return binarysearch(arr, taret, mid+1, end)
    
# 반복문으로 구현 
def binarysearch(arr, target, start, end): 
    while start<=end : 
        mid = (start+end)/2
        if arr[mid] == target: 
            return mid 
        else if (arr[mid]>target) : 
            end = mid - 1 
        else : 
            start = mid + 1 

    return -1
 

    