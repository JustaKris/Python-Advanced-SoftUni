def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result


def main():
    print(multiply(1, 4, 5))
    print(multiply(4, 5, 6, 1, 3))
    print(multiply(2, 0, 1000, 5000))


if __name__ == "__main__":
    main()
