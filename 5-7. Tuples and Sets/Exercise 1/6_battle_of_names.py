n = int(input())

evens = set()
odds = set()

row = 1
for _ in range(n):
    name = input()
    ascii_sum = 0
    for el in name:
        ascii_sum += ord(el)
    ascii_sum //= row
    row += 1
    if ascii_sum % 2 == 0:
        evens.add(ascii_sum)
    else:
        odds.add(ascii_sum)

sum_evens = sum(evens)
sum_odds = sum(odds)
if sum_odds == sum_evens:
    print(*evens.union(odds), sep=", ")
elif sum_odds > sum_evens:
    print(*odds.difference(evens), sep=", ")
elif sum_odds < sum_evens:
    print(*evens.symmetric_difference(odds), sep=", ")
