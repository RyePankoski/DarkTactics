import pygame.draw

from scenes.battle_scene import BattleScene
from scenes.main_menu import MainMenu
from scenes.town import Town
from game.player import Player
from components.character_tray import CharacterTray


class Client:
    def __init__(self, screen, clock):
        roster = []
        self.screen = screen
        self.clock = clock

        #player
        self.player = Player(name="player", starting_gold=100, team_cap=4)

        #tray
        w, h = self.screen.get_size()
        tray_rect = (w - 380, 80, 360, h - 100)
        self.tray = CharacterTray(rect=tray_rect, title="Roster")

        #scenes
        self.main_menu = MainMenu(screen, clock)
        self.battle_scene = BattleScene(screen, clock, roster)
        self.town = Town(screen, clock, self.player, self.tray)
        self.scenes = {'main_menu': self.main_menu,'town': self.town, "battle_scene": self.battle_scene}
        self.state = 'main_menu'

        pass

    def run(self, events):
        scene = self.scenes[self.state]
        next_state = scene.run(events)
        if next_state and next_state in self.scenes:
            self.state = next_state
