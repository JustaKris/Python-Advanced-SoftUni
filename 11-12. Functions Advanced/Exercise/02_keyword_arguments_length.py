def kwargs_length(**kwargs):
    return len(kwargs)


def main():
    dictionary = {'name': 'Peter', 'age': 25}
    print(kwargs_length(**dictionary))


if __name__ == "__main__":
    main()
