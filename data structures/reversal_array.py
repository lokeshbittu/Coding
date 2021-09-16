# driver program

# def rearrange(arr):
#     n = len(arr)
#     for i in range(0,n,2):
#         a = max(arr[i:])
#         b = min(arr[i:])
#         print("beffore", arr)
#         arr[i], a = a, arr[i]
#         arr[i+1], b = b, arr[i+1]
        
#         print("after",arr)
        

# arr = [1, 12, 4, 6, 7, 10]
# rearrange(arr)


#rearrange the array with difference

def difference(arr, k):
    n = len(arr)
    for i in range(arr):
        arr[i] = abs(arr[i] - k)
    return arr.sort()

arr = [10, 5, 3, 9, 2]
k = 2
difference(arr, k)