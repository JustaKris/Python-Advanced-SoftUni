rows, cols = [int(el) for el in input().split(', ')]

matrix = []

for row in range(rows):
    elements = [int(el) for el in input().split(', ')]
    matrix.append(elements)

largest_sum = 0
largest_sub_matrix = []
for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        current_element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        element_below = matrix[row_index + 1][col_index]
        element_diagonal = matrix[row_index + 1][col_index + 1]

        sub_matrix = [
            [current_element, next_element],
            [element_below, element_diagonal]
        ]
        sum_sub_matrix = current_element + next_element + element_below + element_diagonal

        if sum_sub_matrix > largest_sum:
            largest_sum = sum_sub_matrix
            largest_sub_matrix = sub_matrix

print(*largest_sub_matrix[0])
print(*largest_sub_matrix[1])
print(largest_sum)
