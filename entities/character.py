class Character:
    def __init__(self, name, rank, team, x, y):
        self.name = name
        self.rank = rank
        self.team = team
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0

    def move(self):
        self.x += self.dx
        self.y += self.dy
