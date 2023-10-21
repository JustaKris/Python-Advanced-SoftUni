from collections import deque

programmers = deque(int(programmer) for programmer in input().split())
tasks = [int(task) for task in input().split()]

ducks = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0
}

while programmers and tasks:
    programmer = programmers.popleft()
    task = tasks.pop()
    time_requirement = programmer * task

    if time_requirement <= 60:
        ducks['Darth Vader Ducky'] += 1
    elif time_requirement <= 120:
        ducks['Thor Ducky'] += 1
    elif time_requirement <= 180:
        ducks['Big Blue Rubber Ducky'] += 1
    elif time_requirement <= 240:
        ducks['Small Yellow Rubber Ducky'] += 1
    else:
        programmers.append(programmer)
        tasks.append(task - 2)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for duck_type, count in ducks.items():
    print(f"{duck_type}: {count}")

'''
10 15 12 18 22 6
12 16 5 6 9 1
'''
'''
2 55 17 31 23
7 5 17 4 27
'''
