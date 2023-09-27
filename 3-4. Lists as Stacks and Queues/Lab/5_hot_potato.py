from collections import deque

children = deque(input().split())
n = int(input())

while len(children) != 1:
    children.rotate(-n + 1)
    print(f"Removed {children.popleft()}")

print(f"Last is {children.popleft()}")
