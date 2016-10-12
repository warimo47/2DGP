from pico2d import *
import Define_File

class Status_Board:
    def __init__(self):
        self.image = load_image('resource\Background\Blackbackground.png')
    def draw(self):
        self.image.draw(Define_File.WINWIDTH - 54, Define_File.WINHEIGHT / 2)