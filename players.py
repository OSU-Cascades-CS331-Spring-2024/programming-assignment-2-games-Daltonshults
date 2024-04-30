from math import inf 
'''
    Defines Player class, and subclasses Human and Minimax Player.
'''

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    #PYTHON: use obj.symbol instead
    def get_symbol(self):
        return self.symbol
    
    #parent get_move should not be called
    def get_move(self, board):
        raise NotImplementedError()


class HumanPlayer(Player):
    def __init__(self, symbol):
        Player.__init__(self, symbol)

    def clone(self):
        return HumanPlayer(self.symbol)
        
#PYTHON: return tuple instead of change reference as in C++
    def get_move(self, board):
        col = int(input("Enter col:"))
        row = int(input("Enter row:"))
        return col, row


class MinimaxPlayer(Player):

    def __init__(self, symbol):
        Player.__init__(self, symbol)
        if symbol == 'X':
            self.oppSym = 'O'
        else:
            self.oppSym = 'X'


    '''
    Notes:
        - Can use board.has_legal_moves_remaing(self, symbol) to see if any nodes are remaining.
        - Can use board.count_score(self, symbol) to get the score of a specific symbol on the board.
        - can use clone_of_board(self) to make moves, and pass new states down the tree.
        - Can use python math.inf to represent infinity.
    '''
    def get_move(self, board):
        return self.minimax(board, 4, self.symbol)
       
        

