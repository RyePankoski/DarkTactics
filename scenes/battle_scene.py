import pygame
from components.character_tray import CharacterTray
from entities.character import Character


class BattleScene:
    def __init__(self, screen, clock, roster):
        self.screen = screen
        self.clock = clock
        self.ui_font = pygame.font.SysFont('microsoftyahei', 20)
        self.roster = roster
        self.character_tray = CharacterTray(self.roster, self.screen)

    def run(self, events):

        self.character_tray.render()

        for character in self.roster:
            character.move()
            pygame.draw.circle(self.screen, (255, 0, 0), (character.x, character.y), 5)
        pass
