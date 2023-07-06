"""
Problem Statement:
"""

arr=[4, 3, 5, 8, 10]
def subset_sum(arr, sum, n)->bool:
    
    if(sum==0):
        return True
    if(n==0):
        return False
    
    if(arr[n-1]<=sum):
        return (subset_sum(arr, sum-arr[n-1], n-1) or
                subset_sum(arr, sum, n-1))
    else:
        return subset_sum(arr, sum, n-1)

def equal_sum_partition(arr, n)->bool:
    sum=0
    for i in range(n):
        sum += arr[i]
        
    if(sum %2 ==0):
        return subset_sum(arr, sum/2, n)
    else:
        return False

print(equal_sum_partition(arr, len(arr)))
    


