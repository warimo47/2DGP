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
        self.image = load_image('resource\space_ship\space_ship0.png')
        self.x, self.y = -1, -1
        self.direction = 0
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
        if self.direction == 1:
            self.x = self.x + 1
        elif self.direction == 2:
            self.y = self.y - 1
        elif self.direction == 3:
            self.x = self.x - 1
        elif self.direction == 4:
            self.y = self.y + 1

    def collision_check(self):
        if self.x < 0 or self.x > 24 or self.y < 0 or self.y > 24:
            self.direction = 0
            status_board.life -= 1
            if status_board.life < 0:
                Game_Framework.change_state(Title_State)
            stage.StageNum -= 1
            ship.next_stage = True
        else:
            for tile in tiles:
                if self.x == tile.x and self.y == tile.y:
                    if tile.type == 9:
                        if self.direction == 1:
                            self.x = self.x - 1
                        elif self.direction == 2:
                            self.y = self.y + 1
                        elif self.direction == 3:
                            self.x = self.x + 1
                        elif self.direction == 4:
                            self.y = self.y - 1
                        self.canmove = True
                        self.direction = 0
                    if tile.type == 1:
                        self.direction = 0
                        self.next_stage = True
                    if tile.type == 13 and tile.division < 361:
                        if self.direction == 1:
                            self.x = self.x - 1
                        elif self.direction == 2:
                            self.y = self.y + 1
                        elif self.direction == 3:
                            self.x = self.x + 1
                        elif self.direction == 4:
                            self.y = self.y - 1
                        self.canmove = True
                        self.direction = 0
                        tile.division += 36

    def draw(self):
        self.image.clip_draw(self.frame, 0, 36, 36, (self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)

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
                if event.key == SDLK_RIGHT:
                    ship.direction = 1
                    ship.canmove = False
                elif event.key == SDLK_LEFT:
                    ship.direction = 3
                    ship.canmove = False
                elif event.key == SDLK_UP:
                    ship.direction = 4
                    ship.canmove = False
                elif event.key == SDLK_DOWN:
                    ship.direction = 2
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
    delay(0.05)