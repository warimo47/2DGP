from pico2d import *
import json
import Game_Framework
import Title_State
import Define_File
import BackGround
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
        if self.x < 0 or self.x > 24 or self.y < 0 or self.y > 24:
            self.direction = -1
            status_board.life -= 1
            if status_board.life < 0:
                Game_Framework.change_state(Title_State)
            stage.StageNum -= 1
            spaceship.next_stage = True
        else:
            for tile in tiles:
                if tile.type == 1:
                    if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                        if tile.division == 0:
                            self.direction = -1
                            status_board.stagenum += 1
                            self.next_stage = True
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
                    if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                        if tile.division == 1:
                            if self.direction == 1:
                                self.direction = 0
                                self.x = tile.x
                                self.y = tile.y
                            elif self.direction == 2:
                                self.direction = 3
                                self.x = tile.x
                                self.y = tile.y
                            else:
                                self.ship_stop(tile.x, tile.y)
                        elif tile.division == 2:
                            if self.direction == 2:
                                self.direction = 1
                                self.x = tile.x
                                self.y = tile.y
                            elif self.direction == 3:
                                self.direction = 0
                                self.x = tile.x
                                self.y = tile.y
                            else:
                                self.ship_stop(tile.x, tile.y)
                        elif tile.division == 3:
                            if self.direction == 3:
                                self.direction = 2
                                self.x = tile.x
                                self.y = tile.y
                            elif self.direction == 0:
                                self.direction = 1
                                self.x = tile.x
                                self.y = tile.y
                            else:
                                self.ship_stop(tile.x, tile.y)
                        elif tile.division == 4:
                            if self.direction == 0:
                                self.direction = 3
                                self.x = tile.x
                                self.y = tile.y
                            elif self.direction == 1:
                                self.direction = 2
                                self.x = tile.x
                                self.y = tile.y
                            else:
                                self.ship_stop(tile.x, tile.y)
                elif tile.type == 11:
                    if tile.division == 0:
                        if self.direction == 0 or self.direction == 2:
                            if self.y + 1 > tile.y and self.y - 1 < tile.y:
                                tile.division = 1
                        elif self.direction == 1:
                            if self.x > tile.x - 2 and self.x < tile.x - 2 and self.y > tile.y - 1 and self.y < tile.y + 1:
                                self.ship_stop(tile.x - 1, tile.y)
                        elif self.direction == 3:
                            if self.x > tile.x - 2 and self.x < tile.x - 2 and self.y > tile.y - 1 and self.y < tile.y + 1:
                                self.ship_stop(tile.x + 1, tile.y)
                    elif tile.division == 1:
                        if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                            self.ship_stop(tile.x, tile.y)
                elif tile.type == 12:
                    if tile.division == 0:
                        if self.direction == 0 or self.direction == 2:
                            if self.x > tile.x - 1 and self.x < tile.x + 1 and self.y + 1 > tile.y and self.y - 1 < tile.y:
                                tile.division = 1
                        elif self.direction == 1:
                            if self.x > tile.x - 2 and self.x < tile.x - 2 and self.y > tile.y - 1 and self.y < tile.y + 1:
                                self.ship_stop(tile.x - 1, tile.y)
                        elif self.direction == 3:
                            if self.x > tile.x - 2 and self.x < tile.x - 2 and self.y > tile.y - 1 and self.y < tile.y + 1:
                                self.ship_stop(tile.x + 1, tile.y)
                    elif tile.division == 1:
                        if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                            self.ship_stop(tile.x, tile.y)
                elif tile.type == 13 and tile.division < 361:
                    if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                        if tile.division > 0:
                            tile.division = 361
                        self.ship_stop(tile.x, tile.y)
                        tile.division += 36
                elif tile.type == 14:
                    if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                        if self.direction == 0:
                            tile.division += 1
                        elif self.direction == 1:
                            tile.division += 10
                        elif self.direction == 2:
                            tile.division += 100
                        elif self.direction == 3:
                            tile.division += 1000
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

class Stage:
    global tiles
    global spaceship

    def __init__(self):
        self.StageNum = 1
        self.File = None

    def load_stage(self):
        self.filename = 'Stage\Stage' + str(self.StageNum) + '.txt'
        self.stage_data_file = open(self.filename, 'r')
        self.stage_data_text = self.stage_data_file.read()
        self.stage_data = json.loads(self.stage_data_text)
        for number in self.stage_data:
            if self.stage_data[number]['Tile_Type'] == 0:
                spaceship.setxy(self.stage_data[number]['x'], self.stage_data[number]['y'])
            else:
                NewTile = Tile.Tile(self.stage_data[number]['Tile_Type'], self.stage_data[number]['Division'],
                                    self.stage_data[number]['x'], self.stage_data[number]['y'])
                tiles.append(NewTile)
        self.stage_data_file.close()
        self.StageNum += 1

# 키보드, 마우스 이벤트
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Game_Framework.running = False
        elif event.type == SDL_KEYDOWN:
            if spaceship.canmove == True:
                if event.key == SDLK_UP:
                    spaceship.direction = 0
                    spaceship.canmove = False
                elif event.key == SDLK_RIGHT:
                    spaceship.direction = 1
                    spaceship.canmove = False
                elif event.key == SDLK_DOWN:
                    spaceship.direction = 2
                    spaceship.canmove = False
                elif event.key == SDLK_LEFT:
                    spaceship.direction = 3
                    spaceship.canmove = False
                elif event.key == SDLK_ESCAPE:
                    Game_Framework.running = False
                elif event.key == SDLK_SPACE:
                    status_board.life -= 1
                    if status_board.life < 0:
                        Game_Framework.change_state(Title_State)
                    stage.StageNum -= 1
                    spaceship.next_stage = True
                elif event.key == SDLK_n:
                    status_board.stagenum += 1
                    spaceship.next_stage = True
            if event.key == SDLK_g:
                if grid.OnOff == True:
                    grid.OnOff = False
                else:
                    grid.OnOff = True

def get_frame_time():
    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time

def enter():
    global background, status_board, grid, spaceship, stage, tiles, shipdraw, current_time

    current_time = get_time()

    background = BackGround.BackGround()
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
    if int(frame_time) % 2 == 0:
        spaceship.collision_check()
    Tile.Tile.gate_on = True
    for tile in tiles:
        tile.update()
    if Tile.Tile.gate_on == True:
        for tile in tiles:
            if tile.type == 1:
                tile.division = 0

    if spaceship.next_stage == True and shipdraw == False:
        spaceship.next_stage = False
        tiles = []
        stage.load_stage()
        spaceship.canmove = True
    if shipdraw == True:
        spaceship.next_stage = False
        tiles = []
        stage.load_stage()
        delay(1.0)
        spaceship.canmove = True

def draw():
    global tiles

    clear_canvas()
    background.draw()
    grid.draw()
    for tile in tiles:
        tile.draw()
    spaceship.draw()
    status_board.draw()
    update_canvas()
    delay(0.01)