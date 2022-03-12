from re import L


def Maxlength(arr, N, k):
     
    possibility = 0
    for i in range(N):
        for j in range(i,N):
            if(arr[j]-arr[i] <= k):
                possibility += 1
                print("i",i,"j",j,"poss",possibility)
    
    return possibility
        
 
 

arr = [1,10,2]
k = 9
N = len(arr)
print(Maxlength(arr, N,k))