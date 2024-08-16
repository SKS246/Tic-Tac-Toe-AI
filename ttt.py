import numpy as np
import tkinter as tk

human_turn = True
no_of_turns = 0

# Creating the game board
game_board = np.zeros((3,3), int)


root = tk.Tk()
root.geometry("450x350")
root.title("Tic Tac Toe")

turn_label = tk.StringVar()
turn_label.set("Your Turn")
label = tk.Label(root, textvariable=turn_label)
label.grid()
label.place(x=200, y=5)

# Make Move
def make_move(row, column, game_board, turn):
    if game_board[row][column] == 1 or game_board[row][column] == 2:
        return ""
    else:
        game_board[row][column] = 1 if turn else 2
        return True

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

# AI Move
'''
Conditional Hierarchy for moving:
1. Play moves that make the bot win
2. Block the Opponent's Win
3. Play the Center
4. Random (First move in the list of all possible moves)
'''
def ai_move():
    global game_board
    game = np.copy(game_board)
    possible_moves = []

    # Look for possible moves
    for r in range(3):
        for c in range(3):
            if game_board[r][c] == 0:
                possible_moves.append((r, c))

    for i in possible_moves:
        game[i[0]][i[1]] = 2
        # Play the move which makes the bot win
        if check_bot_state(game):
            game_board[i[0]][i[1]] = 2
            return
        # If center is free, play there
        elif (1, 1) in possible_moves:
            game_board[1][1] = 2
            return
        else:
            game = np.copy(game_board)
    for i in possible_moves:
        game = np.copy(game_board)
        
        for p in possible_moves:
            game[p[0]][p[1]] = 1
            # play the move which would've made the opponent win
            if check_human_state(game):
                game_board[p[0]][p[1]] = 2
                return
            else:
                game = np.copy(game_board)
    # Play first possible move if none are better than the others
    game_board[possible_moves[0][0]][possible_moves[0][1]] = 2


# Button Click Function
def button_click(button, r, c):
    global game_board, human_turn, no_of_turns
    if make_move(r, c, game_board, human_turn) == "":
        turn_label.set("Can't place here. Please enter another valid spot.")
        return

    # Update the board with the player's move
    button.config(text="X")
    no_of_turns += 1

    # Check if the player has won after their move
    if check_human_state(game_board):
        turn_label.set("Human (Player 1) Won!")
        root.after(500, root.destroy)  # Close the window after a short delay
        return

    # Check if it's a draw
    if no_of_turns == 9:
        turn_label.set("It's a Tie!")
        root.after(500, root.destroy)  # Close the window after a short delay
        return

    # AI makes a move
    human_turn = False
    ai_move()

    # Update the board UI after AI move
    for i in range(3):
        for j in range(3):
            if game_board[i][j] == 2:
                buttons[i][j].config(text="O")

    no_of_turns += 1

    # Check if the AI has won after its move
    if check_bot_state(game_board):
        turn_label.set("Bot (Player 2) Won!")
        root.after(500, root.destroy)  # Close the window after a short delay
        return

    # Switch back to human turn
    human_turn = True
    turn_label.set("Your Turn")
                

# 2D array of buttons
buttons = []
for i in range(3):
    row_buttons = []
    for j in range(3):
        button = tk.Button(root, text="", height=4, width=8, 
                           command=lambda r=i, c=j: button_click(buttons[r][c], r, c))
        button.grid(row=i, column=j)
        button.place(x=30 + 130 * j, y=50 + 100 * i)
        row_buttons.append(button)
    buttons.append(row_buttons)


root.mainloop()