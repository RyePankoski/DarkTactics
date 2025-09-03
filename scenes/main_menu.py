import pygame

class MainMenu:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.title_font = pygame.font.SysFont('microsoftyahei', 48)
        self.ui_font = pygame.font.SysFont('microsoftyahei', 24)

        #button
        w, h = self.screen.get_size()
        bw, bh = 200, 56
        self.button_rect = pygame.Rect((w - bw) // 2, (h // 2) + 20, bw, bh)

    def run(self, events):
        self.screen.fill((30, 30, 40))

        #title
        title_surf = self.title_font.render('Dark Tactics', True, (220, 220, 220))
        title_rect = title_surf.get_rect(center=(self.screen.get_rect().centerx, 120))
        self.screen.blit(title_surf, title_rect)

        #button
        mouse_pos = pygame.mouse.get_pos()
        hovered = self.button_rect.collidepoint(mouse_pos)
        color = (90, 90, 170) if hovered else (60, 60, 130)
        pygame.draw.rect(self.screen, color, self.button_rect, border_radius=10)
        pygame.draw.rect(self.screen, (25, 25, 50), self.button_rect, width=2, border_radius=10)

        #button label
        label = self.ui_font.render('Start Game', True, (255, 255, 255))
        label_rect = label.get_rect(center=self.button_rect.center)
        self.screen.blit(label, label_rect)

        #click -> go to town
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1 and hovered:
                return 'town'

        #stay on menu if nothing happened
        return None
