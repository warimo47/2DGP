from pico2d import *
import json
import Game_Framework
import Title_State
import Ranking_State
import Define_File
import Status_Board
import Grid
import Tile
import MovingCounter

# 초기화 코드
name = "PlayingState"

# 게임 오브젝트 클래스 정의
class SpaceShip:
    PIXEL_PER_METER = 1.0                                                   # 1.0 pixel 1.0 m
    MOVE_SPEED_MPS = 18.0                                                   # Meter / Sec
    MOVE_SPEED_PPS = (MOVE_SPEED_MPS * PIXEL_PER_METER)                     # Pixel / Sec

    TIME_PER_ACTION = 0.125
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    stagechange_sound = None
    move_sound = None
    stop_sound = None
    bounce_sound = None
    warp_sound = None

    states = { "STAY" : -1, "MOVE_TOP" : 0, "MOVE_RIGHT" : 1, "MOVE_BOTTOM": 2, "MOVE_LEFT" : 3 }

    def __init__(self):
        self.stopimage = load_image('resource\space_ship\space_ship0.png')
        self.imagespritesheet = load_image('resource\space_ship\space_ship.png')
        self.x, self.y = None, None
        self.state = SpaceShip.states["STAY"]
        self.next_stage = False
        self.frame = 0
        self.total_frames = 0.0
        self.bbOn = False
        if SpaceShip.stagechange_sound == None:
            SpaceShip.stagechange_sound = load_wav('resource\EffectSound\\NextStage.wav')
            SpaceShip.stagechange_sound.set_volume(100)
        if SpaceShip.move_sound == None:
            SpaceShip.move_sound = load_wav('resource\EffectSound\Move.wav')
            SpaceShip.move_sound.set_volume(50)
        if SpaceShip.stop_sound == None:
            SpaceShip.stop_sound = load_wav('resource\EffectSound\Stop.wav')
            SpaceShip.stop_sound.set_volume(100)
        if SpaceShip.bounce_sound == None:
            SpaceShip.bounce_sound = load_wav('resource\EffectSound\Bounce.wav')
            SpaceShip.bounce_sound.set_volume(100)
        if SpaceShip.warp_sound == None:
            SpaceShip.warp_sound = load_wav('resource\EffectSound\Warp.wav')
            SpaceShip.warp_sound.set_volume(100)

    def handle_event(self, event):
        global tiles

        if self.state == SpaceShip.states["STAY"] and event.type == SDL_KEYDOWN:
            if event.key == SDLK_n:
                stage.stagenumup()
                tiles = []
                stage.load_stage()
            elif event.key == SDLK_UP:
                self.state = SpaceShip.states["MOVE_TOP"]
                movingcounter.increase_movecount()
                for tile in tiles:
                    if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y - 1 and self.y - 1 < tile.y - 1:
                        if tile.type == 9:
                            self.state = SpaceShip.states["STAY"]
                            movingcounter.decrease_movecount()
                            break
                        elif tile.type == 13 and tile.division > 0 and tile.division < 551:
                            tile.explode()
                            self.state = SpaceShip.states["STAY"]
                            break
            elif event.key == SDLK_RIGHT:
                self.state = SpaceShip.states["MOVE_RIGHT"]
                movingcounter.increase_movecount()
                for tile in tiles:
                    if self.x + 1 > tile.x - 1 and self.x - 1 < tile.x - 1 and self.y + 1 > tile.y and self.y - 1 < tile.y:
                        if tile.type == 9:
                            self.state = SpaceShip.states["STAY"]
                            movingcounter.decrease_movecount()
                            break
                        elif tile.type == 13 and tile.division > 0 and tile.division < 551:
                            tile.explode()
                            self.state = SpaceShip.states["STAY"]
                            break
            elif event.key == SDLK_DOWN:
                self.state = SpaceShip.states["MOVE_BOTTOM"]
                movingcounter.increase_movecount()
                for tile in tiles:
                    if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y + 1 and self.y - 1 < tile.y + 1:
                        if tile.type == 9:
                            self.state = SpaceShip.states["STAY"]
                            movingcounter.decrease_movecount()
                            break
                        elif tile.type == 13 and tile.division > 0 and tile.division < 551:
                            tile.explode()
                            self.state = SpaceShip.states["STAY"]
                            break
            elif event.key == SDLK_LEFT:
                self.state = SpaceShip.states["MOVE_LEFT"]
                movingcounter.increase_movecount()
                for tile in tiles:
                    if self.x + 1 > tile.x + 1 and self.x - 1 < tile.x + 1 and self.y + 1 > tile.y and self.y - 1 < tile.y:
                        if tile.type == 9:
                            self.state = SpaceShip.states["STAY"]
                            movingcounter.decrease_movecount()
                            break
                        elif tile.type == 13 and tile.division > 0 and tile.division < 551:
                            tile.explode()
                            self.state = SpaceShip.states["STAY"]
                            break

    def update(self, frame_time):
        global shipdraw
        shipdraw = False
        distance = SpaceShip.MOVE_SPEED_PPS * frame_time
        self.total_frames += SpaceShip.FRAMES_PER_ACTION * SpaceShip.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 4
        if self.next_stage == True:
            shipdraw = True
        if self.state == SpaceShip.states["MOVE_TOP"]:
            self.y += distance
        elif self.state == SpaceShip.states["MOVE_RIGHT"]:
            self.x += distance
        elif self.state == SpaceShip.states["MOVE_BOTTOM"]:
            self.y -= distance
        elif self.state == SpaceShip.states["MOVE_LEFT"]:
            self.x -= distance

    def collision_check(self):
        global tiles

        if self.x < 0 or self.x > 24 or self.y < 0 or self.y > 24:
            self.state = SpaceShip.states["STAY"]
            status_board.lifedown()
            if status_board.life < 0:
                movingcounter.save_savedata()
                Game_Framework.change_state(Ranking_State)
            tiles = []
            stage.load_stage()
        else:
            for tile in tiles:
                if tile.type == 1:
                    if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                        if tile.division != 0:
                            self.state = SpaceShip.states["STAY"]
                            if status_board.stagechangenow == False:
                                status_board.fadestart()
                                SpaceShip.stagechange_sound.play()
                            if status_board.fadecount < 450:
                                movingcounter.check_bonuslife(stage.stagenum)
                                movingcounter.stagemovecount_to_zero()
                                stage.stagenumup()
                                tiles = []
                                stage.load_stage()
                        else:
                            self.ship_stop(tile.x, tile.y)
                elif tile.type == 2:
                    if self.x + 0.5 > tile.x and self.x - 0.5 < tile.x and self.y + 0.5 > tile.y and self.y - 0.5 < tile.y:
                        if tile.division == 1:
                            for othertile in tiles:
                                if othertile.type == 2 and othertile.division == 2:
                                    if self.state == SpaceShip.states["MOVE_TOP"]:
                                        self.x, self.y = othertile.x, othertile.y + 0.5
                                    elif self.state == SpaceShip.states["MOVE_RIGHT"]:
                                        self.x, self.y = othertile.x + 0.5, othertile.y
                                    elif self.state == SpaceShip.states["MOVE_BOTTOM"]:
                                        self.x, self.y = othertile.x, othertile.y - 0.5
                                    elif self.state == SpaceShip.states["MOVE_LEFT"]:
                                        self.x, self.y = othertile.x - 0.5, othertile.y
                                    SpaceShip.warp_sound.play()
                                    break
                        elif tile.division == 2:
                            for othertile in tiles:
                                if othertile.type == 2 and othertile.division == 1:
                                    if self.state == SpaceShip.states["MOVE_TOP"]:
                                        self.x, self.y = othertile.x, othertile.y + 0.5
                                    elif self.state == SpaceShip.states["MOVE_RIGHT"]:
                                        self.x, self.y = othertile.x + 0.5, othertile.y
                                    elif self.state == SpaceShip.states["MOVE_BOTTOM"]:
                                        self.x, self.y = othertile.x, othertile.y - 0.5
                                    elif self.state == SpaceShip.states["MOVE_LEFT"]:
                                        self.x, self.y = othertile.x - 0.5, othertile.y
                                    SpaceShip.warp_sound.play()
                                    break
                elif tile.type == 3:
                    if self.x + 0.5 > tile.x and self.x - 0.5 < tile.x and self.y + 0.5 > tile.y and self.y - 0.5 < tile.y:
                        if tile.division == 1:
                            for othertile in tiles:
                                if othertile.type == 3 and othertile.division == 2:
                                    if self.state == SpaceShip.states["MOVE_TOP"]:
                                        self.x, self.y = othertile.x, othertile.y + 0.5
                                    elif self.state == SpaceShip.states["MOVE_RIGHT"]:
                                        self.x, self.y = othertile.x + 0.5, othertile.y
                                    elif self.state == SpaceShip.states["MOVE_BOTTOM"]:
                                        self.x, self.y = othertile.x, othertile.y - 0.5
                                    elif self.state == SpaceShip.states["MOVE_LEFT"]:
                                        self.x, self.y = othertile.x - 0.5, othertile.y
                                    SpaceShip.warp_sound.play()
                                    break
                        elif tile.division == 2:
                            for othertile in tiles:
                                if othertile.type == 3 and othertile.division == 1:
                                    if self.state == SpaceShip.states["MOVE_TOP"]:
                                        self.x, self.y = othertile.x, othertile.y + 0.5
                                    elif self.state == SpaceShip.states["MOVE_RIGHT"]:
                                        self.x, self.y = othertile.x + 0.5, othertile.y
                                    elif self.state == SpaceShip.states["MOVE_BOTTOM"]:
                                        self.x, self.y = othertile.x, othertile.y - 0.5
                                    elif self.state == SpaceShip.states["MOVE_LEFT"]:
                                        self.x, self.y = othertile.x - 0.5, othertile.y
                                    SpaceShip.warp_sound.play()
                                    break
                elif tile.type == 4:
                    if self.x + 0.5 > tile.x and self.x - 0.5 < tile.x and self.y + 0.5 > tile.y and self.y - 0.5 < tile.y:
                        if tile.division == 1:
                            for othertile in tiles:
                                if othertile.type == 4 and othertile.division == 2:
                                    if self.state == SpaceShip.states["MOVE_TOP"]:
                                        self.x, self.y = othertile.x, othertile.y + 0.5
                                    elif self.state == SpaceShip.states["MOVE_RIGHT"]:
                                        self.x, self.y = othertile.x + 0.5, othertile.y
                                    elif self.state == SpaceShip.states["MOVE_BOTTOM"]:
                                        self.x, self.y = othertile.x, othertile.y - 0.5
                                    elif self.state == SpaceShip.states["MOVE_LEFT"]:
                                        self.x, self.y = othertile.x - 0.5, othertile.y
                                    SpaceShip.warp_sound.play()
                                    break
                        elif tile.division == 2:
                            for othertile in tiles:
                                if othertile.type == 4 and othertile.division == 1:
                                    if self.state == SpaceShip.states["MOVE_TOP"]:
                                        self.x, self.y = othertile.x, othertile.y + 0.5
                                    elif self.state == SpaceShip.states["MOVE_RIGHT"]:
                                        self.x, self.y = othertile.x + 0.5, othertile.y
                                    elif self.state == SpaceShip.states["MOVE_BOTTOM"]:
                                        self.x, self.y = othertile.x, othertile.y - 0.5
                                    elif self.state == SpaceShip.states["MOVE_LEFT"]:
                                        self.x, self.y = othertile.x - 0.5, othertile.y
                                    SpaceShip.warp_sound.play()
                                    break
                elif tile.type == 5:
                    if self.x + 0.5 > tile.x and self.x - 0.5 < tile.x and self.y + 0.5 > tile.y and self.y - 0.5 < tile.y:
                        if tile.division == 1:
                            for othertile in tiles:
                                if othertile.type == 5 and othertile.division == 2:
                                    if self.state == SpaceShip.states["MOVE_TOP"]:
                                        self.x, self.y = othertile.x, othertile.y + 0.5
                                    elif self.state == SpaceShip.states["MOVE_RIGHT"]:
                                        self.x, self.y = othertile.x + 0.5, othertile.y
                                    elif self.state == SpaceShip.states["MOVE_BOTTOM"]:
                                        self.x, self.y = othertile.x, othertile.y - 0.5
                                    elif self.state == SpaceShip.states["MOVE_LEFT"]:
                                        self.x, self.y = othertile.x - 0.5, othertile.y
                                    SpaceShip.warp_sound.play()
                                    break
                        elif tile.division == 2:
                            for othertile in tiles:
                                if othertile.type == 5 and othertile.division == 1:
                                    if self.state == SpaceShip.states["MOVE_TOP"]:
                                        self.x, self.y = othertile.x, othertile.y + 0.5
                                    elif self.state == SpaceShip.states["MOVE_RIGHT"]:
                                        self.x, self.y = othertile.x + 0.5, othertile.y
                                    elif self.state == SpaceShip.states["MOVE_BOTTOM"]:
                                        self.x, self.y = othertile.x, othertile.y - 0.5
                                    elif self.state == SpaceShip.states["MOVE_LEFT"]:
                                        self.x, self.y = othertile.x - 0.5, othertile.y
                                    SpaceShip.warp_sound.play()
                                    break
                elif tile.type == 6:
                    if self.x + 0.5 > tile.x and self.x - 0.5 < tile.x and self.y + 0.5 > tile.y and self.y - 0.5 < tile.y:
                        if tile.division == 1:
                            for othertile in tiles:
                                if othertile.type == 6 and othertile.division == 2:
                                    if self.state == SpaceShip.states["MOVE_TOP"]:
                                        self.x, self.y = othertile.x, othertile.y + 0.5
                                    elif self.state == SpaceShip.states["MOVE_RIGHT"]:
                                        self.x, self.y = othertile.x + 0.5, othertile.y
                                    elif self.state == SpaceShip.states["MOVE_BOTTOM"]:
                                        self.x, self.y = othertile.x, othertile.y - 0.5
                                    elif self.state == SpaceShip.states["MOVE_LEFT"]:
                                        self.x, self.y = othertile.x - 0.5, othertile.y
                                    SpaceShip.warp_sound.play()
                                    break
                        elif tile.division == 2:
                            for othertile in tiles:
                                if othertile.type == 6 and othertile.division == 1:
                                    if self.state == SpaceShip.states["MOVE_TOP"]:
                                        self.x, self.y = othertile.x, othertile.y + 0.5
                                    elif self.state == SpaceShip.states["MOVE_RIGHT"]:
                                        self.x, self.y = othertile.x + 0.5, othertile.y
                                    elif self.state == SpaceShip.states["MOVE_BOTTOM"]:
                                        self.x, self.y = othertile.x, othertile.y - 0.5
                                    elif self.state == SpaceShip.states["MOVE_LEFT"]:
                                        self.x, self.y = othertile.x - 0.5, othertile.y
                                    SpaceShip.warp_sound.play()
                                    break
                elif tile.type == 7:
                    if self.x + 0.5 > tile.x and self.x - 0.5 < tile.x and self.y + 0.5 > tile.y and self.y - 0.5 < tile.y:
                        if tile.division == 1:
                            for othertile in tiles:
                                if othertile.type == 7 and othertile.division == 2:
                                    if self.state == SpaceShip.states["MOVE_TOP"]:
                                        self.x, self.y = othertile.x, othertile.y + 0.5
                                    elif self.state == SpaceShip.states["MOVE_RIGHT"]:
                                        self.x, self.y = othertile.x + 0.5, othertile.y
                                    elif self.state == SpaceShip.states["MOVE_BOTTOM"]:
                                        self.x, self.y = othertile.x, othertile.y - 0.5
                                    elif self.state == SpaceShip.states["MOVE_LEFT"]:
                                        self.x, self.y = othertile.x - 0.5, othertile.y
                                    SpaceShip.warp_sound.play()
                                    break
                        elif tile.division == 2:
                            for othertile in tiles:
                                if othertile.type == 7 and othertile.division == 1:
                                    if self.state == SpaceShip.states["MOVE_TOP"]:
                                        self.x, self.y = othertile.x, othertile.y + 0.5
                                    elif self.state == SpaceShip.states["MOVE_RIGHT"]:
                                        self.x, self.y = othertile.x + 0.5, othertile.y
                                    elif self.state == SpaceShip.states["MOVE_BOTTOM"]:
                                        self.x, self.y = othertile.x, othertile.y - 0.5
                                    elif self.state == SpaceShip.states["MOVE_LEFT"]:
                                        self.x, self.y = othertile.x - 0.5, othertile.y
                                    SpaceShip.warp_sound.play()
                                    break
                elif tile.type == 8:
                    if self.x + 0.5 > tile.x and self.x - 0.5 < tile.x and self.y + 0.5 > tile.y and self.y - 0.5 < tile.y:
                        if tile.division == 1:
                            for othertile in tiles:
                                if othertile.type == 8 and othertile.division == 2:
                                    if self.state == SpaceShip.states["MOVE_TOP"]:
                                        self.x, self.y = othertile.x, othertile.y + 0.5
                                    elif self.state == SpaceShip.states["MOVE_RIGHT"]:
                                        self.x, self.y = othertile.x + 0.5, othertile.y
                                    elif self.state == SpaceShip.states["MOVE_BOTTOM"]:
                                        self.x, self.y = othertile.x, othertile.y - 0.5
                                    elif self.state == SpaceShip.states["MOVE_LEFT"]:
                                        self.x, self.y = othertile.x - 0.5, othertile.y
                                    SpaceShip.warp_sound.play()
                                    break
                        elif tile.division == 2:
                            for othertile in tiles:
                                if othertile.type == 8 and othertile.division == 1:
                                    if self.state == SpaceShip.states["MOVE_TOP"]:
                                        self.x, self.y = othertile.x, othertile.y + 0.5
                                    elif self.state == SpaceShip.states["MOVE_RIGHT"]:
                                        self.x, self.y = othertile.x + 0.5, othertile.y
                                    elif self.state == SpaceShip.states["MOVE_BOTTOM"]:
                                        self.x, self.y = othertile.x, othertile.y - 0.5
                                    elif self.state == SpaceShip.states["MOVE_LEFT"]:
                                        self.x, self.y = othertile.x - 0.5, othertile.y
                                    SpaceShip.warp_sound.play()
                                    break
                elif tile.type == 9:
                    if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                        self.ship_stop(tile.x, tile.y)
                elif tile.type == 10:
                    if tile.division == 1:
                        if self.state == SpaceShip.states["MOVE_TOP"]:
                            if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                                self.ship_stop(tile.x, tile.y)
                        elif self.state == SpaceShip.states["MOVE_RIGHT"]:
                            if self.x + 1 > tile.x + 0.5 and self.x - 1 < tile.x + 0.5 and self.y + 1 > tile.y and self.y - 1 < tile.y:
                                self.state = SpaceShip.states["MOVE_TOP"]
                                self.x = tile.x
                                self.y = tile.y + 1
                                SpaceShip.bounce_sound.play()
                        elif self.state == SpaceShip.states["MOVE_BOTTOM"]:
                            if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y - 0.5 and self.y - 1 < tile.y - 0.5:
                                self.state = SpaceShip.states["MOVE_LEFT"]
                                self.x = tile.x - 1
                                self.y = tile.y
                                SpaceShip.bounce_sound.play()
                        elif self.state == SpaceShip.states["MOVE_LEFT"]:
                            if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                                self.ship_stop(tile.x, tile.y)
                    elif tile.division == 2:
                        if self.state == SpaceShip.states["MOVE_TOP"]:
                            if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                                self.ship_stop(tile.x, tile.y)
                        elif self.state == SpaceShip.states["MOVE_RIGHT"]:
                            if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                                self.ship_stop(tile.x, tile.y)
                        elif self.state == SpaceShip.states["MOVE_BOTTOM"]:
                            if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y - 0.5 and self.y - 1 < tile.y - 0.5:
                                self.state = SpaceShip.states["MOVE_RIGHT"]
                                self.x = tile.x + 1
                                self.y = tile.y
                                SpaceShip.bounce_sound.play()
                        elif self.state == SpaceShip.states["MOVE_LEFT"]:
                            if self.x + 1 > tile.x - 0.5 and self.x - 1 < tile.x - 0.5 and self.y + 1 > tile.y and self.y - 1 < tile.y:
                                self.state = SpaceShip.states["MOVE_TOP"]
                                self.x = tile.x
                                self.y = tile.y + 1
                                SpaceShip.bounce_sound.play()
                    elif tile.division == 3:
                        if self.state == SpaceShip.states["MOVE_TOP"]:
                            if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y + 0.5 and self.y - 1 < tile.y + 0.5:
                                self.state = SpaceShip.states["MOVE_RIGHT"]
                                self.x = tile.x + 1
                                self.y = tile.y
                                SpaceShip.bounce_sound.play()
                        elif self.state == SpaceShip.states["MOVE_RIGHT"]:
                            if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                                self.ship_stop(tile.x, tile.y)
                        elif self.state == SpaceShip.states["MOVE_BOTTOM"]:
                            if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                                self.ship_stop(tile.x, tile.y)
                        elif self.state == SpaceShip.states["MOVE_LEFT"]:
                            if self.x + 1 > tile.x - 0.5 and self.x - 1 < tile.x - 0.5 and self.y + 1 > tile.y and self.y - 1 < tile.y:
                                self.state = SpaceShip.states["MOVE_BOTTOM"]
                                self.x = tile.x
                                self.y = tile.y - 1
                                SpaceShip.bounce_sound.play()
                    elif tile.division == 4:
                        if self.state == SpaceShip.states["MOVE_TOP"]:
                            if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y + 0.5 and self.y - 1 < tile.y + 0.5:
                                self.state = SpaceShip.states["MOVE_LEFT"]
                                self.x = tile.x - 1
                                self.y = tile.y
                                SpaceShip.bounce_sound.play()
                        elif self.state == SpaceShip.states["MOVE_RIGHT"]:
                            if self.x + 1 > tile.x + 0.5 and self.x - 1 < tile.x + 0.5 and self.y + 1 > tile.y and self.y - 1 < tile.y:
                                self.state = SpaceShip.states["MOVE_BOTTOM"]
                                self.x = tile.x
                                self.y = tile.y - 1
                                SpaceShip.bounce_sound.play()
                        elif self.state == SpaceShip.states["MOVE_BOTTOM"]:
                            if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                                self.ship_stop(tile.x, tile.y)
                        elif self.state == SpaceShip.states["MOVE_LEFT"]:
                            if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                                self.ship_stop(tile.x, tile.y)
                elif tile.type == 11:
                    if tile.division == 0:
                        if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y + 1 and self.y - 1 < tile.y + 1:
                            self.ship_stop(tile.x, tile.y + 1)
                        elif self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y - 1 and self.y - 1 < tile.y - 1:
                            self.ship_stop(tile.x, tile.y - 1)
                        elif self.x + 1 > tile.x + 1 and self.x - 1 < tile.x + 1 and self.y + 1 > tile.y and self.y - 1 < tile.y:
                            if self.state == SpaceShip.states["MOVE_RIGHT"]:
                                tile.division = 1
                                self.x = tile.x + 1
                        elif self.x + 1 > tile.x - 1 and self.x - 1 < tile.x - 1 and self.y + 1 > tile.y and self.y - 1 < tile.y:
                            if self.state == SpaceShip.states["MOVE_LEFT"]:
                                tile.division = 1
                                self.x = tile.x - 1
                    elif tile.division == 1:
                        if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                            self.ship_stop(tile.x, tile.y)
                elif tile.type == 12:
                    if tile.division == 0:
                        if self.x + 1 > tile.x + 1 and self.x - 1 < tile.x + 1 and self.y + 1 > tile.y and self.y - 1 < tile.y:
                            self.ship_stop(tile.x + 1, tile.y)
                        elif self.x + 1 > tile.x - 1 and self.x - 1 < tile.x - 1 and self.y + 1 > tile.y and self.y - 1 < tile.y:
                            self.ship_stop(tile.x - 1, tile.y)
                        elif self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y + 1 and self.y - 1 < tile.y + 1:
                            if self.state == SpaceShip.states["MOVE_TOP"]:
                                tile.division = 1
                                self.y = tile.y + 1
                        elif self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y - 1 and self.y - 1 < tile.y - 1:
                            if self.state == SpaceShip.states["MOVE_BOTTOM"]:
                                tile.division = 1
                                self.y = tile.y - 1
                    elif tile.division == 1:
                        if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                            self.ship_stop(tile.x, tile.y)
                elif tile.type == 13 and tile.division < 551:
                    if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                        if tile.division == 0:
                            tile.division += 50
                        self.ship_stop(tile.x, tile.y)
                elif tile.type == 14:
                    if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                        if self.state == SpaceShip.states["MOVE_TOP"] and tile.division % 10 == 0:
                            tile.division += 1
                        elif self.state == SpaceShip.states["MOVE_RIGHT"] and tile.division % 100 // 10 == 0:
                            tile.division += 10
                        elif self.state == SpaceShip.states["MOVE_BOTTOM"] and tile.division % 1000 // 100 == 0:
                            tile.division += 100
                        elif self.state == SpaceShip.states["MOVE_LEFT"] and tile.division // 1000 == 0:
                            tile.division += 1000
                        self.ship_stop(tile.x, tile.y)

    def ship_stop(self, tilex, tiley):
        if self.state == SpaceShip.states["MOVE_TOP"]:
            self.y = tiley - 1
        elif self.state == SpaceShip.states["MOVE_RIGHT"]:
            self.x = tilex - 1
        elif self.state == SpaceShip.states["MOVE_BOTTOM"]:
            self.y = tiley + 1
        elif self.state == SpaceShip.states["MOVE_LEFT"]:
            self.x = tilex + 1
        self.state = SpaceShip.states["STAY"]
        SpaceShip.stop_sound.play()

    def ship_stay(self):
        self.state = SpaceShip.states["STAY"]

    def draw(self):
        if self.state == SpaceShip.states["STAY"]:
            self.stopimage.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
        else:
            self.imagespritesheet.clip_draw(self.frame * 70, self.state * 70, 70, 70, (self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)

    def draw_bb(self):
        if self.bbOn == True:
            draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x * 36, self.y * 36, (self.x + 1) * 36, (self.y + 1) * 36

    def bbtoggle(self):
        if self.bbOn == True:
            self.bbOn = False
        else:
            self.bbOn = True

    def __del__(self):
        del self.imagespritesheet
        del self.stopimage

class Stage:
    font = None

    def __init__(self):
        self.stagenum = 1
        self.image = load_image('resource\Map\stage1.png')
        if Stage.font == None:
            Stage.font = load_font('digital-7.TTF', 45)
        self.bgm = load_music('NeverEnding_BGM.ogg')
        self.bgm.set_volume(300)
        self.bgm.repeat_play()

    def stagenumup(self):
        self.stagenum += 1

    def load_stage(self):
        self.filename = 'Stage\Stage' + str(self.stagenum) + '.txt'
        self.stage_data_file = open(self.filename, 'r')
        self.stage_data = json.load(self.stage_data_file)
        self.stage_data_file.close()
        for number in self.stage_data:
            if self.stage_data[number]['Tile_Type'] == 0:
                spaceship.x, spaceship.y = self.stage_data[number]['x'], self.stage_data[number]['y']
            else:
                NewTile = Tile.Tile(self.stage_data[number]['Tile_Type'], self.stage_data[number]['Division'],
                                    self.stage_data[number]['x'], self.stage_data[number]['y'])
                tiles.append(NewTile)
        self.image = load_image('resource\Map\stage' + str(self.stagenum) + '.png')

    def draw(self):
        self.image.draw((Define_File.WINWIDTH - 108) / 2, Define_File.WINHEIGHT / 2)
        Stage.font.draw(18, 882, "Stage " + str(self.stagenum), (255, 255, 255))

    def __del__(self):
        del self.bgm
        del self.image

# 키보드, 마우스 이벤트
def handle_events():
    global tiles

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            movingcounter.save_savedata()
            Game_Framework.running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                movingcounter.save_savedata()
                Game_Framework.running = False
            elif event.key == SDLK_g:
                grid.toggle()
            elif event.key == SDLK_b:
                spaceship.bbtoggle()
                tiles[0].bbtoggle()
            elif event.key == SDLK_SPACE:
                spaceship.ship_stay()
                movingcounter.reset_stagemovecount()
                status_board.lifedown()
                if status_board.life < 0:
                    movingcounter.save_savedata()
                    Game_Framework.change_state(Ranking_State)
                tiles.clear()
                stage.load_stage()
            else:
                spaceship.handle_event(event)

def get_frame_time():
    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time

def enter():
    global background, status_board, grid, spaceship, stage, tiles, shipdraw, current_time, movingcounter

    current_time = get_time()

    status_board = Status_Board.Status_Board()
    grid = Grid.Grid()
    spaceship = SpaceShip()
    stage = Stage()
    movingcounter = MovingCounter.MovingCounter()
    tiles = []
    stage.load_stage()
    shipdraw = False

def exit():
    pass

def pause():
    pass

def resume():
    pass

def update():
    global tiles, shipdraw, stage, tiles, status_board

    frame_time = get_frame_time()
    spaceship.update(frame_time)
    spaceship.collision_check()
    status_board.update()

    Tile.Tile.gate_on = True
    for tile in tiles:
        tile.update()
    if Tile.Tile.gate_on == True:
        for tile in tiles:
            if tile.type == 1 and tile.division == 0:
                tile.gate_turn_on()

def draw():
    clear_canvas()

    stage.draw()
    grid.draw()

    for tile in tiles:
        tile.draw()
        tile.draw_bb()

    spaceship.draw()
    spaceship.draw_bb()
    status_board.draw()
    movingcounter.draw()

    update_canvas()
