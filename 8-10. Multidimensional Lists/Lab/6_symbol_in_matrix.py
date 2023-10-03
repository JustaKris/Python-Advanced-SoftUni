n = int(input())
matrix = []
for row in range(n):
    elements = list(input())
    matrix.append(elements)

symbol = input()
for row_index in range(n):
    for col_index in range(n):
        if matrix[row_index][col_index] == symbol:
            print((row_index, col_index))
            exit()
print(f"{symbol} does not occur in the matrix")
