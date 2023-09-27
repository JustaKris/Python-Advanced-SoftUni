from collections import deque

n_petrol_pumps = int(input())

pumps = deque()
start_position = 0
stops = 0

for _ in range(n_petrol_pumps):
    petrol, distance = input().split()
    pumps.append([int(petrol), int(distance)])

while stops < n_petrol_pumps:
    fuel = 0
    for i in range(n_petrol_pumps):
        fuel += pumps[i][0]
        destination = pumps[i][1]
        if fuel < destination:
            pumps.rotate(-1)
            start_position += 1
            stops = 0
            break
        fuel -= destination
        stops += 1

print(start_position)
