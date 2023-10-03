values = tuple(float(num) for num in input().split())

counted = []
for value in values:
    if value not in counted:
        current_count = values.count(value)
        print(f"{value} - {current_count} times")
        counted.append(value)
