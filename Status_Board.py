from pico2d import *
import Define_File

class Status_Board:
    def __init__(self):
        self.life = 2
        self.stagenum = 1
        self.image = load_image('resource\Status\StatusBoard.png')
        self.number0 = load_image('resource\Status\\Number0.png')
        self.number1 = load_image('resource\Status\\Number1.png')
        self.number2 = load_image('resource\Status\\Number2.png')
        self.number3 = load_image('resource\Status\\Number3.png')
        self.number4 = load_image('resource\Status\\Number4.png')
        self.number5 = load_image('resource\Status\\Number5.png')
        self.number6 = load_image('resource\Status\\Number6.png')
        self.number7 = load_image('resource\Status\\Number7.png')
        self.number8 = load_image('resource\Status\\Number8.png')
        self.number9 = load_image('resource\Status\\Number9.png')
        self.numbers = [self.number0, self.number1, self.number2, self.number3, self.number4,
                        self.number5, self.number6, self.number7, self.number8, self.number9]

    def lifedown(self):
        self.life -= 1

    def draw(self):
        self.image.draw(Define_File.WINWIDTH - 54, Define_File.WINHEIGHT / 2)
        if self.life // 10 != 0:
            self.numbers[self.life // 10].draw(954, 882)
        self.numbers[self.life % 10].draw(990, 882)