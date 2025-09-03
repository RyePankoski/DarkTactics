import pygame.draw

from scenes.battle_scene import BattleScene
from scenes.main_menu import MainMenu


class Client:
    def __init__(self, screen, clock):
        roster = []

        #scenes
        self.main_menu = MainMenu(screen, clock)
        self.battle_scene = BattleScene(screen, clock, roster)
        self.scenes = {'main_menu': self.main_menu, "battle_scene": self.battle_scene}
        self.state = 'main_menu'

        pass

    def run(self, events):
        for event in events:
            pass

        scene = self.scenes.get('main_menu')
        scene.run(events)

        pass
