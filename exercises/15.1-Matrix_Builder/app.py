# Your code here
def matrix_builder(num:int) -> list:
    matrix = []
    for i in range(num):
        row = []
        for j in range(num):
            row.append(1)
        matrix.append(row)

    return matrix

result = matrix_builder(5)
print(result)