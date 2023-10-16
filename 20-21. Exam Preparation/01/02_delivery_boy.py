# Reading matrix shape
N, M = [int(num) for num in input().split()]

# Reading matrix and saving delivery boy position
matrix = []
delivery_boy_start_position = list
delivery_boy_current_position = list
for row in range(N):
    row_data = list(input())
    if 'B' in row_data:
        col = row_data.index('B')
        delivery_boy_start_position = [row, col]
        delivery_boy_current_position = [row, col]
    # delivery_spots += row_data.count('A')
    matrix.append(row_data)

# Directional movements mapper
directions_mapper = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

while True:
    command = input()

    row = delivery_boy_current_position[0] + directions_mapper[command][0]
    col = delivery_boy_current_position[1] + directions_mapper[command][1]

    # Unsuccessful delivery (index out of range)
    if row not in range(N) or col not in range(M):
        matrix[delivery_boy_start_position[0]][delivery_boy_start_position[1]] = ' '
        print("The delivery is late. Order is canceled.")
        break

    # Successful delivery
    if matrix[row][col] == 'A':
        matrix[row][col] = 'P'
        print("Pizza is delivered on time! Next order...")
        break

    # Board adjustments logic loop
    if matrix[row][col] == '*':
        continue
    elif matrix[row][col] == 'P':
        matrix[row][col] = 'R'
        print("Pizza is collected. 10 minutes for delivery.")
    elif matrix[row][col] == '-':
        matrix[row][col] = '.'
    delivery_boy_current_position = [row, col]

# Printing final matrix state
[print(*row, sep="") for row in matrix]

''' Input 1
5 6
*----A
*B***-
*-***-
*----P
******
down
down
right
right
right
right
up
up
up
'''

''' Input 2
5 6
*----A
*B***-
*-***-
*----P
******
down
down
left
right
right
right
right
right
up
'''
