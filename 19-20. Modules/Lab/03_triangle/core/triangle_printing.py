def print_upper_part(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def print_lower_part(n):
    for i in range(n - 1, 0, -1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()


def print_triangle(n):
    print_upper_part(n)
    print_lower_part(n)


# print_triangle(3)
