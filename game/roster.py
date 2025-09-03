class Roster:
    def __init__(self, team_cap: int = 4):
        self.characters = []
        self.team_ids = []
        self.team_cap = team_cap

    def add(self, character):
        if any(c.id == character.id for c in self.characters):
            return False
        self.characters.append(character)
        return True

    def remove(self, character):
        if character in self.characters:
            self.characters.remove(character)
            if character.id in self.team_ids:
                self.team_ids.remove(character.id)
            return True
        return False

    def get(self):
        return list(self.characters)

    def count(self):
        return len(self.characters)

    def contain(self, character):
        return character in self.characters

    #team ops
    def select(self, character_id):
        if character_id in self.team_ids:
            return False
        if not any(c.id == character_id for c in self.characters):
            return False
        if len(self.team_ids) >= self.team_cap:
            return False
        self.team_ids.append(character_id)
        return True

    def deselect(self, character_id):
        if character_id in self.team_ids:
            self.team_ids.remove(character_id)
            return True
        return False

    def clear_team(self) -> None:
        self.team_ids.clear()

    def heal_all(self):
        for character in self.characters:
            character.heal()