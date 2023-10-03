from collections import deque

chocolates = [int(num) for num in input().split(', ')]
milk_cups = deque(int(num) for num in input().split(', '))

milkshakes = 0

while chocolates and milk_cups and milkshakes < 5:
    if chocolates[-1] <= 0 and milk_cups[0] <= 0:
        chocolates.pop()
        milk_cups.popleft()
        continue
    if chocolates[-1] <= 0:
        chocolates.pop()
        continue
    if milk_cups[0] <= 0:
        milk_cups.popleft()
        continue
        # if not milk_cups:
        #     break

    if chocolates[-1] == milk_cups[0]:
        chocolates.pop()
        milk_cups.popleft()
        milkshakes += 1
    else:
        chocolates[-1] -= 5
        milk_cups.rotate(-1)

print(f'{"Great! You made all the chocolate milkshakes needed!" if milkshakes == 5 else "Not enough milkshakes."}')
print(f'Chocolate: {", ".join([str(chocolate) for chocolate in chocolates]) if chocolates else "empty"}')
print(f'Milk: {", ".join([str(cup) for cup in milk_cups]) if milk_cups else "empty"}')
