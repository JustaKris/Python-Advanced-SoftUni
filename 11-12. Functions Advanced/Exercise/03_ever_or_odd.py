def even_odd(*args):
    command, args = args[-1], args[:-1]
    if command == 'even':
        return [int(num) for num in args if num % 2 == 0]
    return [int(num) for num in args if num % 2 != 0]


def main():
    print(even_odd(1, 2, 3, 4, 5, 6, "even"))
    print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))


if __name__ == "__main__":
    main()
