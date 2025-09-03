import uuid


class Character:
    def __init__(self, name, hp=100, atk=10, x=0, y=0):
        self.id = str(uuid.uuid4())
        self.name = name
        self.hp = hp
        self.hp_max = hp
        self.atk = atk
        self.x = x
        self.y = y
        self.dx = 1
        self.dy = 1

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            return True
        return False

    def is_alive(self):
        return self.hp > 0

    def is_dead(self):
        return self.hp <= 0

    def heal_full(self):
        self.hp = self.hp_max

    def __repr__(self):
        return f'<character: {self.name}HP:{self.hp}/{self.hp_max} ATK:{self.atk}>'

