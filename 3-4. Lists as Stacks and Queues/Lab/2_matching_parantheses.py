expression = input()

stack = []

for i in range(len(expression)):
    if expression[i] == '(':
        stack.append(i)
    elif expression[i] == ')':
        start_index = stack.pop()
        last_index = i + 1
        print(expression[start_index:last_index])
