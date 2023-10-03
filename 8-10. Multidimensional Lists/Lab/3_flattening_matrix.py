rows = int(input())

flattened_matrix = []

for row_index in range(rows):
    elements = [int(el) for el in input().split(", ")]
    flattened_matrix += elements

print(flattened_matrix)
