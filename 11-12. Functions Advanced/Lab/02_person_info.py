def get_info(name, age, town):
    return f"This is {name} from {town} and he is {age} years old"


def main():
    print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))


if __name__ == "__main__":
    main()
