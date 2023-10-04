n = int(input())

matrix = []
alice = []

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == 'A':
            alice = [row, col]
            break

moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

bags_of_tea = 0
while True:
    direction = input()
    matrix[alice[0]][alice[1]] = '*'
    move = [alice[0] + moves[direction][0], alice[1] + moves[direction][1]]
    if move[0] not in range(n) or move[1] not in range(n):
        print("Alice didn't make it to the tea party.")
        break
    else:
        if matrix[move[0]][move[1]] == "R":
            matrix[move[0]][move[1]] = '*'
            print("Alice didn't make it to the tea party.")
            break
        elif matrix[move[0]][move[1]].isdigit():
            bags_of_tea += int(matrix[move[0]][move[1]])
        matrix[move[0]][move[1]] = '*'
        alice = move
        if bags_of_tea >= 10:
            print("She did it! She went to the party.")
            break

[print(*row, sep=" ") for row in matrix]

'''
5
. A . . 1
R . 2 . .
4 7 . 1 .
. . . 2 .
. 3 . . .
down
right
left
down
up
left
'''