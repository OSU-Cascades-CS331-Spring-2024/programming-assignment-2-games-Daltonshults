from math import inf
from state_node import StateNode
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
            - Could use count score of 'X' and count score of 'O' to get a utility function
        - can use clone_of_board(self) to make moves, and pass new states down the tree.
        - Can use python math.inf to represent infinity.
        - The board represents the state of the game.
    '''
    def get_move(self, board):
        _, state = self.minimax(board, 5, self.symbol)
        return (state[0], state[1])
    
    def simple_utility(self, board):
        return board.count_score(self.symbol) - board.count_score(self.oppSym)
    
    def successors(self, symbol, board):
        legal_moves = board.get_legal_moves(symbol)

        successors = []

        if len(legal_moves) == 0:
            return successors
        
        else:
            for action in legal_moves:
                successors.append(StateNode(state=board, action=action))

        return successors
    
    def maxi(self, board, depth, alpha, beta):    
        # Set value to negative infinity
        max_value = - inf
        
        # for each child of node do:
        for child in self.successors(self.symbol, board):
            
            # Value = max(value, minimax(child, depth - 1, self.symbol))
            child.board = board.clone_of_board()
            child.board.play_move(child.action[0], child.action[1], self.symbol)
            new_value, _ = self.minimax(child.board, depth - 1, False, alpha=alpha, beta=beta)

            #max_value = max(max_value, new_value)
            alpha = max(alpha, new_value)
            if max_value < new_value:
                action_taken = child.action
                max_value = new_value

            if beta <= alpha:
                break
        
        # return value
        return max_value, action_taken
    
    def mini(self, board, depth, alpha, beta):    
        # Set value to positive infinity
        min_value = inf

        # for each child of node do:
        for child in self.successors(self.oppSym, board):

            # Value = min(value, minimax(child, depth - 1, self.oppSym))
            child.board = board.clone_of_board()
            child.board.play_move(child.action[0], child.action[1], self.oppSym)
            new_value, _ = self.minimax(child.board, depth - 1, True, alpha=alpha, beta=beta)

            # new_value, _ = self.minimax(new_board, depth - 1, self.symbol, alpha=alpha, beta=beta)
            beta = min(beta, new_value)
            if min_value > new_value:
                action_taken = child.action
                min_value = new_value

            if beta <= alpha:
                break
            
        return min_value, action_taken
    
    def minimax(self, board, depth, maximizing, alpha=-inf, beta=inf):
        action_taken = None

        # If depth os 0 or node is terminal, return utility
        if depth == 0 or not board.has_legal_moves_remaining(self.symbol if maximizing else self.oppSym):
            result = self.simple_utility(board)
            return result, action_taken
        
        # If Maximizing Player then
        if maximizing:
            return self.maxi(board=board, depth=depth, alpha=alpha, beta=beta)

        # If Minimizing Player then
        else:
            return self.mini( board=board, depth=depth, alpha=alpha, beta=beta)
        
        

       
        

