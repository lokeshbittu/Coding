
def MinBlockNeeded(A):
    strokes = 0
    while sum(A) > 0:
        for i in range(len(A)):
            if (A[i] > 0) and ((i+1 == len(A)) or (A[i+1] == 0)):
                strokes += 1
            if A[i] > 0:
                A[i] -= 1
    return strokes


A =[5,8]
print("MinBlocksNeeded", MinBlockNeeded(A))