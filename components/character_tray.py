import pygame.draw
from game.settings import *

from entities.character import Character


class CharacterTray:
    def __init__(self, roster, screen):
        self.width, self.height = pygame.display.get_desktop_sizes()[0]
        self.screen = screen
        self.roster = roster
        self.roster_placed_at = []
        self.selected_character = None
        self.character_placed_at = None
        self.dragging = False
        self._roster_positions_calculated = False

    def detect_input(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    self.detect_click_on_character((mouse_x, mouse_y))
                    self.dragging = True

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if self.dragging and self.selected_character:
                        mouse_x, mouse_y = event.pos
                        self.place_character(mouse_x, mouse_y)
                    self.dragging = False
                    self.selected_character = None

    def detect_click_on_character(self, mouse_position):
        self._calculate_roster_positions()

        for i, position in enumerate(self.roster_placed_at):
            distance_squared = (mouse_position[0] - position[0]) ** 2 + (mouse_position[1] - position[1]) ** 2
            if distance_squared < 25 * 25:
                self.selected_character = position[2]
                print(f"Click on character detected at {mouse_position}")
                break

    def _calculate_roster_positions(self):
        if self._roster_positions_calculated and len(self.roster_placed_at) == len(self.roster):
            return

        self.roster_placed_at = []
        character_position_x = 0
        character_position_y = 100
        character_offset = 100
        characters_per_row = 10

        for character in self.roster:
            if character_position_x > character_offset * (characters_per_row - 1):
                character_position_y += 100
                character_position_x = 0

            character_position_x += character_offset
            pos_x = character_position_x + character_offset
            self.roster_placed_at.append((pos_x, character_position_y, character))

        self._roster_positions_calculated = True

    def place_character(self, x, y):
        self.selected_character.x = x
        self.selected_character.y = y
        self.character_placed_at = self.selected_character

    def collect_placed_character(self):
        if self.character_placed_at:
            return self.character_placed_at
        return None

    def render(self):
        self._calculate_roster_positions()

        character_offset = 100
        characters_per_row = 10
        box_height = (len(self.roster) / characters_per_row) * 100

        pygame.draw.rect(self.screen, DARK_GRAY, (150, 50, characters_per_row * character_offset, box_height))

        for pos_x, pos_y, character in self.roster_placed_at:
            color = BRIGHT_BLUE if character == self.selected_character else BRIGHT_RED
            pygame.draw.circle(self.screen, color, (pos_x, pos_y), 25)

        if self.dragging and self.selected_character:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            pygame.draw.circle(self.screen, BRIGHT_GREEN, (mouse_x, mouse_y), 25)

        if self.character_placed_at:
            character = self.character_placed_at
            pygame.draw.circle(self.screen, YELLOW, (character.x, character.y), 25)