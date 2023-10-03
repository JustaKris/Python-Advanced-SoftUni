from collections import deque

materials = [int(mat) for mat in input().split()]
magic = deque([int(mat) for mat in input().split()])

material_requirements = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

presents = {
    'Doll': 0,
    'Wooden train': 0,
    'Teddy bear': 0,
    'Bicycle': 0
}

while materials and magic:
    total_magic = materials[-1] * magic[0]
    if total_magic in material_requirements:
        new_present = material_requirements[total_magic]
        presents[new_present] += 1
        materials.pop()
        magic.popleft()
    elif total_magic < 0:
        materials.append(materials.pop() + magic.popleft())
    elif total_magic > 0:
        magic.popleft()
        materials[-1] += 15
    elif materials[-1] == 0 and magic[0] == 0:
        materials.pop()
        magic.popleft()
    elif materials[-1] == 0:
        materials.pop()
    elif magic[0] == 0:
        magic.popleft()


if (presents['Doll'] > 0 and presents['Wooden train'] > 0) or (presents['Teddy bear'] > 0 and presents['Bicycle'] > 0):
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials[::-1]])}")

if magic:
    print(f"Magic left: {', '.join([str(x) for x in magic])}")

for key, value in sorted(presents.items()):
    if value > 0:
        print(f'{key}: {value}')
