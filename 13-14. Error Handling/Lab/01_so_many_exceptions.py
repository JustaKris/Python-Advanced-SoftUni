numbers_list = [int(el) for el in input().split(", ")]
result = 1
for i in range(len(numbers_list)):
    number = numbers_list[i]
    if number <= 5:
        result *= number
    elif 5 < number <= 10:
        result /= number
print(result)

'''
2, 5, 10
'''
'''
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
'''
