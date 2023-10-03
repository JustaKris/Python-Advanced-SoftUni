from collections import deque


# Step 1: Function to calculate honey made from a bee and nectar
def calculate_honey(bee, nectar, symbol):
    if symbol == "+":
        return abs(bee + nectar)
    elif symbol == "-":
        return abs(bee - nectar)
    elif symbol == "*":
        return abs(bee * nectar)
    elif symbol == "/":
        if nectar == 0:
            return None
        return abs(bee / nectar)


def main():
    bees = deque(list(map(int, input().split())))
    nectar_values = deque(list(map(int, input().split())))
    symbols = deque(input().split())

    total_honey = 0

    while bees and nectar_values:
        while nectar_values:
            nectar = nectar_values.pop()
            if nectar >= bees[0]:
                bee = bees.popleft()
                symbol = symbols.popleft()
                result = calculate_honey(bee, nectar, symbol)
                if result is not None:
                    total_honey += result
                    break

    print(f"Total honey made: {total_honey}")
    if bees:
        print(f"Bees left: {', '.join(map(str, bees))}")
    if nectar_values:
        print(f"Nectar left: {', '.join(map(str, nectar_values))}")


if __name__ == "__main__":
    main()
