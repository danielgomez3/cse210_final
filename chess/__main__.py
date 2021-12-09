"""
Name: Daniel Gomez
Description:
    This is my chess game in which I may use pygame as a library.
    Made using git verion control, vim, and my custom vim IDE.
    Thank you for reading :)
"""
import pygame as p
import chess_engine

WIDTH = HEIGHT = 512
DIMENSION = 8 #dimensions of a chessboard are 8x8
SQUARE_SIZE = HEIGHT // DIMENSION # This is the width and height of the board divded evenly into 8 Squares!
MAX_FPS = 15
IMAGES = {}

def load_images():
    # slow way: IMAGES['bp'] = p.images.load("images/bp.png"), 12 times
    pieces = ['wP','wN','wB','wR','wQ','wK','bP','bN','bB','bR','bQ','bK']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQUARE_SIZE, SQUARE_SIZE))

"""
The main driver for our code. This will handle user input and updating graphics
"""
def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = chess_engine.Gamestate()
    load_images() # only do his once before the game loop
    running = True
    while running:
        for e in p.event.get():
            if e.type ==  p.QUIT:
                running = False # if we hit 'x', the game will quite
        
        draw_game_state(screen,gs)
        clock.tick(MAX_FPS)
        p.display.flip()

def draw_game_state(screen,gs):
    draw_board(screen) # draw squares on the board
    draw_pieces(screen,gs.board)

"""
Draw squares
    the top left square is always white
    we strt with a white square (top right) if you add up the row and the collumn,
    and divide it by 2 (e.g coord. 0,0: 0 + 0 = 0/2 = 0)
    all light squares have 1 parity.
    all dark squares will have an odd parity, meaning they will have a remainder when divided by 2.
    (e.g coord 1,0 to right. 1 + 1 = 1. 1/2 =.5 is the remainder (1 IOW)
    Collumn is left & right, row is up and down!
"""
def draw_board(screen):
    colors = [p.Color("white"), p.Color("gray")] #white is indexed with 0,grey 1
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)] # if there answer is 1, color is grey
            # if 0, color is white
            # draw the square spaces for the board
            p.draw.rect(screen, color, p.Rect(c*SQUARE_SIZE, r*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)) 
            # p.Rect() object takes x,y, and dimesions by coordinates
"""
Draw pieces
"""
def draw_pieces(screen,board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c] 
            if piece != "--": # if it's not an empty space
                screen.blit(IMAGES[piece], p.Rect(c*SQUARE_SIZE, r*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))  # Blit means draw them 



if __name__ == "__main__":
    main()
