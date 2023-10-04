def is_inside_matrix(row, col, n):
    return 0 <= row < n and 0 <= col < n


def main():
    number_of_presents = int(input())
    n = int(input())

    matrix = []
    for row in range(5):
        matrix.append(input().split())
        for col in range(5):
            if matrix[row][col] == 'A':
                my_position = [row, col]
            elif matrix[row][col] == 'x':
                targets += 1

    directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    hits = []


if __name__ == "__main__":
    main()






def main():
    m = int(input())
    n = int(input())

    neighborhood = [list(input().split()) for _ in range(n)]

    santa_row, santa_col = None, None
    nice_kids_count = 0

    for i in range(n):
        for j in range(n):
            if neighborhood[i][j] == "S":
                santa_row, santa_col = i, j
            elif neighborhood[i][j] == "V":
                nice_kids_count += 1

    commands = ["up", "down", "left", "right"]

    for _ in range(m):
        command = input()
        if command == "Christmas morning":
            break

        new_row, new_col = santa_row, santa_col

        if command == "up":
            new_row -= 1
        elif command == "down":
            new_row += 1
        elif command == "left":
            new_col -= 1
        elif command == "right":
            new_col += 1

        if is_inside_matrix(new_row, new_col, n):
            cell_value = neighborhood[new_row][new_col]
            if cell_value == "V":
                m -= 1
                nice_kids_count -= 1
                neighborhood[new_row][new_col] = "-"
            elif cell_value == "C":
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    r, c = santa_row + dr, santa_col + dc
                    if is_inside_matrix(r, c, n) and neighborhood[r][c] == "V":
                        m -= 1
                        nice_kids_count -= 1
                        neighborhood[r][c] = "-"

            santa_row, santa_col = new_row, new_col

    print("\n".join([" ".join(row) for row in neighborhood]))

    if nice_kids_count == 0:
        print(f"Good job, Santa! {nice_kids_count} happy nice kid/s.")
    else:
        print(f"No presents for {nice_kids_count} nice kid/s.")

    if m <= 0 < nice_kids_count:
        print("Santa ran out of presents!")


if __name__ == "__main__":
    main()
