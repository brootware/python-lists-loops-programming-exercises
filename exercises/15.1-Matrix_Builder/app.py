#Import random
# import random
#Create the function below:
def matrixBuilder(int):
    matrix = []
    # Populates row column matrix
    for i in range(int):
        matrix.append(list(range(int)))

    # Updates the elements inside the matrix
    for row in range(int):
        for col in range(int):
            matrix[row][col] = 1
    
    return matrix

print(matrixBuilder(5))