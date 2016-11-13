from pico2d import *
import json
import Game_Framework
import Title_State
import Define_File
import Status_Board
import Grid
import Tile

# 초기화 코드
name = "PlayingState"

# 게임 오브젝트 클래스 정의
class SpaceShip:
    global tiles
    global exit_gate

    PIXEL_PER_METER = 1.0                                                   # 1.0 pixel 1.0 m
    MOVE_SPEED_MPS = 18.0                                                   # Meter / Sec
    MOVE_SPEED_PPS = (MOVE_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.125
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    def __init__(self):
        self.stop = load_image('resource\space_ship\space_ship0.png')
        self.image = load_image('resource\space_ship\space_ship.png')
        self.x, self.y = -1, -1
        self.direction = -1
        self.canmove = True
        self.next_stage = False
        self.frame = 0
        self.total_frames = 0.0
        self.bbOn = True

    def setxy(self, xx, yy):
        self.x, self.y = xx, yy

    def update(self, frame_time):
        global shipdraw
        shipdraw = False
        distance = SpaceShip.MOVE_SPEED_PPS * frame_time
        self.total_frames += SpaceShip.FRAMES_PER_ACTION * SpaceShip.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 4
        if self.next_stage == True:
            shipdraw = True
        if self.direction == 0:
            self.y += distance
        elif self.direction == 1:
            self.x += distance
        elif self.direction == 2:
            self.y -= distance
        elif self.direction == 3:
            self.x -= distance

    def collision_check(self):
        global tiles

        if self.x < 0 or self.x > 24 or self.y < 0 or self.y > 24:
            self.direction = -1
            status_board.life -= 1
            if status_board.life < 0:
                Game_Framework.change_state(Title_State)
            tiles = []
            stage.load_stage()
        else:
            for tile in tiles:
                if tile.type == 1:
                    if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                        if tile.division == 0:
                            self.direction = -1
                            status_board.stagenum += 1
                            Stage.StageNum += 1
                            tiles = []
                            stage.load_stage()
                        else:
                            self.ship_stop(tile.x, tile.y)
                elif tile.type == 2:
                    if self.x + 0.5 > tile.x and self.x - 0.5 < tile.x and self.y + 0.5 > tile.y and self.y - 0.5 < tile.y:
                        if tile.division == 1:
                            for othertile in tiles:
                                if othertile.type == 2 and othertile.division == 2:
                                    if self.direction == 0:
                                        self.x, self.y = othertile.x, othertile.y + 0.5
                                    elif self.direction == 1:
                                        self.x, self.y = othertile.x + 0.5, othertile.y
                                    elif self.direction == 2:
                                        self.x, self.y = othertile.x, othertile.y - 0.5
                                    elif self.direction == 3:
                                        self.x, self.y = othertile.x - 0.5, othertile.y
                        elif tile.division == 2:
                            for othertile in tiles:
                                if othertile.type == 2 and othertile.division == 1:
                                    if self.direction == 0:
                                        self.x, self.y = othertile.x, othertile.y + 0.5
                                    elif self.direction == 1:
                                        self.x, self.y = othertile.x + 0.5, othertile.y
                                    elif self.direction == 2:
                                        self.x, self.y = othertile.x, othertile.y - 0.5
                                    elif self.direction == 3:
                                        self.x, self.y = othertile.x - 0.5, othertile.y
                elif tile.type == 3:
                    if self.x + 0.5 > tile.x and self.x - 0.5 < tile.x and self.y + 0.5 > tile.y and self.y - 0.5 < tile.y:
                        if tile.division == 1:
                            for othertile in tiles:
                                if othertile.type == 3 and othertile.division == 2:
                                    if self.direction == 0:
                                        self.x, self.y = othertile.x, othertile.y + 0.5
                                    elif self.direction == 1:
                                        self.x, self.y = othertile.x + 0.5, othertile.y
                                    elif self.direction == 2:
                                        self.x, self.y = othertile.x, othertile.y - 0.5
                                    elif self.direction == 3:
                                        self.x, self.y = othertile.x - 0.5, othertile.y
                        elif tile.division == 2:
                            for othertile in tiles:
                                if othertile.type == 3 and othertile.division == 1:
                                    if self.direction == 0:
                                        self.x, self.y = othertile.x, othertile.y + 0.5
                                    elif self.direction == 1:
                                        self.x, self.y = othertile.x + 0.5, othertile.y
                                    elif self.direction == 2:
                                        self.x, self.y = othertile.x, othertile.y - 0.5
                                    elif self.direction == 3:
                                        self.x, self.y = othertile.x - 0.5, othertile.y
                elif tile.type == 4:
                    if self.x + 0.5 > tile.x and self.x - 0.5 < tile.x and self.y + 0.5 > tile.y and self.y - 0.5 < tile.y:
                        if tile.division == 1:
                            for othertile in tiles:
                                if othertile.type == 4 and othertile.division == 2:
                                    if self.direction == 0:
                                        self.x, self.y = othertile.x, othertile.y + 0.5
                                    elif self.direction == 1:
                                        self.x, self.y = othertile.x + 0.5, othertile.y
                                    elif self.direction == 2:
                                        self.x, self.y = othertile.x, othertile.y - 0.5
                                    elif self.direction == 3:
                                        self.x, self.y = othertile.x - 0.5, othertile.y
                        elif tile.division == 2:
                            for othertile in tiles:
                                if othertile.type == 4 and othertile.division == 1:
                                    if self.direction == 0:
                                        self.x, self.y = othertile.x, othertile.y + 0.5
                                    elif self.direction == 1:
                                        self.x, self.y = othertile.x + 0.5, othertile.y
                                    elif self.direction == 2:
                                        self.x, self.y = othertile.x, othertile.y - 0.5
                                    elif self.direction == 3:
                                        self.x, self.y = othertile.x - 0.5, othertile.y
                elif tile.type == 5:
                    if self.x + 0.5 > tile.x and self.x - 0.5 < tile.x and self.y + 0.5 > tile.y and self.y - 0.5 < tile.y:
                        if tile.division == 1:
                            for othertile in tiles:
                                if othertile.type == 5 and othertile.division == 2:
                                    if self.direction == 0:
                                        self.x, self.y = othertile.x, othertile.y + 0.5
                                    elif self.direction == 1:
                                        self.x, self.y = othertile.x + 0.5, othertile.y
                                    elif self.direction == 2:
                                        self.x, self.y = othertile.x, othertile.y - 0.5
                                    elif self.direction == 3:
                                        self.x, self.y = othertile.x - 0.5, othertile.y
                        elif tile.division == 2:
                            for othertile in tiles:
                                if othertile.type == 5 and othertile.division == 1:
                                    if self.direction == 0:
                                        self.x, self.y = othertile.x, othertile.y + 0.5
                                    elif self.direction == 1:
                                        self.x, self.y = othertile.x + 0.5, othertile.y
                                    elif self.direction == 2:
                                        self.x, self.y = othertile.x, othertile.y - 0.5
                                    elif self.direction == 3:
                                        self.x, self.y = othertile.x - 0.5, othertile.y
                elif tile.type == 6:
                    if self.x + 0.5 > tile.x and self.x - 0.5 < tile.x and self.y + 0.5 > tile.y and self.y - 0.5 < tile.y:
                        if tile.division == 1:
                            for othertile in tiles:
                                if othertile.type == 6 and othertile.division == 2:
                                    if self.direction == 0:
                                        self.x, self.y = othertile.x, othertile.y + 0.5
                                    elif self.direction == 1:
                                        self.x, self.y = othertile.x + 0.5, othertile.y
                                    elif self.direction == 2:
                                        self.x, self.y = othertile.x, othertile.y - 0.5
                                    elif self.direction == 3:
                                        self.x, self.y = othertile.x - 0.5, othertile.y
                        elif tile.division == 2:
                            for othertile in tiles:
                                if othertile.type == 6 and othertile.division == 1:
                                    if self.direction == 0:
                                        self.x, self.y = othertile.x, othertile.y + 0.5
                                    elif self.direction == 1:
                                        self.x, self.y = othertile.x + 0.5, othertile.y
                                    elif self.direction == 2:
                                        self.x, self.y = othertile.x, othertile.y - 0.5
                                    elif self.direction == 3:
                                        self.x, self.y = othertile.x - 0.5, othertile.y
                elif tile.type == 7:
                    if self.x + 0.5 > tile.x and self.x - 0.5 < tile.x and self.y + 0.5 > tile.y and self.y - 0.5 < tile.y:
                        if tile.division == 1:
                            for othertile in tiles:
                                if othertile.type == 7 and othertile.division == 2:
                                    if self.direction == 0:
                                        self.x, self.y = othertile.x, othertile.y + 0.5
                                    elif self.direction == 1:
                                        self.x, self.y = othertile.x + 0.5, othertile.y
                                    elif self.direction == 2:
                                        self.x, self.y = othertile.x, othertile.y - 0.5
                                    elif self.direction == 3:
                                        self.x, self.y = othertile.x - 0.5, othertile.y
                        elif tile.division == 2:
                            for othertile in tiles:
                                if othertile.type == 7 and othertile.division == 1:
                                    if self.direction == 0:
                                        self.x, self.y = othertile.x, othertile.y + 0.5
                                    elif self.direction == 1:
                                        self.x, self.y = othertile.x + 0.5, othertile.y
                                    elif self.direction == 2:
                                        self.x, self.y = othertile.x, othertile.y - 0.5
                                    elif self.direction == 3:
                                        self.x, self.y = othertile.x - 0.5, othertile.y
                elif tile.type == 8:
                    if self.x + 0.5 > tile.x and self.x - 0.5 < tile.x and self.y + 0.5 > tile.y and self.y - 0.5 < tile.y:
                        if tile.division == 1:
                            for othertile in tiles:
                                if othertile.type == 8 and othertile.division == 2:
                                    if self.direction == 0:
                                        self.x, self.y = othertile.x, othertile.y + 0.5
                                    elif self.direction == 1:
                                        self.x, self.y = othertile.x + 0.5, othertile.y
                                    elif self.direction == 2:
                                        self.x, self.y = othertile.x, othertile.y - 0.5
                                    elif self.direction == 3:
                                        self.x, self.y = othertile.x - 0.5, othertile.y
                        elif tile.division == 2:
                            for othertile in tiles:
                                if othertile.type == 8 and othertile.division == 1:
                                    if self.direction == 0:
                                        self.x, self.y = othertile.x, othertile.y + 0.5
                                    elif self.direction == 1:
                                        self.x, self.y = othertile.x + 0.5, othertile.y
                                    elif self.direction == 2:
                                        self.x, self.y = othertile.x, othertile.y - 0.5
                                    elif self.direction == 3:
                                        self.x, self.y = othertile.x - 0.5, othertile.y
                elif tile.type == 9:
                    if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                        self.ship_stop(tile.x, tile.y)
                elif tile.type == 10:
                    if tile.division == 1:
                        if self.direction == 0:
                            if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                                self.ship_stop(tile.x, tile.y)
                        elif self.direction == 1:
                            if self.x + 1 > tile.x + 0.5 and self.x - 1 < tile.x + 0.5 and self.y + 1 > tile.y and self.y - 1 < tile.y:
                                self.direction = 0
                                self.x = tile.x
                                self.y = tile.y + 1
                        elif self.direction == 2:
                            if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y - 0.5 and self.y - 1 < tile.y - 0.5:
                                self.direction = 3
                                self.x = tile.x - 1
                                self.y = tile.y
                        elif self.direction == 3:
                            if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                                self.ship_stop(tile.x, tile.y)
                    elif tile.division == 2:
                        if self.direction == 0:
                            if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                                self.ship_stop(tile.x, tile.y)
                        elif self.direction == 1:
                            if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                                self.ship_stop(tile.x, tile.y)
                        elif self.direction == 2:
                            if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y - 0.5 and self.y - 1 < tile.y - 0.5:
                                self.direction = 1
                                self.x = tile.x + 1
                                self.y = tile.y
                        elif self.direction == 3:
                            if self.x + 1 > tile.x - 0.5 and self.x - 1 < tile.x - 0.5 and self.y + 1 > tile.y and self.y - 1 < tile.y:
                                self.direction = 0
                                self.x = tile.x
                                self.y = tile.y + 1
                    elif tile.division == 3:
                        if self.direction == 0:
                            if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y + 0.5 and self.y - 1 < tile.y + 0.5:
                                self.direction = 1
                                self.x = tile.x + 1
                                self.y = tile.y
                        elif self.direction == 1:
                            if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                                self.ship_stop(tile.x, tile.y)
                        elif self.direction == 2:
                            if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                                self.ship_stop(tile.x, tile.y)
                        elif self.direction == 3:
                            if self.x + 1 > tile.x - 0.5 and self.x - 1 < tile.x - 0.5 and self.y + 1 > tile.y and self.y - 1 < tile.y:
                                self.direction = 2
                                self.x = tile.x
                                self.y = tile.y - 1
                    elif tile.division == 4:
                        if self.direction == 0:
                            if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y + 0.5 and self.y - 1 < tile.y + 0.5:
                                self.direction = 3
                                self.x = tile.x - 1
                                self.y = tile.y
                        elif self.direction == 1:
                            if self.x + 1 > tile.x + 0.5 and self.x - 1 < tile.x + 0.5 and self.y + 1 > tile.y and self.y - 1 < tile.y:
                                self.direction = 2
                                self.x = tile.x
                                self.y = tile.y - 1
                        elif self.direction == 2:
                            if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                                self.ship_stop(tile.x, tile.y)
                        elif self.direction == 3:
                            if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                                self.ship_stop(tile.x, tile.y)
                elif tile.type == 11:
                    if tile.division == 0:
                        if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y + 1 and self.y - 1 < tile.y + 1:
                            self.ship_stop(tile.x, tile.y + 1)
                        elif self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y - 1 and self.y - 1 < tile.y - 1:
                            self.ship_stop(tile.x, tile.y - 1)
                        elif self.x + 1 > tile.x + 1 and self.x - 1 < tile.x + 1 and self.y + 1 > tile.y and self.y - 1 < tile.y:
                            if self.direction == 1:
                                tile.division = 1
                                self.x = tile.x + 1
                        elif self.x + 1 > tile.x - 1 and self.x - 1 < tile.x - 1 and self.y + 1 > tile.y and self.y - 1 < tile.y:
                            if self.direction == 3:
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
                            if self.direction == 0:
                                tile.division = 1
                                self.y = tile.y + 1
                        elif self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y - 1 and self.y - 1 < tile.y - 1:
                            if self.direction == 2:
                                tile.division = 1
                                self.y = tile.y - 1
                    elif tile.division == 1:
                        if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                            self.ship_stop(tile.x, tile.y)
                elif tile.type == 13 and tile.division < 361:
                    if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                        if tile.division == 0:
                            tile.division += 36
                        self.ship_stop(tile.x, tile.y)
                elif tile.type == 14:
                    if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                        if self.direction == 0 and tile.division % 10 == 0:
                            tile.division += 1
                        elif self.direction == 1 and tile.division % 100 // 10 == 0:
                            tile.division += 10
                        elif self.direction == 2 and tile.division % 1000 // 100 == 0:
                            tile.division += 100
                        elif self.direction == 3 and tile.division // 1000 == 0:
                            tile.division += 1000
                        self.ship_stop(tile.x, tile.y)
                elif tile.type == 15:
                    if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                        self.ship_stop(tile.x, tile.y)

    def ship_stop(self, tilex, tiley):
        if self.direction == 0:
            self.y = tiley - 1
        elif self.direction == 1:
            self.x = tilex - 1
        elif self.direction == 2:
            self.y = tiley + 1
        elif self.direction == 3:
            self.x = tilex + 1
        self.canmove = True
        self.direction = -1

    def draw(self):
        if self.direction == -1:
            self.stop.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
        else:
            self.image.clip_draw(self.frame * 70, self.direction * 70, 70, 70, (self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)

    def draw_bb(self):
        if self.bbOn == True:
            draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x * 36, self.y * 36, (self.x + 1) * 36, (self.y + 1) * 36

class Stage:
    global tiles
    global spaceship

    def __init__(self):
        Stage.StageNum = 1
        Stage.image = load_image('resource\Map\stage1.png')

    def load_stage(self):
        self.filename = 'Stage\Stage' + str(Stage.StageNum) + '.txt'
        self.stage_data_file = open(self.filename, 'r')
        self.stage_data = json.load(self.stage_data_file)
        self.stage_data_file.close()
        for number in self.stage_data:
            if self.stage_data[number]['Tile_Type'] == 0:
                spaceship.setxy(self.stage_data[number]['x'], self.stage_data[number]['y'])
            else:
                NewTile = Tile.Tile(self.stage_data[number]['Tile_Type'], self.stage_data[number]['Division'],
                                    self.stage_data[number]['x'], self.stage_data[number]['y'])
                tiles.append(NewTile)
        Stage.image = load_image('resource\Map\stage' + str(Stage.StageNum) + '.png')
        spaceship.canmove = True

    def draw(self):
        Stage.image.draw((Define_File.WINWIDTH - 108) / 2, Define_File.WINHEIGHT / 2)

# 키보드, 마우스 이벤트
def handle_events():
    global tiles
    global Tile

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Game_Framework.running = False
        elif event.type == SDL_KEYDOWN:
            if spaceship.canmove == True:
                if event.key == SDLK_UP:
                    spaceship.direction = 0
                    spaceship.canmove = False
                    for tile in tiles:
                        if tile.type == 13 and tile.division > 0 and tile.division < 361:
                            if spaceship.x + 1 > tile.x and spaceship.x - 1 < tile.x and \
                            spaceship.y + 1 > tile.y - 1 and spaceship.y - 1 < tile.y - 1:
                                tile.division = 361
                                spaceship.direction = -1
                                spaceship.canmove = True
                                break
                elif event.key == SDLK_RIGHT:
                    spaceship.direction = 1
                    spaceship.canmove = False
                    for tile in tiles:
                        if tile.type == 13 and tile.division > 0 and tile.division < 361:
                            if spaceship.x + 1 > tile.x - 1 and spaceship.x - 1 < tile.x - 1 and \
                            spaceship.y + 1 > tile.y and spaceship.y - 1 < tile.y:
                                tile.division = 361
                                spaceship.direction = -1
                                spaceship.canmove = True
                                break
                elif event.key == SDLK_DOWN:
                    spaceship.direction = 2
                    spaceship.canmove = False
                    for tile in tiles:
                        if tile.type == 13 and tile.division > 0 and tile.division < 361:
                            if spaceship.x + 1 > tile.x and spaceship.x - 1 < tile.x and \
                            spaceship.y + 1 > tile.y + 1 and spaceship.y - 1 < tile.y + 1:
                                tile.division = 361
                                spaceship.direction = -1
                                spaceship.canmove = True
                                break
                elif event.key == SDLK_LEFT:
                    spaceship.direction = 3
                    spaceship.canmove = False
                    for tile in tiles:
                        if tile.type == 13 and tile.division > 0 and tile.division < 361:
                            if spaceship.x + 1 > tile.x + 1 and spaceship.x - 1 < tile.x + 1 and \
                            spaceship.y + 1 > tile.y and spaceship.y - 1 < tile.y:
                                tile.division = 361
                                spaceship.direction = -1
                                spaceship.canmove = True
                                break
                elif event.key == SDLK_ESCAPE:
                    Game_Framework.running = False
                elif event.key == SDLK_n:
                    status_board.stagenum += 1
                    spaceship.next_stage = True
            if event.key == SDLK_g:
                if grid.OnOff == True:
                    grid.OnOff = False
                else:
                    grid.OnOff = True
            elif event.key == SDLK_b:
                if spaceship.bbOn == True:
                    spaceship.bbOn = False
                else:
                    spaceship.bbOn = True
                if Tile.Tile.bbOn == True:
                    Tile.Tile.bbOn = False
                else:
                    Tile.Tile.bbOn = True
            elif event.key == SDLK_SPACE:
                status_board.life -= 1
                if status_board.life < 0:
                    Game_Framework.change_state(Title_State)
                tiles = []
                stage.load_stage()

def get_frame_time():
    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time

def enter():
    global background, status_board, grid, spaceship, stage, tiles, shipdraw, current_time

    current_time = get_time()

    status_board = Status_Board.Status_Board()
    grid = Grid.Grid()
    spaceship = SpaceShip()
    stage = Stage()
    tiles = []
    stage.load_stage()
    hide_cursor()
    shipdraw = False

def exit():
    pass

def pause():
    pass

def resume():
    pass

def update():
    global tiles, shipdraw, stage, tiles

    frame_time = get_frame_time()
    spaceship.update(frame_time)
    spaceship.collision_check()

    Tile.Tile.gate_on = True
    for tile in tiles:
        tile.update()
    if Tile.Tile.gate_on == True:
        for tile in tiles:
            if tile.type == 1:
                tile.division = 0

def draw():
    global tiles

    clear_canvas()
    stage.draw()
    grid.draw()
    for tile in tiles:
        tile.draw()
        tile.draw_bb()
    spaceship.draw()
    spaceship.draw_bb()
    status_board.draw()
    update_canvas()
