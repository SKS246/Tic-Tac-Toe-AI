import numpy as np

human_turn = True
end = False
human_won = False
bot_won = False
no_of_turns = 0

# Creating the game board
game_board = np.zeros((3,3), int)


# Make Move
def make_move(row, column):
    if human_turn:
        game_board[row][column] = 1
    else:
        game_board[row][column] = 2


# Check if Human (Player 1) has won, returns true if they have
def check_human_state():
    # Check all 3 rows
    for i in range(3):
        if game_board[i][0] == game_board[i][1] == game_board[i][2] == 1:
            return True
    
    # Check all 3 columns
    for i in range(3):
        if game_board[0][i] == game_board[1][i] == game_board[2][i] == 1:
            return True
    
    # Check First Diagonal
    if game_board.diagonal()[0] == game_board.diagonal()[1] == game_board.diagonal()[2] == 1:
        return True
    else:
        # Check Second Diagonal
        if np.flipud(game_board).diagonal()[0] == np.flipud(game_board).diagonal()[1] == np.flipud(game_board).diagonal()[2]  == 1:
            return True
        else:
            return False

# Check if Bot (Player 2) has won, returns true if they have
def check_bot_state():
    # Check all 3 rows
    for i in range(3):
        if game_board[i][0] == game_board[i][1] == game_board[i][2] == 2:
            return True
    
    # Check all 3 columns
    for i in range(3):
        if game_board[0][i] == game_board[1][i] == game_board[2][i] == 2:
            return True
    
    # Check First Diagonal
    if game_board.diagonal()[0] == game_board.diagonal()[1] == game_board.diagonal()[2] == 2:
        return True
    else:
        # Check Second Diagonal
        if np.flipud(game_board).diagonal()[0] == np.flipud(game_board).diagonal()[1] == np.flipud(game_board).diagonal()[2]  == 2:
            return True
        else:
            return False

def Main():

    for i in range(3):
        make_move(2, i)
    print(game_board)
    if check_human_state():
        print("Human has won")


Main()

