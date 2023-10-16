def update_board_and_mouse(matrix, mouse, row, col):
    matrix[mouse[0]][mouse[1]] = '*'
    matrix[row][col] = 'M'
    mouse = [row, col]
    return matrix, mouse


N, M = [int(num) for num in input().split(',')]

matrix = []
mouse = []
cheese_count = 0
for row in range(N):
    matrix.append(list(input()))
    for col in range(M):
        if matrix[row][col] == 'M':
            mouse = [row, col]
        elif matrix[row][col] == 'C':
            cheese_count += 1

directions_mapper = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

while True:
    command = input()
    if command == 'danger':
        print("Mouse will come back later!")
        break
    row = mouse[0] + directions_mapper[command][0]
    col = mouse[1] + directions_mapper[command][1]

    if row not in range(N) or col not in range(M):
        print("No more cheese for tonight!")
        break
    else:
        if matrix[row][col] == '@':
            continue
        elif matrix[row][col] == 'C':
            cheese_count -= 1
            if not cheese_count:
                matrix, mouse = update_board_and_mouse(matrix, mouse, row, col)
                print("Happy mouse! All the cheese is eaten, good night!")
                break
        elif matrix[row][col] == 'T':
            matrix, mouse = update_board_and_mouse(matrix, mouse, row, col)
            print("Mouse is trapped!")
            break
        matrix, mouse = update_board_and_mouse(matrix, mouse, row, col)

[print(*row, sep="") for row in matrix]


'''
5,5
**M**
T@@**
CC@**
**@@*
**CC*
left
down
left
down
down
down
right
danger
'''
