import ttt
import random

def generate(start, end):
    row = random.randint(start, end)
    column = random.randint(start, end)

    return row, column

def ai_move(game_board):
    while True:
        row, column = generate(0, 2)

        if game_board[row][column] == 1 or game_board[row][column] == 2:
            row, column = generate(0, 2)
        else:
            break
    
    game_board[row][column] = 2
