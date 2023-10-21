def shop_from_grocery_list(budget, grocery_list, *products):
    shopping = []
    for product_name, product_price in products:
        if budget < product_price:
            break
        if product_name not in shopping and product_name in grocery_list:
            budget -= product_price
            grocery_list.remove(product_name)
            shopping.append(product_name)

    if not grocery_list:
        result = f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        result = f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."

    return result


def main():
    print(shop_from_grocery_list(
        100,
        ["tomato", "cola"],
        ("cola", 5.8), ("tomato", 10.0), ("tomato", 20.45),
    ))
    print(shop_from_grocery_list(
        100,
        ["tomato", "cola", "chips", "meat"],
        ("cola", 5.8), ("tomato", 10.0), ("meat", 22),
    ))
    print(shop_from_grocery_list(
        100,
        ["tomato", "cola", "chips", "meat", "chocolate"],
        ("cola", 15.8), ("chocolate", 30), ("tomato", 15.85), ("chips", 50), ("meat", 22.99),
    ))


if __name__ == '__main__':
    main()
