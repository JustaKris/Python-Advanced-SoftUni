from collections import deque

caffeine_quantities = [int(quantity) for quantity in input().split(', ')]
energy_drinks = deque(int(drink) for drink in input().split(', '))

CAFFEINE_LIMIT = 300
caffeine_drank = 0

while caffeine_quantities and energy_drinks:

    caffeine_quantity = caffeine_quantities.pop()
    energy_drink = energy_drinks.popleft()

    result = caffeine_quantity * energy_drink
    if caffeine_drank + result <= CAFFEINE_LIMIT:
        caffeine_drank += result
    else:
        energy_drinks.append(energy_drink)
        if caffeine_drank <= 30:
            caffeine_limit = 0
        else:
            caffeine_drank -= 30

if energy_drinks:
    print(f"Drinks left: {', '.join([str(drink) for drink in energy_drinks])}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {caffeine_drank} mg caffeine.")

'''Test Input 1
34, 2, 3
40, 100, 250
'''
'''Test Input 2
1, 16, 8, 14, 5
27, 23
'''
'''Test Input 3
1, 23, 2, 1, 42, 22, 7, 14
51, 100, 3, 7
'''
