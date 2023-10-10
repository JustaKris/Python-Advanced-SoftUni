
def sum_nums(*args):
    sum_positives = sum([x for x in args if x > 0])
    sum_negatives = sum([x for x in args if x < 0])
    return sum_positives, sum_negatives


def main():
    numbers = [int(num) for num in input().split()]

    sum_positives, sum_negatives = sum_nums(*numbers)
    print(f"{sum_negatives}\n{sum_positives}")
    if abs(sum_positives) > abs(sum_negatives):
        print("The positives are stronger than the negatives")
    elif abs(sum_positives) < abs(sum_negatives):
        print("The negatives are stronger than the positives")


if __name__ == "__main__":
    main()
