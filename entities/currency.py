class Currency:
    def __init__(self, starting_gold = 100):
        self.gold = max(0, starting_gold)

    def balance(self):
        return self.gold

    def can_afford(self, amount):
        return 0 <= amount <= self.gold

    #commands
    def earn(self, amount):
        if amount < 0:
            return
        self.gold += amount

    def spend(self, amount):
        if amount < 0:
            return False
        if self.gold >= amount:
            self.gold -= amount
            return True
        return False

    #admin
    def set(self, amount):
        self.gold = max(0, amount)


