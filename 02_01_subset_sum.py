# Problem statement:
# given array, we need to find if subset exists 
# with given sum
# output -> boolean

arr=[4, 3, 5, 8, 10]
sum=12

def subset_sum_recusrs(arr, sum, n)->bool:
    
    if(sum==0):
        return True
    if(n==0):
        return False
    
    if(arr[n-1]<=sum):
        return (subset_sum_recusrs(arr, sum-arr[n-1], n-1) or
                subset_sum_recusrs(arr, sum, n-1))
    else:
        return subset_sum_recusrs(arr, sum, n-1)




rows, cols = (sum+1, len(arr)+1)
result = [[-1 for i in range(cols)] for j in range(rows)]

def subset_sum_memo(arr, sum, n)->bool:
    if(sum==0):
        return True
    if(n==0):
        return False
    if result[sum][n]!= -1:
        return result[sum][n]
    
    if(arr[n-1]<=sum):
        result[sum][n]= (subset_sum_memo(arr, sum-arr[n-1], n-1) or
                subset_sum_memo(arr, sum, n-1))
        return result[sum][n]
    else:
        result[sum][n] = subset_sum_memo(arr, sum, n-1)
        return result[sum][n]

def subset_sum_top(arr, sum, n)->bool:
    subset=([[False for i in range(sum+1)] for j in range(n + 1)])
    #if n is 0 then answer is False
    for j in range(sum+1):
        subset[0][j]=False
    #if sum is 0 then answer is true
    for i in range(n+1):
        subset[i][0]=True
    
    for i in range(1, n+1):
        for j in range(1, sum+1):
            if(arr[i-1]<=j):
                subset[i][j]= subset[i-1][j-arr[i-1]] or subset[i-1][j]
            else:
                subset[i][j]= subset[i-1][j]
    
    """for i in range(n + 1):
        for j in range(sum + 1):
            print (subset[i][j], end =" ")"""


    
    return subset[n][sum]



#calling the three function
print(subset_sum_recusrs(arr, sum, len(arr)))
print(subset_sum_memo(arr, sum, len(arr)))
print(subset_sum_top(arr,sum, len(arr)))


    



