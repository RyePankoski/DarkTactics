# components/character_tray.py
import pygame

class CharacterTray:
    def __init__(self, rect=None, title="Your Roster"):
        self.rect = pygame.Rect(0, 0, 360, 360) if rect is None else pygame.Rect(rect)
        self.title = title
        self._heroes = []
        self._scroll = 0
        self._item_h = 64
        self._pad = 12
        self._bar_h = 8

        #fonts
        self._font_title = pygame.font.SysFont("microsoftyahei", 22)
        self._font_item  = pygame.font.SysFont("microsoftyahei", 18)
        self._font_small = pygame.font.SysFont("microsoftyahei", 14)

        #colors
        self._bg      = (38, 40, 52)
        self._border  = (22, 24, 30)
        self._card    = (48, 51, 66)
        self._card_b  = (28, 30, 38)
        self._text    = (235, 235, 240)
        self._muted   = (190, 195, 205)
        self._hp_ok   = (90, 180, 110)
        self._hp_low  = (205, 100, 90)
        self._hp_mid  = (220, 180, 90)

    #api
    def set_heroes(self, heroes):
        self._heroes = list(heroes)
        self._clamp_scroll()

    def set_rect(self, rect):
        self.rect = pygame.Rect(rect)
        self._clamp_scroll()

    def handle_events(self, events):
        mouse_pos = pygame.mouse.get_pos()
        if not self.rect.collidepoint(mouse_pos):
            return
        for e in events:
            if e.type == pygame.MOUSEWHEEL:
                self._scroll -= e.y * (self._item_h // 2)
                self._clamp_scroll()

    def draw(self, surface):
        #background + border
        pygame.draw.rect(surface, self._bg, self.rect, border_radius=10)
        pygame.draw.rect(surface, self._border, self.rect, width=2, border_radius=10)

        #title
        title_s = self._font_title.render(self.title, True, self._text)
        surface.blit(title_s, (self.rect.x + self._pad, self.rect.y + self._pad))

        #viewport for list items
        list_top = self.rect.y + self._pad + title_s.get_height() + self._pad
        list_rect = pygame.Rect(self.rect.x + self._pad, list_top,
                                self.rect.w - 2*self._pad, self.rect.h - (list_top - self.rect.y) - self._pad)

        #set clip so items don’t draw outside tray
        prev_clip = surface.get_clip()
        surface.set_clip(list_rect)

        y = list_rect.y - self._scroll
        for c in self._heroes:
            card_rect = pygame.Rect(list_rect.x, y, list_rect.w, self._item_h - 8)
            #only draw visible rows
            if card_rect.bottom >= list_rect.top and card_rect.top <= list_rect.bottom:
                pygame.draw.rect(surface, self._card, card_rect, border_radius=8)
                pygame.draw.rect(surface, self._card_b, card_rect, width=2, border_radius=8)

                #name + stats
                name_s  = self._font_item.render(c.name, True, self._text)
                stats_s = self._font_small.render(f"HP {c.hp}/{c.hp_max}  |  ATK {c.atk}", True, self._muted)

                surface.blit(name_s,  (card_rect.x + 12, card_rect.y + 8))
                surface.blit(stats_s, (card_rect.x + 12, card_rect.y + 30))

                #HP bar
                bar_w = 140
                bar_x = card_rect.right - bar_w - 12
                bar_y = card_rect.y + 14
                pygame.draw.rect(surface, (25, 25, 30), (bar_x, bar_y, bar_w, self._bar_h), border_radius=4)

                ratio = 0 if c.hp_max <= 0 else max(0, min(1, c.hp / c.hp_max))
                if   ratio >= 0.67: color = self._hp_ok
                elif ratio >= 0.33: color = self._hp_mid
                else:               color = self._hp_low

                pygame.draw.rect(surface, color, (bar_x, bar_y, int(bar_w * ratio), self._bar_h), border_radius=4)

            y += self._item_h

        #restore clip
        surface.set_clip(prev_clip)

        #scrollbar indicator
        content_h = len(self._heroes) * self._item_h
        if content_h > list_rect.h:
            track = pygame.Rect(self.rect.right - 6, list_rect.y, 3, list_rect.h)
            pygame.draw.rect(surface, (70, 70, 80), track, border_radius=2)
            thumb_h = max(24, int(list_rect.h * (list_rect.h / content_h)))
            max_scroll = content_h - list_rect.h
            thumb_y = list_rect.y if max_scroll == 0 else int(list_rect.y + (self._scroll / max_scroll) * (list_rect.h - thumb_h))
            pygame.draw.rect(surface, (150, 150, 160), (self.rect.right - 6, thumb_y, 3, thumb_h), border_radius=2)

    #keep scroll within bounds
    def _clamp_scroll(self):
        content_h = len(self._heroes) * self._item_h
        view_h = self.rect.h - (self._pad + self._font_title.get_height() + 2*self._pad)
        view_h = max(0, view_h)
        max_scroll = max(0, content_h - view_h)
        self._scroll = max(0, min(self._scroll, max_scroll))
