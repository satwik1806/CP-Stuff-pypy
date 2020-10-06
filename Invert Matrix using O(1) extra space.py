
def invertmatrix(Matrix):
    for i in range(n//2):    #number of squares
        for j in range(i,n-i-1):

            #now rotating the chosen 4 indices manually
            temp = Matrix[i][j]
            Matrix[i][j] = Matrix[j][n-i-1]
            Matrix[j][n-i-1] = Matrix[n-i-1][n-j-1]
            Matrix[n-i-1][n-j-1] = Matrix[n-j-1][i]
            Matrix[n-j-1][i] = temp



n = 4
Matrix = [[0, 1,  2,  3],
         [4, 5,  6,  7],
         [8, 9,  10, 11],
         [12, 13, 14, 15]]

invertmatrix(Matrix)

for i in range(n):
    print(' '.join(str(Matrix[i][j]) for j in range(n)))
