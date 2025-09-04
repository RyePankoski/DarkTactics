import pygame
from components.character_tray import CharacterTray
from entities.character import Character
from game.settings import *


class BattleScene:
    def __init__(self, screen, clock, roster):
        self.screen = screen
        self.clock = clock
        self.ui_font = pygame.font.SysFont('microsoftyahei', 20)
        self.roster = []
        self.roster = roster
        self.units_on_battleground = []

        for _ in range(50):
            new_character = Character("soldier", "private", 1, 500 + _ + 10, 500 + _ + 10)
            self.roster.append(new_character)

        self.character_tray = CharacterTray(self.roster, self.screen)

    def run(self, events):
        self.character_tray.render()
        self.character_tray.detect_input(events)
        self.collect_placed_units()
        self.render()
        pass

    def collect_placed_units(self):
        if self.character_tray.character_placed_at:
            self.units_on_battleground.append(self.character_tray.character_placed_at)
            if self.character_tray.character_placed_at in self.roster:
                self.roster.remove(self.character_tray.character_placed_at)
            self.character_tray.character_placed_at = None

    def render(self):
        for character in self.units_on_battleground:
            pygame.draw.circle(self.screen, RED, (character.x, character.y), 25)
