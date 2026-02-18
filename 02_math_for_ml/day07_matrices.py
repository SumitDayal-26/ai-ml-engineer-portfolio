# Day 7: Matrices for Machine Learning
# Representing Matrices as Lists of Lists
matrix_a=[
    [1,2],
    [3,4]
]
matrix_b = [
    [5,6],
    [7,8]
]
print("matrix A: ", matrix_a)
print(" Matrix B:", matrix_b)

# matrix addition
matrix_sum=[]
for i in range(len(matrix_a)):#go row by row
    row = []
    for j in range(len(matrix_a[0])):#go column by column
        row.append(matrix_a[i][j] + matrix_b[i][j])
    matrix_sum.append(row)    
   
print("matrix Addition:", matrix_sum)

# Matrix vector multiplication 
vector = [1,2]
result = []
for row in matrix_a:
    dot = 0
    for i in range(len(vector)):
        dot+=row[i]*vector[i]
    result.append(dot)
print("Matrix vector Multiplication:", result)        
