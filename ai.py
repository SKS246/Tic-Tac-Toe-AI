import ttt
import numpy as np


# AI Move
'''
Conditional Hierarchy for moving:
1. Play moves that make the bot win
2. Block the Opponent's Win
3. Play the Center
4. Random (First move in the list of all possible moves)
'''

def ai_move(g):
    game = np.copy(g)
    possible_moves = []

    # Look for possible moves
    for r in range(3):
        for c in range(3):
            if g[r][c] == 0:
                possible_moves.append((r, c))

    for i in possible_moves:
        game[i[0]][i[1]] = 2
        # Play the move which makes the bot win
        if ttt.check_bot_state(game):
            g[i[0]][i[1]] = 2
            return
        else:
            game = np.copy(g)
            pm = possible_moves
            
            # If center is free, play there
            if (1, 1) in pm:
                g[1][1] = 2
                return

            for p in pm:
                game[p[0]][p[1]] = 1
                # play the move which would've made the opponent win
                if ttt.check_human_state(game):
                    g[p[0]][p[1]] = 2
                    return
                else:
                    game = np.copy(g)
    # Play first possible move if none are better than the others
    g[possible_moves[0][0]][possible_moves[0][1]] = 2