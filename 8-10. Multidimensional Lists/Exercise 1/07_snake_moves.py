from collections import deque

r, c = [int(el) for el in input().split()]
txt = deque(input())

matrix = []

for row in range(r):
    matrix.append([''] * c)
    for col in range(c):
        if row % 2 == 0:
            matrix[row][col] = txt[0]
        else:
            matrix[row][-1 - col] = txt[0]
        txt.rotate(-1)

[print(*row, sep='') for row in matrix]
