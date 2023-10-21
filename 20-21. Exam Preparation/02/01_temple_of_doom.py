from collections import deque

tools = deque(int(tool) for tool in input().split())
substances = [int(substance) for substance in input().split()]
challenges = [int(challenge) for challenge in input().split()]


while tools and substances:

    tool = tools.popleft()
    substance = substances.pop()

    result = tool * substance
    if result in challenges:
        challenges.remove(result)
        if not challenges:
            print("Harry found an ostracon, which is dated to the 6th century BCE.")
            break
    else:
        tools.append(tool + 1)
        if substance - 1 != 0:
            substances.append(substance - 1)
else:
    print("Harry is lost in the temple. Oblivion awaits him.")

if tools:
    print(f"Tools: {', '.join([str(tool) for tool in tools])}")
if substances:
    print(f"Substances: {', '.join([str(substance) for substance in substances])}")
if challenges:
    print(f"Challenges: {', '.join([str(challenge) for challenge in challenges])}")


'''
2 4 6 8
11 3 5 7 9
24 28 18 30
'''

'''
13 7 4 22 11 15 20
3 2 1
12 10 5
'''