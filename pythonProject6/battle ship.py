import random

# Инициализация игрового поля
board = [['-' for _ in range(6)] for _ in range(6)]

# Вывод игрового поля на экран
def print_board(board):
    for row in board:
        print(' '.join(row))

# Функция для определения победителя
def check_win(board, player):
    for row in board:
        if row.count(player) == 6:
            return True
    for col in range(6):
        if all([board[row][col] == player for row in range(6)]):
            return True
    if all([board[i][i] == player for i in range(6)]):
        return True
    if all([board[i][5-i] == player for i in range(6)]):
        return True
    return False

# Функция для сделать ход
def make_move(board, player, row, col):
    if board[row][col] == '-':
        board[row][col] = player
        return True
    else:
        return False

# Функция для хода ИИ
def make_ai_move(board, ai):
    while True:
        row = random.randint(0, 5)
        col = random.randint(0, 5)
        if make_move(board, ai, row, col):
            break

# Основной цикл игры
def play_game():
    players = ['X', 'O']
    ai = players[random.randint(0,1)]
    human = 'X' if ai == 'O' else 'O'

    turn = 0
    while True:
        print_board(board)
        player = players[turn % 2]
        if player == ai:
            make_ai_move(board, ai)
        else:
            while True:
                try:
                    row, col = map(int, input(f"Player {player}, enter row and column: ").split())
                    if make_move(board, player, row, col):
                        break
                    else:
                        print("This cell is already occupied. Try again.")
                except ValueError:
                    print("Invalid input. Try again.")
        if check_win(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        if all([cell != '-' for row in board for cell in row]):
            print_board(board)
            print("It's a tie!")
            break
        turn += 1

# Запуск игры
play_game()