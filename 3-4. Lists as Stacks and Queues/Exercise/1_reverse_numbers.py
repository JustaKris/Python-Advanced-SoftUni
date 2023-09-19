stack = [int(num) for num in input().split()]

reverse_num = []
while stack:
    reverse_num.append(stack.pop())

print(*reverse_num)
