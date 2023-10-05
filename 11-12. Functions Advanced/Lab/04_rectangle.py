def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        return 'Enter valid values!'

    def area():
        return length * width

    def perimeter():
        return 2 * (length + width)

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"


def main():
    print(rectangle(2, 10))
    print(rectangle('2', 10))


if __name__ == "__main__":
    main()
