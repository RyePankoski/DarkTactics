# scenes/town.py
import pygame
import random
from entities.character import Character

ADJECTIVES = ["Grim", "Swift", "Stout", "Brave", "Clever", "Fierce", "Calm", "Nimble"]
CLASSES     = ["Swordsman", "Archer", "Cleric", "Guard", "Scout", "Pikeman", "Rogue"]

def roll_recruit():
    name = f"{random.choice(ADJECTIVES)} {random.choice(CLASSES)}"
    hp   = random.randint(6, 14)
    atk  = random.randint(2, 6)
    cost = 10 * atk + 5 * hp
    return {"name": name, "hp": hp, "atk": atk, "cost": cost}

class Town:
    def __init__(self, screen, clock, player, character_tray, pool_size: int = 4):
        self.screen = screen
        self.clock  = clock
        self.player = player
        self.tray   = character_tray

        self.pool_size = pool_size
        self.font_title = pygame.font.SysFont("microsoftyahei", 36)
        self.font_ui    = pygame.font.SysFont("microsoftyahei", 20)
        self.font_sm    = pygame.font.SysFont("microsoftyahei", 16)

        #layout
        w, h = self.screen.get_size()
        self.margin   = 20
        self.card_w   = 300
        self.card_h   = 90
        self.card_gap = 12
        self.left_col_x = self.margin
        self.cards_top  = 90

        #button cache gets rebuilt each frame
        self._buttons = []  # list of dicts: {"rect": Rect, "index": int}

        #initial recruits + sync tray
        self.recruits = [roll_recruit() for _ in range(self.pool_size)]
        self._sync_tray()

    def _sync_tray(self):
        heroes = self.player.roster.get()
        if hasattr(self.tray, "set_heroes"):
            self.tray.set_heroes(heroes)
        elif hasattr(self.tray, "set_characters"):
            self.tray.set_characters(heroes)

    def _draw_header(self):
        w, _ = self.screen.get_size()
        #title
        title = self.font_title.render("Town", True, (235, 235, 240))
        self.screen.blit(title, (self.margin, self.margin))

        #gold
        gold_txt = self.font_ui.render(f"🪙 Gold: {self.player.gold_balance()}", True, (240, 220, 120))
        gold_rect = gold_txt.get_rect()
        gold_rect.topright = (w - self.margin, self.margin + 6)
        self.screen.blit(gold_txt, gold_rect)

    def _draw_recruit_cards(self):
        self._buttons = []
        x = self.left_col_x
        y = self.cards_top

        for i, offer in enumerate(self.recruits):
            #card background
            card_rect = pygame.Rect(x, y, self.card_w, self.card_h)
            pygame.draw.rect(self.screen, (44, 48, 62), card_rect, border_radius=10)
            pygame.draw.rect(self.screen, (24, 26, 34), card_rect, width=2, border_radius=10)

            #text lines
            name = self.font_ui.render(offer["name"], True, (230, 230, 235))
            stats = self.font_sm.render(f"HP {offer['hp']}   |   ATK {offer['atk']}", True, (200, 205, 210))
            cost  = self.font_sm.render(f"Cost: {offer['cost']}", True, (220, 210, 120))

            self.screen.blit(name,  (x + 14, y + 10))
            self.screen.blit(stats, (x + 14, y + 40))
            self.screen.blit(cost,  (x + 14, y + 62))

            #recruit button on the right of the card
            btn_w, btn_h = 100, 36
            btn_rect = pygame.Rect(x + self.card_w - btn_w - 12, y + (self.card_h - btn_h)//2, btn_w, btn_h)

            affordable = self.player.can_recruit(offer["cost"])
            hovered = btn_rect.collidepoint(pygame.mouse.get_pos())

            btn_color = (78, 120, 86) if affordable else (70, 70, 70)
            if hovered and affordable:
                btn_color = (98, 150, 108)

            pygame.draw.rect(self.screen, btn_color, btn_rect, border_radius=8)
            pygame.draw.rect(self.screen, (25, 25, 30), btn_rect, width=2, border_radius=8)

            label = self.font_ui.render("Recruit", True, (255, 255, 255) if affordable else (180, 180, 180))
            label_rect = label.get_rect(center=btn_rect.center)
            self.screen.blit(label, label_rect)

            self._buttons.append({"rect": btn_rect, "index": i})

            y += self.card_h + self.card_gap

    def _draw_tray(self):
        if hasattr(self.tray, "draw"):
            self.tray.draw(self.screen)

    def run(self, events):
        self.screen.fill((30, 30, 40))
        self._draw_header()
        self._draw_recruit_cards()
        self._draw_tray()

        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                pos = e.pos
                for b in self._buttons:
                    if b["rect"].collidepoint(pos):
                        idx = b["index"]
                        offer = self.recruits[idx]
                        cost  = offer["cost"]
                        if self.player.recruit(
                            Character(name=offer["name"], hp=offer["hp"], atk=offer["atk"]),
                            cost
                        ):
                            self._sync_tray()
                            self.recruits[idx] = roll_recruit()
                        else:
                            pass

        return None
