n = int(input())

matrix = []
my_position = list
for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == 'S':
            my_position = [row, col]

directions_mapper = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

FISH_TARGET = 20
fish_collected = 0

direction = input()
while direction != 'collect the nets':
    row = my_position[0] + directions_mapper[direction][0]
    col = my_position[1] + directions_mapper[direction][1]
    if row not in range(n):
        if row > n - 1:
            row = 0
        elif row < 0:
            row = n - 1
    if col not in range(n):
        if col > n - 1:
            col = 0
        elif col < 0:
            col = n - 1
    if matrix[row][col].isnumeric():
        fish_collected += int(matrix[row][col])
    elif matrix[row][col] == 'W':
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
              f"Last coordinates of the ship: [{row},{col}]")
        break
    matrix[my_position[0]][my_position[1]] = '-'
    matrix[row][col] = 'S'
    my_position = [row, col]
    direction = input()
else:
    if fish_collected >= FISH_TARGET:
        print("Success! You managed to reach the quota!")
    else:
        print(f"You didn't catch enough fish and didn't reach the quota!"
              f" You need {FISH_TARGET - fish_collected} tons of fish more.")
    if fish_collected:
        print(f"Amount of fish caught: {fish_collected} tons.")
    [print(*row, sep="") for row in matrix]

'''Test Input 1
4
---S
----
9-5-
34--
down
down
right
down
collect the nets
'''

'''Test input 2
5
S---9
777-1
W333-
11111
-----
down
down
right
down
collect the nets
'''

'''Test Input 3
5
S---9
777-1
--5--
11W11
988--
down
down
down
down
down
down
right
right
right
collect the nets
'''