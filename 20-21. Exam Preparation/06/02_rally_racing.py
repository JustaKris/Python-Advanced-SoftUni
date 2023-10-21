N = int(input())
racecar_number = input()

matrix = []
racecar_position = [0, 0]
tunnel_positions = []
for row in range(N):
    matrix.append(list(input().split()))
    for col in range(N):
        if matrix[row][col] == 'T':
            tunnel_positions.append((row, col))

directions_mapper = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
kilometers_traveled = 0

while True:
    direction = input()
    if direction == 'End':
        print(f"Racing car {racecar_number} DNF.")
        break

    row = racecar_position[0] + directions_mapper[direction][0]
    col = racecar_position[1] + directions_mapper[direction][1]
    if row not in range(N) or col not in range(N):
        continue

    matrix[racecar_position[0]][racecar_position[1]] = '.'
    kilometers_traveled += 10

    if matrix[row][col] == 'T':
        for tunnel_row, tunnel_col in tunnel_positions:
            if row != tunnel_row and col != tunnel_col:
                row, col = tunnel_row, tunnel_col
            else:
                matrix[tunnel_row][tunnel_col] = '.'
        kilometers_traveled += 20
    elif matrix[row][col] == 'F':
        matrix[row][col] = 'C'
        print(f"Racing car {racecar_number} finished the stage!")
        break
    matrix[row][col] = 'C'
    racecar_position = [row, col]

print(f"Distance covered {kilometers_traveled} km.")
[print(*row, sep="") for row in matrix]

'''
5
01
. . . . .
. . . T .
. . . . .
. T . . .
. . F . .
down
right
right
right
down
right
up
down
right
up
End
'''
'''
10
45
. . . . . . . . . . 
. . T . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . F . . .
. . . . . . . . . .
. . . . . . . . . . 
. . . . . . . T . .
right
down
down
right
up
left
up
up
End
'''
