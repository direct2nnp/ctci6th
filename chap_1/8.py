'''
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, 
its entire row and column are set to 0.
'''
def get_zero_matrix(matrix):
    m = len(matrix)
    n = 0 if m == 0 else len(matrix[0])
    row_index = [None for i in range(m)]
    column_index = [None for i in range(n)]

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row_index[i] = 0
                column_index[j] = 0

    for i in range(m):
        for j in range(n):
            if row_index[i] == 0 or column_index[j] == 0:
                matrix[i][j] = 0

    return matrix

def print_matrix(matrix):
    for l in matrix:
        print l

matrix = [[1,0,3,4],
          [5,6,0,8],
          [9,10,0,12],
          [13,14,15,16]]
matrix_2 = [[1,0],
          [5,6],
          [9,0],
          [13,14]]
          
print 'Initial Matrix'
print_matrix(matrix)
print 'Final Matrix'
print_matrix(get_zero_matrix(matrix))

print 'Initial Matrix'
print_matrix(matrix_2)
print 'Final Matrix'
print_matrix(get_zero_matrix(matrix_2))
