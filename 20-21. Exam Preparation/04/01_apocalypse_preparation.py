from collections import deque

textiles = deque(int(textile) for textile in input().split())
medicaments = [int(medicament) for medicament in input().split()]

healing_items_mapper = {
    30: "Patch",
    40: "Bandage",
    100: "MedKit"
}

healing_items_created = {
    "Patch": 0,
    "Bandage": 0,
    "MedKit": 0
}

while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()
    result = textile + medicament

    if result in healing_items_mapper:
        healing_items_created[healing_items_mapper[result]] += 1
    elif result > 100:
        healing_items_created['MedKit'] += 1
        if medicaments:
            medicaments.append((result - 100) + medicaments.pop())
        else:
            medicaments.append(result - 100)
    else:
        medicaments.append(medicament + 10)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

for healing_item, quantity in sorted(healing_items_created.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    if quantity > 0:
        print(f"{healing_item} - {quantity}")

if medicaments:
    print(f"Medicaments left: {', '.join([str(medicament) for medicament in sorted(medicaments, reverse=True)])}")

if textiles:
    print(f"Textiles left: {', '.join([str(textile) for textile in sorted(textiles, reverse=True)])}")

'''
20 10 40 70 20
10 50 10 30 20 80
'''
'''
30 30 10 80 60
40 20 30 10 70
'''
'''
30 30 10 80 60 20
40 20 30 10 70
'''
'''
60 15 20 30 20
20 15 40
'''
