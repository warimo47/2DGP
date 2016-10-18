from pico2d import *
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
class Ship:
    global tiles
    global exit_gate

    def __init__(self):
        self.stop = load_image('resource\space_ship\space_ship0.png')
        self.image = load_image('resource\space_ship\space_ship.png')
        self.x, self.y = -1, -1
        self.direction = -1
        self.canmove = True
        self.next_stage = False
        self.frame = 0

    def setxy(self, xx, yy):
        self.x, self.y = xx, yy

    def update(self):
        global shipdraw
        shipdraw = False
        if self.next_stage == True:
            shipdraw = True
        if self.direction == 0:
            self.y += Define_File.MOVEDISTANCE
        elif self.direction == 1:
            self.x += Define_File.MOVEDISTANCE
        elif self.direction == 2:
            self.y -= Define_File.MOVEDISTANCE
        elif self.direction == 3:
            self.x -= Define_File.MOVEDISTANCE

    def collision_check(self):
        if self.x < 0 or self.x > 24 or self.y < 0 or self.y > 24:
            self.direction = -1
            status_board.life -= 1
            if status_board.life < 0:
                Game_Framework.change_state(Title_State)
            stage.StageNum -= 1
            ship.next_stage = True
        else:
            for tile in tiles:
                if tile.type == 1:
                    if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                        if tile.division == 0:
                            self.direction = -1
                            self.next_stage = True
                        else:
                            self.ship_stop()
                if tile.type == 2:
                    pass
                if tile.type == 3:
                    pass
                if tile.type == 4:
                    pass
                if tile.type == 5:
                    pass
                if tile.type == 6:
                    pass
                if tile.type == 7:
                    pass
                if tile.type == 8:
                    pass
                if tile.type == 9:
                    if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                        self.ship_stop()
                if tile.type == 10:
                    pass
                if tile.type == 11:
                    if tile.division == 0:
                        if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y + 1 and self.y - 1 < tile.y + 1:
                            self.ship_stop()
                        elif self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                                tile.division = 1
                        elif self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y - 1 and self.y - 1 < tile.y - 1:
                            self.ship_stop()
                    else:
                        if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                            self.ship_stop()
                if tile.type == 12:
                    if tile.division == 0:
                        if self.x + 1 > tile.x + 1 and self.x - 1 < tile.x + 1 and self.y + 1 > tile.y and self.y - 1 < tile.y:
                            self.ship_stop()
                        elif self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                                tile.division = 1
                        elif self.x + 1 > tile.x - 1 and self.x - 1 < tile.x - 1 and self.y + 1 > tile.y and self.y - 1 < tile.y:
                            self.ship_stop()
                    else:
                        if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                            self.ship_stop()
                if tile.type == 13 and tile.division < 361:
                    if self.x + 1 > tile.x and self.x - 1 < tile.x and self.y + 1 > tile.y and self.y - 1 < tile.y:
                        if tile.division > 0:
                            tile.division = 361
                        self.ship_stop()
                        tile.division += 36

    def ship_stop(self):
        if self.direction == 0:
            self.y -= Define_File.MOVEDISTANCE
        elif self.direction == 1:
            self.x -= Define_File.MOVEDISTANCE
        elif self.direction == 2:
            self.y += Define_File.MOVEDISTANCE
        elif self.direction == 3:
            self.x += Define_File.MOVEDISTANCE
        self.canmove = True
        self.direction = -1

    def draw(self):
        if self.direction == -1:
            self.stop.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
        else:
            self.image.clip_draw(self.frame * 70, self.direction * 70, 70, 70, (self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)

class Stage:
    global tiles
    global ship

    def __init__(self):
        self.StageNum = 1
        self.File = None

    def load_stage(self):
        self.filename = 'Stage\Stage' + str(self.StageNum) + '.txt'
        self.File = open(self.filename, 'r')
        self.tile_num = int(self.File.readline())
        while(self.tile_num):
            temp_type = int(self.File.readline())
            temp_division = int(self.File.readline())
            temp_x = int(self.File.readline())
            temp_y = int(self.File.readline())
            tiles.append(Tile.Tile(temp_type, temp_division, temp_x, temp_y))
            self.tile_num -= 1
        self.File.close()
        for tile in tiles:
            if tile.type == 0:
                ship.setxy(tile.x, tile.y)
                tiles.remove(tile)
                break
        self.StageNum += 1

# 키보드, 마우스 이벤트
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Game_Framework.running = False
        elif event.type == SDL_KEYDOWN:
            if ship.canmove == True:
                if event.key == SDLK_UP:
                    ship.direction = 0
                    ship.canmove = False
                elif event.key == SDLK_RIGHT:
                    ship.direction = 1
                    ship.canmove = False
                elif event.key == SDLK_DOWN:
                    ship.direction = 2
                    ship.canmove = False
                elif event.key == SDLK_LEFT:
                    ship.direction = 3
                    ship.canmove = False
                elif event.key == SDLK_ESCAPE:
                    Game_Framework.running = False
                elif event.key == SDLK_SPACE:
                    status_board.life -= 1
                    if status_board.life < 0:
                        Game_Framework.change_state(Title_State)
                    stage.StageNum -= 1
                    ship.next_stage = True
                elif event.key == SDLK_n:
                    ship.next_stage = True
            if event.key == SDLK_g:
                if grid.OnOff == True:
                    grid.OnOff = False
                else:
                    grid.OnOff = True

def enter():
    global background, status_board, grid, ship, stage, tiles, shipdraw

    background = BackGround.BackGround()
    status_board = Status_Board.Status_Board()
    grid = Grid.Grid()
    ship = Ship()
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

    ship.update()
    ship.collision_check()
    for tile in tiles:
        tile.update()

    if ship.next_stage == True and shipdraw == False:
        ship.next_stage = False
        tiles = []
        stage.load_stage()
        ship.canmove = True
    if shipdraw == True:
        ship.next_stage = False
        tiles = []
        stage.load_stage()
        delay(1.0)
        ship.canmove = True

def draw():
    global tiles

    clear_canvas()
    background.draw()
    grid.draw()
    for tile in tiles:
        tile.draw()
    ship.draw()
    status_board.draw()
    update_canvas()
    delay(0.01)