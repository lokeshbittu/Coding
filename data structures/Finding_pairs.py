# driver code

def pairs(arr, n, sum):
    for i in range(n):
        for j in range(i+1,n):
            if(arr[i]+arr[j] == sum):
                print(arr[i], arr[j])


A = [1, 4, 45, 6, 10, 8]
n = 16
pairs(A, len(A), n)

#this is with the polynomial time complexity 
# space complexity = O(1)