"""
Responsible for:
*storing all information about current state of the game
*dermines the valid moves!
*keeps a move log.
"""

class Gamestate():
    def __init__(self):
        #8x8 2D list
        self.board = [
                ["bR","bN","bB","bQ","bK","bB","bN","bR"],
                ["bP","bP","bP","bP","bP","bP","bP","bP"],
                ["--","--","--","--","--","--","--","--"],
                ["--","--","--","--","--","--","--","--"],
                ["--","--","--","--","--","--","--","--"],
                ["--","--","--","--","--","--","--","--"],
                ["wP","wP","wP","wP","wP","wP","wP","wP"],
                ["wR","wN","wB","wQ","wK","wB","wN","wR"]
                ]
        self.whiteToMove = True
        self.moveLog = []



