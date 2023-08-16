import random

def create_board(rows, cols, num_mines):
    board = [[' ' for _ in range(cols)] for _ in range(rows)]
    mines = random.sample(range(rows * cols), num_mines)
    for mine in mines:
        row = mine // cols
        col = mine % cols
        board[row][col] = 'X'
    return board

def count_adjacent_mines(board, row, col):
    count = 0
    for i in range(max(0, row - 1), min(row + 2, len(board))):
        for j in range(max(0, col - 1), min(col + 2, len(board[0]))):
            if board[i][j] == 'X':
                count += 1
    return count

def reveal_cell(board, revealed, row, col):
    if revealed[row][col]:
        return
    revealed[row][col] = True
    if board[row][col] == 'X':
        return
    if count_adjacent_mines(board, row, col) == 0:
        for i in range(max(0, row - 1), min(row + 2, len(board))):
            for j in range(max(0, col - 1), min(col + 2, len(board[0]))):
                reveal_cell(board, revealed, i, j)

def print_board(board, revealed):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if revealed[i][j]:
                print(board[i][j], end=' ')
            else:
                print('-', end=' ')
        print()

def play_game(rows, cols, num_mines):
    board = create_board(rows, cols, num_mines)
    revealed = [[False for _ in range(cols)] for _ in range(rows)]
    game_over = False

    while not game_over:
        print_board(board, revealed)
        row = int(input('Enter row: '))
        col = int(input('Enter column: '))

        if board[row][col] == 'X':
            print('Game over!')
            game_over = True
        else:
            reveal_cell(board, revealed, row, col)
            if all(all(revealed[i][j] or board[i][j] == 'X' for j in range(cols)) for i in range(rows)):
                print('You win!')
                game_over = True

play_game(8, 8, 10)
