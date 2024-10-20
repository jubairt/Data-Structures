# ===================================================


# 2 D arrays
# Creating a 2D array (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Printing the matrix
for row in matrix:
    print(row)

# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]

# ------------------------

# Access the element at the second row and third column
element = matrix[1][2]
print(element)  # Output: 6

# ---------------------

# Traverse and print each element
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()  # For a new line after each row

# 1 10 3 
# 4 5 6 
# 7 8 9 

# ---------------------------------------------------------

def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    # Creating a new matrix to store the transpose
    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]
    
    return transposed_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = transpose(matrix)
for row in transposed:
    print(row)

# [1, 4, 7]
# [2, 5, 8]
# [3, 6, 9]


# -----------------------------------------------------------------

matrix = [
    [1,2],
    [3,4],
    [5,6]
]

def transpose(matrix):
    row = len(matrix)
    col = len(matrix[0])
    
    print('orginal')
    for i in range(row):
        for j in range(col):
            print(matrix[i][j], end=' ')
        print()
        
        
    print('transposed')
    for i in range(col):
        for j in range(row):
            print(matrix[j][i], end=' ')
        print()
transpose(matrix)

# -----------------------------------------------------------------

def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    # Creating a new matrix to store the result
    result_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
    
    return result_matrix

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result = add_matrices(matrix1, matrix2)
for row in result:
    print(row)

# [10, 10, 10]
# [10, 10, 10]
# [10, 10, 10]

# ==============================================================