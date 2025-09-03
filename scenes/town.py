import pygame
from components.character_tray import CharacterTray
from entities.character import Character


class Town:
    def __init__(self, screen, clock, roster):
        self.screen = screen
        self.clock = clock
        self.roster = roster
        self.character_tray = CharacterTray(self.roster, self.screen)
        self.ui_font = pygame.font.SysFont('microsoftyahei', 20)

    def run(self, events):
        self.character_tray.render()

        for character in self.roster:
            character.render()

        pass