rows, cols = [int(el) for el in input().split(', ')]

matrix = []

for row in range(rows):
    elements = [int(el) for el in input().split()]
    matrix.append(elements)

for col_index in range(cols):
    col_sum = 0
    for row_index in range(rows):
        col_sum += matrix[row_index][col_index]
    print(col_sum)
