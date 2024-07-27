import random

def new_game():
    board = [[0] * 4 for _ in range(4)]
    add_new_tile(board)
    add_new_tile(board)
    return board

def add_new_tile(board):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = 2 if random.random() < 0.9 else 4

def print_board(board):
    for row in board:
        print("\t".join(map(str, row)))
    print()

def merge(row):
    pair = False
    new_row = []
    for i in range(len(row)):
        if pair:
            new_row.append(2 * row[i])
            pair = False
        else:
            if i + 1 < len(row) and row[i] == row[i + 1]:
                pair = True
                new_row.append(2 * row[i])
            else:
                new_row.append(row[i])
    new_row += [0] * (len(row) - len(new_row))
    return new_row

def move(board, direction):
    for i in range(4):
        if direction == "left":
            board[i] = merge([num for num in board[i] if num != 0])
        elif direction == "right":
            board[i] = merge([num for num in board[i][::-1] if num != 0])[::-1]
    return board

def transpose(board):
    return [[board[j][i] for j in range(4)] for i in range(4)]

def invert(board):
    return [row[::-1] for row in board]

def move_up(board):
    board = transpose(board)
    board = move(board, "left")
    board = transpose(board)
    return board

def move_down(board):
    board = transpose(board)
    board = move(board, "right")
    board = transpose(board)
    return board

def play():
    board = new_game()
    print_board(board)
    while True:
        move_direction = input("Enter move direction (w/a/s/d): ").strip().lower()
        if move_direction in ['w', 'a', 's', 'd']:
            if move_direction == 'w':
                board = move_up(board)
            elif move_direction == 's':
                board = move_down(board)
            elif move_direction == 'a':
                board = move(board, 'left')
            elif move_direction == 'd':
                board = move(board, 'right')
            add_new_tile(board)
            print_board(board)
        else:
            print("Invalid input. Please enter w, a, s, or d.")

play()
