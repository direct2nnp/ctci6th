'''
Rotate Matrix: Given an image represented by an NxN matrix, 
where each pixel in the image is 4 bytes, 
write a method to rotate the image by 90 degrees. 
Can you do this in place?
'''

def rotate_matrix(matrix):
    N = len(matrix)
    temp = []
    print 'Initial Matrix'
    print_matrix(matrix)

    for x in range(N/2):
        for y in range(x,N-x-1):
            temp = matrix[x][y]
            matrix[x][y] = matrix[y][N-1-x]
            matrix[y][N-1-x] = matrix[N-1-x][N-1-y]
            matrix[N-1-x][N-1-y] = matrix[N-1-y][x]
            matrix[N-1-y][x] = temp

    print 'Final Matrix'
    print_matrix(matrix)

def print_matrix(matrix):
    for l in matrix:
        print l

matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]]
rotate_matrix(matrix)