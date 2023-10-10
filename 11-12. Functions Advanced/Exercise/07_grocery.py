def grocery_store(**kwargs):
    receipt = dict(sorted(kwargs.items(), key=lambda kvp: (-int(kvp[1]), -len(kvp[0]), kvp[0])))
    result = []
    for product_name, quantity in receipt.items():
        result.append(f"{product_name}: {quantity}\n")
    return ''.join(result)


def main():
    print(grocery_store(
        bread=5,
        pasta=12,
        eggs=12,
    ))
    print(grocery_store(
        bread=2,
        pasta=2,
        eggs=20,
        carrot=1,
    ))


if __name__ == "__main__":
    main()
