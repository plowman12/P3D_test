import pygame
from map import maze

window = pygame.display.set_mode((1000, 600))
W, H = window.get_size()

class camera:
     
    def __init__(self, Xpos, Ypos):
        self.Pos = {"X": Xpos, "Y": Ypos}
        self.Dir = {"X": -1, "Y": 0}
        self.Plane = {"X": 0, "Y": 0.16}
    
    def draw(self):
        for x in range(W):
            camX = x self.Dir["X"] / 0.12
            break