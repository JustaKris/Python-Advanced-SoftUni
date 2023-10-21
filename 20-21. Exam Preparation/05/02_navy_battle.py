n = int(input())

matrix = []
submarine = list
for row in range(n):
    row_data = list(input())
    if 'S' in row_data:
        col = row_data.index('S')
        submarine = [row, col]
    matrix.append(row_data)

directions_mapper = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

battlecruisers = 3
mines_hit = 0
while True:
    direction = input()

    row = submarine[0] + directions_mapper[direction][0]
    col = submarine[1] + directions_mapper[direction][1]

    if row not in range(n) or col not in range(n):
        continue

    if matrix[row][col] == 'C':
        battlecruisers -= 1
    elif matrix[row][col] == '*':
        mines_hit += 1

    matrix[submarine[0]][submarine[1]] = '-'
    matrix[row][col] = 'S'
    submarine = [row, col]

    if not battlecruisers:
        print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
        break
    if mines_hit == 3:
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!")
        break

[print(*row, sep="") for row in matrix]


''' Test Input 1
5
*--*-
-S-*C
-*---
-----
-C-*C
right
down
left
up
right
right
right
down
down
down
up
left
left
left
down
'''
'''Test Input 2
5
*--*-
-S-*C
-*---
-----
*C-*C
right
right
up
left
left
left
'''
