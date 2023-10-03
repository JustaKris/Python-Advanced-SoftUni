rows, cols = [int(el) for el in input().split()]
matrix = [[x for x in input().split()] for _ in range(rows)]

count = 0
for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        if matrix[row_index][col_index] == matrix[row_index][col_index + 1] == matrix[row_index + 1][col_index] == matrix[row_index + 1][col_index + 1]:
            count += 1

print(count)
