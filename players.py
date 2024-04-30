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

        self.memo = {}
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

        return board.count_score(self.oppSym) - board.count_score(self.symbol)
    
    def get_child_nodes(self, symbol, board):
        legal_moves = board.get_legal_moves(symbol)

        children = []

        if len(legal_moves) == 0:
            return children
        
        else:
            for action in legal_moves:
                children.append(StateNode(state=board, parent=None, action=action, cost=None))

        return children
    

    def minimax(self, board, depth, symbol):
        action_taken = None
        board_hash = str(board.grid)

        if (board_hash, depth, symbol) in self.memo:
            return self.memo[(board_hash, symbol)]
        
        # If depth os 0 or node is terminal, return utility
        if depth == 0 or not board.has_legal_moves_remaining(symbol):
            result = self.simple_utility(board)
            self.memo[(board_hash, symbol)] = result, action_taken
            return result, action_taken
        
        # If Maximizing Player then
        if symbol != self.symbol:
    
            # Set value to negative infinity
            value = - inf
            
            # for each child of node do:
            for child in self.get_child_nodes(symbol, board):
                
                # Value = max(value, minimax(child, depth - 1, self.symbol))
                new_board = board.clone_of_board()
                new_board.play_move(child.action[0], child.action[1], self.oppSym)
                new_value, _ = self.minimax(new_board, depth - 1, self.symbol)
                value = max(value, new_value)
                if value == new_value:
                    action_taken = child.action
            

            # return value
            result = value, action_taken
            self.memo[(board_hash, symbol)] = result
            return value, action_taken

        # If Minimizing Player then
        if symbol == self.symbol:

            # Set value to positive infinity
            value = inf

            # for each child of node do:
            for child in self.get_child_nodes(symbol, board):

                # Value = min(value, minimax(child, depth - 1, self.oppSym))
                new_board = board.clone_of_board()
                new_board.play_move(child.action[0], child.action[1], self.symbol)
                new_value, _ = self.minimax(new_board, depth - 1, self.oppSym)
                value = min(value, new_value)

                if value == new_value:
                    action_taken = child.action

            result = value, action_taken
            self.memo[(board_hash, symbol)] = result
            # return value  
            return value, action_taken
        
        

       
        

