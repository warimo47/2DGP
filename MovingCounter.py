from pico2d import *
import json
import Game_Framework
import Playing_State
import Title_State

# 초기화 코드
name = "MovingCounter"

class MovingCounter:
    font_45 = None
    font_30 = None

    def __init__(self):
        self.totalmovecount = 0
        self.stagemovecount = 0
        if MovingCounter.font_45 == None:
            MovingCounter.font_45 = load_font('digital-7.TTF', 45)
        if MovingCounter.font_30 == None:
            MovingCounter.font_30 = load_font('digital-7.TTF', 30)
        self.setting_data_file = open('SettingData.txt', 'r')
        self.setting_data = json.load(self.setting_data_file)
        self.setting_data_file.close()
        self.playernumber = self.setting_data["PlayerNumber"]

    def save_savedata(self):
        global Playing_State

        self.ranking_data_file = open('RankingDataFile.txt', 'r')
        self.ranking_data = json.load(self.ranking_data_file)
        self.ranking_data_file.close()

        self.ranking_data.append({'PlayerNumber' : self.playernumber, 'StageNumber' : Playing_State.stage.stagenum, 'Movecount' : self.totalmovecount})

        self.ranking_data_file = open('RankingDataFile.txt', 'w')
        json.dump(self.ranking_data, self.ranking_data_file)
        self.ranking_data_file.close()

        self.playernumber += 1
        self.setting_data["PlayerNumber"] = self.playernumber

        self.setting_data_file = open('SettingData.txt', 'w')
        json.dump(self.setting_data, self.setting_data_file)
        self.setting_data_file.close()

    def draw(self):
        MovingCounter.font_45.draw(900, 800, "TOTAL", (255, 255, 255))
        MovingCounter.font_45.draw(910, 750, "MOVE", (255, 255, 255))
        MovingCounter.font_45.draw(950, 700, str(self.totalmovecount), (255, 255, 255))
        MovingCounter.font_45.draw(920, 650, "THIS", (255, 255, 255))
        MovingCounter.font_45.draw(900, 600, "STAGE", (255, 255, 255))
        MovingCounter.font_45.draw(910, 550, "MOVE", (255, 255, 255))
        MovingCounter.font_45.draw(950, 500, str(self.stagemovecount), (255, 255, 255))
        MovingCounter.font_30.draw(910, 80, "PLAYER ", (255, 255, 255))
        if self.playernumber < 10:
            MovingCounter.font_30.draw(950, 40, str(self.playernumber), (255, 255, 255))
        elif self.playernumber < 100:
            MovingCounter.font_30.draw(940, 40, str(self.playernumber), (255, 255, 255))
        elif self.playernumber < 1000:
            MovingCounter.font_30.draw(930, 40, str(self.playernumber), (255, 255, 255))
        elif self.playernumber < 10000:
            MovingCounter.font_30.draw(920, 40, str(self.playernumber), (255, 255, 255))
        else:
            MovingCounter.font_30.draw(910, 40, str(self.playernumber), (255, 255, 255))

    def reset_stagemovecount(self):
        self.totalmovecount -= self.stagemovecount
        self.stagemovecount = 0

    def increase_movecount(self):
        self.totalmovecount += 1
        self.stagemovecount += 1

    def decrease_movecount(self):
        self.totalmovecount -= 1
        self.stagemovecount -= 1

    def stagemovecount_to_zero(self):
        self.stagemovecount = 0