
#Solution 1
def rightRotate(arr, k, n):

    for i in range(k//2):
        print("temp", arr[i], "arr[k-i-1]", arr[k-i-1], "total arry", arr)
        temp = arr[i]
        arr[i] = arr[k-i-1]
        arr[k-i-1] = temp
        print("arr steps", arr)
    return arr


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("n//2", len(arr)//2)
n = len(arr)
k = 3

#-> Solution 2
arr[:] = arr[n-k-1:n]+arr[:n-k-1]

print('arr reverse total', arr)

# print(rightRotate(arr, k, n))
# print(rightRotate(arr, n-k,n ))
