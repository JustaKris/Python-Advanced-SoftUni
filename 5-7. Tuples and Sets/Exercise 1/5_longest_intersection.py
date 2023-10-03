n = int(input())

longest_range = list()
for _ in range(n):
    ranges = input().split("-")
    first_range, second_range = ranges[0].split(","), ranges[1].split(",")
    first_range_start, first_range_end = int(first_range[0]), int(first_range[1])
    second_range_start, second_range_end = int(second_range[0]), int(second_range[1])

    set_1 = set(num for num in range(first_range_start, first_range_end + 1))
    set_2 = set(num for num in range(second_range_start, second_range_end + 1))

    intersection = set_1.intersection(set_2)
    if len(intersection) > len(longest_range):
        longest_range = list(intersection)

print(f"Longest intersection is {longest_range} with length {len(longest_range)}")
