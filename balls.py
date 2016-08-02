import pygame
import settings


class Balls:
    def __init__(self, b0, b1, b2, b3):
        self.bs = b0, b1, b2, b3

    # lo stato e' del tipo [0,3,1,2]
    def change_state(self, info):
        r = range(4)
        s = []
        self.bs[0].state = r[info / 6]
        s.append(r[info / 6])
        r.remove(r[info / 6])
        info %= 6
        self.bs[1].state = r[info / 2]
        s.append(r[info / 2])
        r.remove(r[info / 2])
        info %= 2
        self.bs[2].state = r[info]
        s.append(r[info])
        r.remove(r[info])
        self.bs[3].state = r[0]
        s.append(r[0])
        self.state = s

    def get_state(self):
        return (self.state)


class Ball:
    # forse non e' bellissimo che i colori siano cablati dentro con riferimento a settings. Metterli in costruttore?
    def __init__(self, surface):
        self._w, self._h = surface.get_size()
        self.state = 0
        self.surface = surface

    def render(self):
        r, g, b = 0, 0, 0
        if self.state == 0:
            r, g, b = settings.Hours[0]['color']
        elif self.state == 1:
            r, g, b = settings.Hours[1]['color']
        elif self.state == 2:
            r, g, b = settings.Hours[2]['color']
        else:
            r, g, b = settings.Hours[3]['color']
        pygame.draw.circle(self.surface, pygame.Color(r, g, b),
                           (self._w / 2, self._h / 2), self._w / 2)
