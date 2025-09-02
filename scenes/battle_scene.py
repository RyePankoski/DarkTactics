import pygame
from components.character_tray import CharacterTray
from entities.character import Character


class BattleScene:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.ui_font = pygame.font.SysFont('microsoftyahei', 20)
        character_tray = CharacterTray()

        self.player1characters = []

        character = Character("simao", "general", 500, 500)
        self.player1characters.append(character)

    def run(self):
        for character in self.player1characters:
            character.move()
            pygame.draw.circle(self.screen, (255,0,0), (character.x, character.y), 5)
        pass
