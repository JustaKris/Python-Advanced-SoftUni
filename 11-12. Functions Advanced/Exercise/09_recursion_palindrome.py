def palindrome(word, index):
    if index == len(word):
        return f"{word} is a palindrome"
    if word[index] != word[-1 - index]:
        return f"{word} is not a palindrome"
    return palindrome(word, index + 1)


def main():
    print(palindrome("abcba", 0))
    print(palindrome("peter", 0))


if __name__ == "__main__":
    main()
