matrix = []
my_position = []
targets = 0

for row in range(5):
    matrix.append(input().split())
    for col in range(5):
        if matrix[row][col] == 'A':
            my_position = [row, col]
        elif matrix[row][col] == 'x':
            targets += 1

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
hits = []

for _ in range(int(input())):
    command = input().split()
    if command[0] == 'shoot':
        r = my_position[0] + directions[command[1]][0]
        c = my_position[1] + directions[command[1]][1]
        while r in range(5) and c in range(5):
            if matrix[r][c] == 'x':
                matrix[r][c] = '.'
                targets -= 1
                hits.append([r, c])
                break
            r += directions[command[1]][0]
            c += directions[command[1]][1]
        if targets == 0:
            print(f"Training completed! All {len(hits)} targets hit.")
            break
    elif command[0] == 'move':
        r = my_position[0] + directions[command[1]][0] * int(command[2])
        c = my_position[1] + directions[command[1]][1] * int(command[2])
        if r in range(5) and c in range(5) and matrix[r][c] == '.':
            matrix[r][c] = 'A'
            matrix[my_position[0]][my_position[1]] = '.'
            my_position = [r, c]

if targets > 0:
    print(f"Training not completed! {targets} targets left.")
[print(row) for row in hits]
