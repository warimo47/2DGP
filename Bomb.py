from pico2d import *
import Define_File

class Bomb:
    def __init__(self):
        self.image = load_image('resource\Tiles\\bomb.png')
        self.x, self.y = -1, -1
    def draw(self):
        self.image.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)