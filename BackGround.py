from pico2d import *
import Define_File

class BackGround:
    def __init__(self):
        self.image = load_image('resource\Map\stage1.png')
        self.StageNum = 1
    def draw(self):
        self.image.draw(Define_File.WINWIDTH / 2, Define_File.WINHEIGHT / 2)