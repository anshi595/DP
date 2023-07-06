"""
Problem Statment:Given array, we need to count the number of subsets if it exists with given sum
output -> Int
"""

arr=[4, 3, 5, 8, 10]
sum=12
def subset_count(arr, sum, n)->int:
    count=0
    if(sum==0):
        count= count+1
        return count
    if(n==0):
        return count
    
    if(arr[n-1]<=sum):
        return (subset_count(arr, sum-arr[n-1], n-1) +
                subset_count(arr, sum, n-1))
    else:
        return subset_count(arr, sum, n-1)




rows, cols = (sum+1, len(arr)+1)
result = [[-1 for i in range(cols)] for j in range(rows)]
def subset_count_memo(arr, sum, n)->int:
    count=0
    if(sum==0):
        count= count+1
        return count
    if(n==0):
        return count
    if result[sum][n]!= -1:
        return result[sum][n]
    
    if(arr[n-1]<=sum):
        result[sum][n]= (subset_count_memo(arr, sum-arr[n-1], n-1) +
                subset_count_memo(arr, sum, n-1))
        return result[sum][n]
        
    else:
        result[sum][n] = subset_count_memo(arr, sum, n-1)
        return result[sum][n]


def subset_count_top(arr, sum, n)->int:
        result= [[0 for i in range(n+1)] for i in range(sum+1)]
        

#calling the function
print(subset_count(arr, sum, len(arr)))
print(subset_count_memo(arr, sum, len(arr)))




