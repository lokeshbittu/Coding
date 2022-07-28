import numpy as np

# a = np.unravel_index(89,(44,44))
# print(a)


# def generatePos(height, width):
#     pos_matrix = np.zeros([height, width], dtype=int)

#     count = 1
#     for i in range(width): #-> 2
#         for j in range(height): #-> 20
#             pos_matrix[j][i] = count
#             count = count + 1
    
#     return pos_matrix

# print(generatePos(20, 2))

a = np.arange(18).reshape(3,3,2)
print(a[:2, :])
        

# def get_pos_matrix_map(a):
    
#     pos_matrix_map = {}

#     for i in range(a.shape[0]):
#         for j in range(a.shape[1]):
#             pos = (i, j)
#             val = a[i][j]
#             pos_matrix_map[val] = pos

#     return pos_matrix_map

# pos_matrix = get_pos_matrix_map(a)
# print(pos_matrix.shape[1])

