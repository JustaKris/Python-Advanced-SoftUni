def main():
    number_of_presents = int(input())
    n = int(input())

    matrix = []
    santa = []
    nice_kids = 0
    nice_kids_with_presents = 0
    for row in range(n):
        matrix.append(input().split())
        for col in range(n):
            if matrix[row][col] == 'S':
                santa = [row, col]
            elif matrix[row][col] == 'V':
                nice_kids += 1

    directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

    while number_of_presents > 0:
        command = input()
        if command == 'Christmas morning':
            break
        matrix[santa[0]][santa[1]] = '-'
        row = santa[0] + directions[command][0]
        col = santa[1] + directions[command][1]
        if row in range(n) and col in range(n):
            if matrix[row][col] == 'C':
                for r, c in directions.values():
                    if matrix[row + r][col + c] == 'X':
                        number_of_presents -= 1
                    elif matrix[row + r][col + c] == 'V':
                        nice_kids_with_presents += 1
                        number_of_presents -= 1
                    matrix[row + r][col + c] = '-'
            elif matrix[row][col] == 'V':
                nice_kids_with_presents += 1
                number_of_presents -= 1
            matrix[row][col] = 'S'
            santa = [row, col]
    else:
        if nice_kids > nice_kids_with_presents:
            print("Santa ran out of presents!")

    [print(*row, sep=" ") for row in matrix]

    if nice_kids == nice_kids_with_presents:
        print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
    else:
        print(f"No presents for {nice_kids - nice_kids_with_presents} nice kid/s.")


if __name__ == "__main__":
    main()
