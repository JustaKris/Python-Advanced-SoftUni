from collections import deque

n = int(input())
directions = deque(input().split(', '))

matrix = []
squirrel = list
for row in range(n):
    row_data = list(input())
    if 's' in row_data:
        col = row_data.index('s')
        squirrel = [row, col]
    matrix.append(row_data)

directions_mapper = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

hazelnut_target = 3
while directions:
    direction = directions.popleft()
    row = squirrel[0] + directions_mapper[direction][0]
    col = squirrel[1] + directions_mapper[direction][1]

    if row not in range(n) or col not in range(n):
        print("The squirrel is out of the field.")
        break

    if matrix[row][col] == 't':
        print("Unfortunately, the squirrel stepped on a trap...")
        break

    if matrix[row][col] == 'h':
        hazelnut_target -= 1
        if not hazelnut_target:
            print("Good job! You have collected all hazelnuts!")
            break
        matrix[row][col] = '*'

    squirrel = [row, col]

else:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {3 - hazelnut_target}")

'''
5
left, left, up, right, up, up
**h**
t****
*h***
*h*s*
*****
'''

'''
4
down, down, right, right
*s*h
***h
***t
h***
'''

'''
4
down, down, right, right
h***
***h
*s*t
**h*
'''
