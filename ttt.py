import numpy as np
import ai

human_turn = True
end = False
human_won = False
bot_won = False
no_of_turns = 0

# Creating the game board
game_board = np.zeros((3,3), int)


# Make Move
def make_move(row, column, game_board, turn):
    if game_board[row][column] == 1 or game_board[row][column] == 2:
        return ""
    else:
        if turn:
            game_board[row][column] = 1
        else:
            game_board[row][column] = 2

# Check if Human (Player 1) has won, returns true if they have
def check_human_state(game_board):
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
def check_bot_state(game_board):
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

# Game Loop
def Main():
    global human_turn
    global no_of_turns
    global game_board
    while True:
        # When to end
        if check_human_state(game_board):
            print("Human (Player 1) Won")
            break
        elif check_bot_state(game_board):
            print("Bot (Player 2) Won")
            break
        elif no_of_turns == 9:
            print("Tie")
            break
        else:
            if human_turn:
                r = (int(input("Player 1 which row do you want to place your piece in: ")) - 1)
                c = (int(input("Player 1 which column do you want to place your piece in: ")) - 1)
                # If another piece has been played at that spot don't allow the player to play there
                if make_move(r, c, game_board, human_turn) == "":
                    print("\nCan't place here. Please enter another valid spot.")
                    print(game_board)
                else:
                    make_move(r, c, game_board, human_turn)
                    print(game_board)
                    human_turn = False
                    no_of_turns += 1

            else:
                ai.ai_move(game_board)
                print(game_board)
                human_turn = True
                no_of_turns += 1

if __name__ == "__main__":
    Main()
