import pygame.draw

from scenes.battle_scene import BattleScene


class Client:
    def __init__(self, screen, clock):
        roster = []
        self.battle_scene = BattleScene(screen, clock, roster)
        self.scenes = {"battle_scene": self.battle_scene}

        pass

    def run(self, events):
        for event in events:
            pass

        scene = self.scenes.get("battle_scene")
        scene.run(events)

        pass
