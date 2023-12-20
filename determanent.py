def determine(matrix):
    det = 0
    for i in range(3):
        det += matrix[0][i] * (matrix[1][(i + 1) % 3] * matrix[2][(i + 2) % 3] - matrix[1][(i + 2) % 3] * matrix[2][(i + 1) % 3])
    return det
matrix = [
    [2, 3, 44],
    [5, 6, 75],
    [8, 9, 10]
]

result = determine(matrix)
print("Determinant:", result)
