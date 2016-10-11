from pico2d import *
import Define_File

class Grid:
    def __init__(self):
        self.image = load_image('resource\Map\grid_white.png')
        self.OnOff = False
    def draw(self):
        if self.OnOff == True:
            self.image.draw(Define_File.WINWIDTH / 2, Define_File.WINHEIGHT / 2)