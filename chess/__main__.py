"""
 Description:
    This File uses uses the chess_engine.py file and imports its classes, the classes methods, and attributes to use in the Game Loop

 OOP Principles Used:
   Inheritance

 Reasoning:
   This class uses inheritance because...
   This file uses polymorphism etc....
"""

import pygame as p
import chess_engine

WIDTH = HEIGHT = 512
DIMENSION = 8 #dimensions of a chessboard are 8x8
SQUARE_SIZE = HEIGHT // DIMENSION # This is the width and height of the board divded evenly into 8 large squares, To see them divided into the indiv. 64 squares, see line 8 and 82
MAX_FPS = 15
IMAGES = {}

def load_images():
    # slow way: IMAGES['bp'] = p.images.load("images/bp.png"), 12 times
    pieces = ['wP','wN','wB','wR','wQ','wK','bP','bN','bB','bR','bQ','bK']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQUARE_SIZE, SQUARE_SIZE))

"""
 Description:
    This File uses uses the chess_engine.py file and imports its classes, the classes methods, and attributes to use in the Game Loop

 OOP Principles Used:
   Inheritance, Abstraction, etc...

 Reasoning:
   This class uses inheritance because...
   This file uses polymorphism etc....
"""
def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = chess_engine.Gamestate()
    load_images() # only do his once before the game loop
    running = True
    sq_selected = () # keep track of the last click of the user. this is a Tuple
    player_clicks = [] # this is a list. Will have two tuples: [(4,2),(4,4)]
    print(type(player_clicks))

    while running:
        for e in p.event.get():
            if e.type ==  p.QUIT:
                running = False # if we hit 'x', the game will quite
            elif e.type == p.MOUSEBUTTONDOWN: # if we click(e.type == event.type)
                location = p.mouse.get_pos() #returns an (x,y) location of the mouse
                
                # This is how we are able to divide rows and columns of where the mouse is
                #we take the x coord [0] of the location and divide it by the size of the square
                col = location[0] // SQUARE_SIZE 
                row = location[1] // SQUARE_SIZE 
                if sq_selected == (row, col): #if the user clicke the same row twice, BAD
                    sq_selected = () #re initialize to clear
                    player_clicks = [] # clear player clicks
                else: # If they did click the right square tho..
                    sq_selected = (row, col)
                    player_clicks.append(sq_selected) # append for both 1st and 2nd clicks

                if len(player_clicks) == 2: #What happens if they click twice:
                    move = chess_engine.Player_move(player_clicks[0], player_clicks[1], gs.board)
                    print(move.get_chess_notation())
                    gs.make_move(move)
                    sq_selected = () # reset the user clicks
                    player_clicks = []

        
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
