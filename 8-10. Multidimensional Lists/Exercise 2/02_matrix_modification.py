n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

while True:
    command = input()
    if command == "END":
        break

    task, row, col, value = command.split()
    row, col, value = int(row), int(col), int(value)
    if row in range(n) and col in range(len(matrix[0])):
        if task == 'Add':
            matrix[row][col] += value
        elif task == 'Subtract':
            matrix[row][col] -= value
    else:
        print('Invalid coordinates')

[print(*row, sep=' ') for row in matrix]
