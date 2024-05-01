class StateNode:

    def __init__(self, state, action):
        self.state = state
        self.action = action

    def get_state(self):
        return self.state
    
    def get_action(self):
        return self.action
    
    def set_state(self, state):
        self.state = state

    def set_action(self, action):
        self.action = action


    def __str__(self):
        return f"State: {self.state},\nParent: {self.parent},\nAction: {self.action},\n Cost: {self.cost}"