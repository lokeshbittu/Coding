def minAbsSumPair(arr):
    arr.sort()
    i = 0
    j = len(n)-1
    min_sum = float(inf)
    while(i < j):
        if(arr[i]-arr[j] == 0):
            return (i, j)
        if(abs(arr[i]-arr[j])<min_sum):
            
        

arr = [1, 60, -10, 70, -80, 85]
 
minAbsSumPair(arr, 6);