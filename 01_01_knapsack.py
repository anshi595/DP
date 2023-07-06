wt= [7, 3, 4]
val=[10, 5, 3]
W=9
def knapsack(wt:list, val:list, W:int, n: int)->int:
    if(W==0 or n==0):
        return 0
    if(wt[n-1]<=W):
        return max()

