from pico2d import *
import Define_File

# 초기화 코드
name = "Status_Board"

class Status_Board:
    font = None

    def __init__(self):
        self.life = 2
        self.image = load_image('resource\Status\StatusBoard.png')
        self.fadeoutfadein = load_image('resource\Background\FadeOutFadeIn.png')
        self.fadecount = 1550
        self.stagechangenow = False
        if Status_Board.font == None:
            Status_Board.font = load_font('digital-7.TTF', 45)

    def update(self):
        if self.stagechangenow == True:
            self.fadecount -= 15
            if self.fadecount < -650:
                self.stagechangenow = False

    def lifedown(self):
        self.life -= 1

    def lifeup(self):
        self.life += 1

    def fadestart(self):
        self.fadecount = 1550
        self.stagechangenow = True

    def draw(self):
        self.image.draw(Define_File.WINWIDTH - 54, Define_File.WINHEIGHT / 2)
        Status_Board.font.draw(975, 882, str(self.life), (255, 255, 255))
        if self.stagechangenow == True:
            self.fadeoutfadein.draw(Define_File.WINWIDTH / 2 - 54, self.fadecount)

    def __del__(self):
        del self.image
        del self.fadeoutfadein
