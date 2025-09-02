class Character:
    def __init__(self, name, rank, x, y):
        self.name = name
        self.rank = rank
        self.x = x
        self.y = y
        self.dx = 1
        self.dy = 1

    def move(self):
        self.x += self.dx
        self.y += self.dy
