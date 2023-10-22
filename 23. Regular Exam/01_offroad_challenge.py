from collections import deque

fuel_quantities = [int(fuel_quantity) for fuel_quantity in input().split()]
consumption_indexes = deque(int(index) for index in input().split())
altitude_targets = deque(int(target) for target in input().split())

targets_reached = 1

while altitude_targets:
    fuel_quantity = fuel_quantities.pop()
    consumption_index = consumption_indexes.popleft()
    result = fuel_quantity - consumption_index

    altitude_target = altitude_targets.popleft()
    if result >= altitude_target:
        print(f"John has reached: Altitude {targets_reached}")
        targets_reached += 1
    else:
        print(f"John did not reach: Altitude {targets_reached}")
        print("John failed to reach the top.")
        if targets_reached < 2:
            print("John didn't reach any altitude.")
        else:
            altitudes_list = []
            for i in range(1, targets_reached):
                altitudes_list.append(f"Altitude {i}")
            print(f"Reached altitudes: {', '.join(altitudes_list)}")
        altitude_targets.appendleft(altitude_target)
        break

else:
    print("John has reached all the altitudes and managed to reach the top!")


'''Test Input 1
200 90 40 100
20 40 30 50
50 60 80 90
'''
'''Test input 2
40 66 123 100
10 30 70 33
40 55 77 100
'''