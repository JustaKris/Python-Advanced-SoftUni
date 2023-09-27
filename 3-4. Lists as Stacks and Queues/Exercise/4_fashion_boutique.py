clothes_stack = [int(x) for x in input().split()]
rack_capacity = int(input())

number_of_racks = 1
current_rack = 0

while clothes_stack:
    current_item = clothes_stack.pop()
    if current_rack + current_item <= rack_capacity:
        current_rack += current_item
    else:
        current_rack = current_item
        number_of_racks += 1

print(number_of_racks)
