# def maxsum(arr):
#     res = 0
#     n = len(arr)-1
#     for i in range(len(arr)):
#         curr_sum  = 0
#         for j in range(len(arr)):
#             index = int((i + j)% n)
#             curr_sum = curr_sum + index*arr[j]
#             if(curr_sum > res):
#                 res = curr_sum

#     return res

# arr = [8, 3, 1, 2]
# print(maxsum(arr))


r = "lokesh"
print(r[1])