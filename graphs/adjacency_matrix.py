import numpy as np

height = 3
widht = 2

graph_int = np.arange(1, 3*2 + 1).reshape(2, 3).transpose()


adjacency_matrix = np.zeros([14,14],dtype=float)


width = graph_int.shape[1]
        
for _, j in enumerate(graph_int[:, 0]):
    print(j)
    # adjacency_matrix[0, j] = float("inf")
    adjacency_matrix[j, 0] = float("inf")
    
#-> 
for _, j in enumerate(graph_int[:, width - 1]):
    print("j",j, "adj",)
    adjacency_matrix[j, adjacency_matrix.shape[1] - 1] = float("inf")

print("graph_int", graph_int)
print("adjacency_matrix", adjacency_matrix)