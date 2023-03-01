class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0 # Needed in my brain implementation
        self.turn_points = 0 # each player is aware of his/her hand running points

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
