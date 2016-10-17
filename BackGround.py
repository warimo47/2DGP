from pico2d import *
import Define_File

class BackGround:
    image = None
    StageNum = 1
    def __init__(self):
        if BackGround.image == None:
            BackGround.image = load_image('resource\Map\stage1.png')
        self.StageNum = 1
    def draw(self):
        BackGround.image.draw((Define_File.WINWIDTH - 108) / 2, Define_File.WINHEIGHT / 2)