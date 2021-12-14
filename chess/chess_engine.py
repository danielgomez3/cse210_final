

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

        self._white_to_move = True
        self._move_log = []

    def make_move(self,move):
        self.board[move.start_row][move.start_col] = "--"
        self.board[move.end_row][move.end_col] = move.piece_moved
        self._move_log.append(move) # log the move so we can undo it later
        self._white_to_move = not self._white_to_move # This is how we swtich turns

"""
 Description:

 OOP Principles Used:
   Polymorphism, Encapsulation

 Reasoning:
   We name what a move might do. In the future there could be more kinds 
   of moves(What about 4-player chess, or a fun mini game where there are special moves???).
   But for now we make a template on what a move could be like.
   This isn't an Abstract Class exactly per-se because we instantiate
   attributes to be inherited from its child classes.
   We use Encapsulation because in our __init__, we denote attributes
   that don't need to be altered any further and ought not to be rewritten with
   an '_' underscore.
"""
class Move():
    # If we want to log our moves and use chess notation, we need to change our system
    #to use ranks-file notation. We also need to flip our numbers around!:
    _ranks_to_rows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    #This is a way to reverse our dictionary above! This says:
    # in v:k, V and K are created. This is how is the order of or Dictionary.
    # for k,v instantiates these 2 new seperate variables and are plugged into what items() spits out.
    # Thus v:k are set to the values of k,v respectively.
    # to read this better, read this backwards!
    _rows_to_ranks = {v: k for k, v in _ranks_to_rows.items()}
    _files_to_cols = {"a": 0, "b":1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    _cols_to_files = {v: k for k, v in _files_to_cols.items()}
    def __init__(self):
        pass

    def set_chess_notation_conversion(self):
        pass
    def get_current_position(self):
        pass


"""
 Description:

 OOP Principles Used:
   Abstaction, Inheritance

 Reasoning:
   This class uses Abstraction because in the get_chess_notation and 
   get_rank_file methods, we don't define anything, but just returns. 
   The existence of these methods in reality  are just concepts, and rely 
   on other information to have purpose. What's interesting about these two methods
   in hindsight, is that their function would change completely if the information they
   borrowed changed!
   The way we use Inheritance is more apparent because of directly Inhereting attributes
   from the Move() class
"""
class Player_move(Move): 

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
        return self._cols_to_files[c] + self._rows_to_ranks[r]
