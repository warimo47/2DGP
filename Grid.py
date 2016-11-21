from pico2d import *
import Define_File

class Grid:
    W_Grid = None
    def __init__(self):
        if Grid.W_Grid == None:
            Grid.W_Grid = load_image('resource\Map\Grid_white.png')
        self.OnOff = False

    def toggle(self):
        if self.OnOff == True:
            self.OnOff = False
        else:
            self.OnOff = True

    def draw(self):
        if self.OnOff == True:
            Grid.W_Grid.draw((Define_File.WINWIDTH - 108) / 2, Define_File.WINHEIGHT / 2)