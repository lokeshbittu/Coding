
def replacefunction(arr, ar):
    n = len(ar)
    for i in range(n):
        first_ele = ar[i][0]
        last_ele = ar[i][1]
        replace_ele = ar[i][2]
        for j in range(len(arr)):
            if j>= first_ele-1 and j <= last_ele-1:  
                arr[j] += replace_ele
                
    return max(arr)

arr = 5*[0]
print(arr)
ar = [[1,2,10],[2,4,5],[3,5,12]]
print(replacefunction(arr, ar))