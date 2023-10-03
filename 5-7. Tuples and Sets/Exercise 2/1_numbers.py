# def add_numbers(sequence, numbers):
#     for number in numbers:
#         sequence.add(number)
#     return sequence
#
#
# def remove_numbers(sequence, numbers):
#     for number in numbers:
#         if number in sequence:
#             sequence.remove(number)
#     return sequence


first_sequence = set(int(num) for num in input().split())
second_sequence = set(int(num) for num in input().split())

n = int(input())
for _ in range(n):
    command = input()

    if command == "Check Subset":
        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            print('True')
        else:
            print("False")
    else:
        numbers = [int(num) for num in command.split()[2:]]
        if "Add First" in command:
            # first_sequence = add_numbers(first_sequence, numbers)
            first_sequence.update(numbers)
        elif "Add Second" in command:
            # second_sequence = add_numbers(second_sequence, numbers)
            second_sequence.update(numbers)
        elif "Remove First" in command:
            # first_sequence = remove_numbers(first_sequence, numbers)
            first_sequence.difference_update(numbers)
        elif "Remove Second" in command:
            # second_sequence = remove_numbers(second_sequence, numbers)
            second_sequence.difference_update(numbers)

print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")


'''
5 4 2 9 9 5 4
1 1 1 5 6 5
4
Add First 5 6 9 3
Add Second 1 2 3 3 3
Check Subset
Remove Second 1 2 3 4 5
'''