class StateNode:

    def __init__(self, state, parent, action, cost):
        self.state = state
        self.parent = parent
        self.aciton = action
        self.cost = cost
    

    def get_state(self):
        return self.state
    
    def get_parent(self):
        return self.parent
    
    def get_action(self):
        return self.action
    
    def get_cost(self):
        return self.cost
    
    def set_state(self, state):
        self.state = state

    def set_parent(self, parent):
        self.parent = parent
    
    def set_action(self, action):
        self.action = action

    def set_cost(self, cost):
        self.cost = cost

    def __str__(self):
        return f"State: {self.state},\nParent: {self.parent},\nAction: {self.action},\n Cost: {self.cost}"