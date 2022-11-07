from pico2d import *

class Grass:
    def __init__(self, Gy):
        self.image = load_image('grass.png')
        self.y = Gy

    def draw(self):
        self.image.draw(400, self.y)

    def update(self):
        pass
