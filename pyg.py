import pygame
import numpy as np
import ttt

# Pygame Variables
WIDTH = 600
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Game Variables
human_turn = True
end = False
human_won = False
bot_won = False
no_of_turns = 0
running = True

game_board = np.zeros((3,3), int)

text_font = pygame.font.SysFont("Anek Devanagari", 60)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            for i in game_board:
                for j in i:
                    print(j)

    screen.fill("cadetblue2")



    # GAME LOGIC

    # Lines Canvas
    pygame.draw.line(screen, "black", (WIDTH/3, HEIGHT/3), (WIDTH/3, HEIGHT), width=2)
    pygame.draw.line(screen, "black", (2*WIDTH/3, HEIGHT/3), (2*WIDTH/3, HEIGHT), width=2)

    pygame.draw.line(screen, "black", (0, HEIGHT/3), (WIDTH, HEIGHT/3), width=2)
    pygame.draw.line(screen, "black", (0, 5*HEIGHT/9), (WIDTH, 5*HEIGHT/9), width=2)
    pygame.draw.line(screen, "black", (0, 7*HEIGHT/9), (WIDTH, 7*HEIGHT/9), width=2)


    
    if human_turn:
        draw_text("Player 1 Play", text_font, "limegreen", WIDTH/5 + 50, HEIGHT/7)
    else:
        draw_text("Player 2 Play", text_font, "black", WIDTH/5 + 50, HEIGHT/7)



    pygame.display.flip()

    clock.tick(60)

pygame.quit()
