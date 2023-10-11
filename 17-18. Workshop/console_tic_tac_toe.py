def is_valid_sign(player_one_sign_):
    return player_one_sign_ in ['X', '0']


def render_board(board_):
    for row in board_:
        print("| ", end="")
        print(" | ".join([sign if sign else '' for sign in row]), end="")
        print(" |")


def is_row_win(board_):
    for row in board_:
        if len(set(row)) == 1 and set(row) != {None}:
            return True
        return False


def is_column_win(board_, current_sign_):
    for col_ in range(len(board_)):
        current_column = []
        for row in range(len(board_)):
            current_column.append(board_[row][col_] == current_sign_)
        if all(current_column):
            return True
    return False


def is_diagonal_win(board_, current_sign_):
    diagonal_1, diagonal_2 = [], []
    for i in range(len(board_)):
        diagonal_1.append(board_[i][i] == current_sign_)
        diagonal_2.append(board_[i][len(board_) - 1 - i] == current_sign_)
    return all(diagonal_1) or all(diagonal_2)


def is_win(board_, current_sign_):
    return any([is_row_win(board_), is_column_win(board_, current_sign_), is_diagonal_win(board_, current_sign_)])


def is_row_win_possible(board_):
    if all(['X' in row_ and 'O' in row_ for row_ in board_]):
        return False
    return True


def is_col_win_possible(board_):
    columns = []
    for col_ in range(len(board_)):
        current_column = []
        for row_ in range(len(board_)):
            current_column.append(board_[row_][col_])
        columns.append(current_column)
    if all(['X' in col_ and 'O' in col_ for col_ in board_]):
        return False
    return True


def is_diagonal_win_possible(board_):
    diagonal_1, diagonal_2 = [], []
    for index in range(len(board_)):
        diagonal_1.append(board_[index][index])
        diagonal_2.append(board_[index][len(board_) - 1 - index])
    if 'X' in diagonal_1 and 'O' in diagonal_1 and 'X' in diagonal_2 and 'O' in diagonal_2:
        return False
    return True


def is_draw(board_):
    if any([is_row_win_possible(board_), is_col_win_possible(board_), is_diagonal_win_possible(board_)]):
        return False
    return True


def choice_is_valid(board_, choice_, position_mapper_):
    if not choice_.isdigit():
        return False
    choice_ = int(choice_)
    if choice_ not in position_mapper_:
        print("Invalid choice")
        return False
    if board_[position_mapper_[choice_][0]][position_mapper_[choice_][1]]:
        print("Position taken")
        return False
    return True


def main():
    player_one = input("Player one name: ").strip()
    player_two = input("Player two name: ").strip()

    while True:
        player_one_sign = input(f"{player_one}, would you like to play with 'X' or '0'?")
        if is_valid_sign(player_one_sign):
            break
        print('Please, enter one of "X" or "0"!')
    player_two_sign = 'X' if player_one_sign == '0' else '0'

    SIZE = 3
    board = [[None] * SIZE for _ in range(SIZE)]
    position_mapper = {i + 1: (i // SIZE, i % SIZE) for i in range(SIZE * SIZE)}

    print('This is the numeration of the board:')
    [print(f"| {' | '.join([str(i + 1 + row * SIZE) for i in range(SIZE)])} |") for row in range(SIZE)]
    print(f"{player_one} starts first!")

    turn = 1

    while True:
        current_player = player_one if turn % 2 else player_two
        current_sign = player_one_sign if turn % 2 else player_two_sign
        while True:
            choice = input(f"{current_player} choose a free position [1-9]: ").strip()
            if choice_is_valid(board, choice, position_mapper):
                break
        row, col = position_mapper[int(choice)]
        board[row][col] = current_sign
        render_board(board)
        if is_win():
            print(f"{current_player} has won!")
            break
        if is_draw():
            print("Draw!")
            break

        turn += 1


if __name__ == "__main__":
    main()
