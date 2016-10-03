import os
def findPath(matrix):
    n=len(matrix)
    m=len(matrix[0])
    for i in range(1,n*m):
        a=[(index,row.index(i)) for index,row in enumerate(matrix) if i in row]
        b=[(index,row.index(i+1)) for index,row in enumerate(matrix) if i+1 in row]
        if abs(a[0][0]-b[0][0]+a[0][1]-b[0][1])!=1:
            return False
    return True
findPath([[1, 4, 5],[2, 3, 6]])
