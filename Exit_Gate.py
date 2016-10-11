from pico2d import *
import Define_File

class Exit_Gate:
    def __init__(self):
        self.image = load_image('resource\Tiles\exit_gate.png')
        self.x, self.y = 8, 11
    def draw(self):
        self.image.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)