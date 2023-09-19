from collections import deque

food_quantity = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

while orders:
    if orders[0] <= food_quantity:
        food_quantity -= orders.popleft()
    else:
        print(f'Orders left: {" ".join([str(order) for order in orders])}')
        break
else:
    print('Orders complete')
