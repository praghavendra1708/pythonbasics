# Transpose matrix

matrix = [ [x*y for x in range(4)] for y in range(4)]

matrix = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 0]]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


print('matrix', *matrix, sep='\n')

#tranposeMatrix =[[matrix[y][x] for y in range(len(matrix[x]))] for x in range(len(matrix))]

#print('transpose of matrix',*tranposeMatrix, sep='\n')



forTransMatrix = []
for x in range(len(matrix)):
    row = []
    for y in range(len(matrix[x])):
        row.append(matrix[y][x])
    forTransMatrix.append(row)

print(*forTransMatrix, sep='\n')