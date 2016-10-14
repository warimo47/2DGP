from pico2d import *
import Define_File

class Grid:
    W_Grid = None
    B_Grid = None
    def __init__(self):
        if Grid.W_Grid == None:
            Grid.W_Grid = load_image('resource\Map\Grid_white.png')
        if Grid.B_Grid == None:
            Grid.B_Grid = load_image('resource\Map\Grid_black.png')
        self.OnOff = False
    def draw(self):
        if self.OnOff == True:
            Grid.W_Grid.draw((Define_File.WINWIDTH - 108) / 2, Define_File.WINHEIGHT / 2)
    def b_draw(self):
        if self.OnOff == True:
            Grid.B_Grid.draw((Define_File.WINWIDTH - 108) / 2, Define_File.WINHEIGHT / 2)