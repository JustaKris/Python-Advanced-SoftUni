from collections import deque

monsters_armors = deque(int(armor) for armor in input().split(','))
soldier_attacks = [int(attack) for attack in input().split(',')]

monsters_killed = 0

while True:
    if not soldier_attacks and not monsters_armors:
        print("All monsters have been killed!")
        print("The soldier has been defeated.")
        break
    if not soldier_attacks:
        print("The soldier has been defeated.")
        break
    if not monsters_armors:
        print("All monsters have been killed!")
        break

    monster_armor = monsters_armors.popleft()
    soldier_attack = soldier_attacks.pop()
    if soldier_attack >= monster_armor:
        soldier_attack -= monster_armor
        if soldier_attack > 0:
            if soldier_attacks:
                soldier_attacks.append(soldier_attack + soldier_attacks.pop())
            else:
                soldier_attacks.append(soldier_attack)
        monsters_killed += 1
    else:
        monster_armor -= soldier_attack
        if monster_armor > 0:
            monsters_armors.append(monster_armor)

print(f"Total monsters killed: {monsters_killed}")

'''
20,15,10
5,15,10,25

30,25,40,35
15,20,10,30
'''
