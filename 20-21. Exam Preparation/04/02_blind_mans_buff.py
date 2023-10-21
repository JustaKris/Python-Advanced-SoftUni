N, M = [int(num) for num in input().split()]

matrix = []
my_position = list
for row in range(N):
    row_data = list(input().split())
    if 'B' in row_data:
        col = row_data.index('B')
        my_position = [row, col]
    matrix.append(row_data)

directions_mapper = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

opponents_touched = 0
moves_made = 0
while True:
    direction = input()
    if direction == 'Finish':
        break

    row = my_position[0] + directions_mapper[direction][0]
    col = my_position[1] + directions_mapper[direction][1]

    if row not in range(N) or col not in range(M) or matrix[row][col] == 'O':
        continue

    # if matrix[row][col] == 'O':  # Obstacle
    #     continue
    moves_made += 1
    if matrix[row][col] == 'P':  # Player
        opponents_touched += 1
        matrix[row][col] = '-'
        if opponents_touched == 3:
            break
    my_position = [row, col]

print(f"Game over!\nTouched opponents: {opponents_touched} Moves made: {moves_made}")


'''
5 8
- - - O - P - O
- P - O O - - -
- - - - - - O -
- P B - O - - O
- - - O - - - -
up
up
left
Finish
'''
'''
4 4
O B O -
- P O P
- - P -
- - - -
left
right
down
right
down
right
up
right
up
down
Finish
'''
