import pygame.draw

from scenes.battle_scene import BattleScene


class Client:
    def __init__(self, screen, clock):
        self.battle_scene = BattleScene(screen, clock)
        pass

    def run(self, events):

        for event in events:
            pass

        self.battle_scene.run()
        pass
