from pico2d import *
import Define_File

class Wall:
    image = None
    def __init__(self):
        if Wall.image == None:
            Wall.image = load_image('resource\Tiles\wall.png')
        self.x, self.y = -1, -1
    def draw(self):
        Wall.image.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)