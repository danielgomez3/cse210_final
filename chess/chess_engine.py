

"""
 Description:

 OOP Principles Used:
   Inheritance, Abstraction, etc...

 Reasoning:
   This class uses inheritance because...
   This file uses polymorphism etc....
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
                ["wR","wN","wB","wQ","wK","wB","wN","wR"]]

        self.white_to_move = True
        self.move_log = []

    def make_move(self,move):
        self.board[move.start_row][move.start_col] = "--"
        self.board[move.end_row][move.end_col] = move.piece_moved
        self.move_log.append(move) # log the move so we can undo it later
        self.white_to_move = not self.white_to_move # This is how we swtich turns


"""
 Description:

 OOP Principles Used:
   Inheritance, Abstraction, etc...

 Reasoning:
   This class uses inheritance because...
   This file uses polymorphism etc....
"""
class Move(): 
    # If we want to log our moves and use chess notation, we need to change our system
    #to use ranks-file notation. We also need to flip our numbers around!:
    ranks_to_rows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    #This is a way to reverse our dictionary above! This says:
    # in v:k, V and K are created. This is how is the order of or Dictionary.
    # for k,v instantiates these 2 new seperate variables and are plugged into what items() spits out.
    # Thus v:k are set to the values of k,v respectively.
    # to read this better, read this backwards!
    rows_to_ranks = {v: k for k, v in ranks_to_rows.items()}
    files_to_cols = {"a": 0, "b":1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    cols_to_files = {v: k for k, v in files_to_cols.items()}

    def __init__(self, start_square, end_square, board):
        self.start_row = start_square[0]
        self.start_col = start_square[1]
        self.end_row = end_square[0]
        self.end_col = end_square[1]
        self.piece_moved = board[self.start_row][self.start_col]
        self.piece_captured = board[self.end_row][self.end_col]

    def get_chess_notation(self):
        return self.get_rank_file(self.start_row, self.start_col) + self.get_rank_file(self.end_row, self.end_col)

    def get_rank_file(self,r,c):
        return self.cols_to_files[c] + self.rows_to_ranks[r]
