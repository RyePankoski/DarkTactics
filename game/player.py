from entities.currency import Currency
from game.roster import Roster

class Player:
    def __init__(self, name = 'player', starting_gold=100, team_cap = 4):
        self.name = name
        self.currency = Currency()
        self.roster = Roster(team_cap = team_cap)

    #recruitment
    def can_recruit(self, cost):
        return self.currency.can_afford(cost)

    def recruit(self, character, cost):
        if self.currency.spend(cost):
            self.roster.add(character)
            return True
        return False

    def heal_all(self, cost=0):
        if cost > 0 and not self.currency.spend(cost):
            return False
        self.roster.heal_all()
        return True

    #currency
    def award_gold(self, amount):
        self.currency.earn(amount)

    def gold_balance(self):
        return self.currency.balance()

    #team mgmt
    def select_for_team(self, cid):
        return self.roster.select(cid)

    def deselect_from_team(self, cid):
        return self.roster.deselect(cid)

    def clear_team(self):
        return self.roster.clear_team()