class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def add_score(self, points):
        self.score += points

    def get_score(self):
        return self.score