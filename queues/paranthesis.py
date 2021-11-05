
def squarematrix(n):
    matrix = ["" for y in range(n)]
    start = "*"
    
    for i in range(len(matrix)):
        if(i == 0 or i == len(matrix)-1):
            matrix[i] = (matrix[i]+start)*4
        else:
            matrix[i] = (matrix[0]+start)
            matrix[i] = matrix[1]*(len(matrix)-1)
            matrix[i] = (matrix[len(matrix)-1]+start)
    print(matrix)

        


squarematrix(4)