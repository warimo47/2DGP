from pico2d import *
import Define_File

class Bomb:
    image = None
    def __init__(self):
        if Bomb.image == None:
            Bomb.image = load_image('resource\Tiles\Bomb.png')
        self.x, self.y = -1, -1
    def draw(self):
        Bomb.image.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)