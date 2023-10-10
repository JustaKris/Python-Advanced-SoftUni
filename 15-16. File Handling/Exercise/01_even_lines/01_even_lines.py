with open("text.txt") as file:
    for row, line in enumerate(file.readlines()):
        if row % 2 == 0:
            for character in "-,.!?":
                line = line.replace(character, "@")
            print(' '.join(line.split()[::-1]))
