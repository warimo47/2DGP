from pico2d import *

# 초기화 코드
name = "MovingCounter"

class MovingCounter:
    font = None

    def __init__(self):
        self.totalmovecount = 0
        self.stagemovecount = 0
        if MovingCounter.font == None:
            MovingCounter.font = load_font('digital-7.TTF', 45)

    def draw(self):
        MovingCounter.font.draw(900, 800, "TOTAL", (255, 255, 255))
        MovingCounter.font.draw(910, 750, "MOVE", (255, 255, 255))
        MovingCounter.font.draw(950, 700, str(self.totalmovecount), (255, 255, 255))
        MovingCounter.font.draw(920, 650, "THIS", (255, 255, 255))
        MovingCounter.font.draw(900, 600, "STAGE", (255, 255, 255))
        MovingCounter.font.draw(910, 550, "MOVE", (255, 255, 255))
        MovingCounter.font.draw(950, 500, str(self.stagemovecount), (255, 255, 255))

    def increase_movecount(self):
        self.totalmovecount += 1
        self.stagemovecount += 1

    def decrease_movecount(self):
        self.totalmovecount -= 1
        self.stagemovecount -= 1

    def reset_stagemovecount(self):
        self.stagemovecount = 0