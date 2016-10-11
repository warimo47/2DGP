from pico2d import *
import Game_Framework
import Title_State
import Define_File
import BackGround
import Status_Board
import Grid
import Wall
import Bomb
import Exit_Gate

# 초기화 코드
name = "PlayingState"
background = None
status_board = None
grid = None
walls = None
exit_gate = None
ship = None

# 게임 오브젝트 클래스 정의
class Ship:
    global wall
    def __init__(self):
        self.image = load_image('resource\space_ship\space_ship0.png')
        self.x, self.y = 12, 12
        self.direction = 0
        self.canmove = True
    def update(self):
        if self.direction == 1:
            self.x = self.x + 1
        elif self.direction == 2:
            self.y = self.y - 1
        elif self.direction == 3:
            self.x = self.x - 1
        elif self.direction == 4:
            self.y = self.y + 1
    def collision_check(self):
        for i in range(8):
            if self.x < 0 or self.x > 24 or self.y < 0 or self.y > 24:
                self.direction = 0
            elif self.x == walls[i].x and self.y == walls[i].y:
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
    def draw(self):
        self.image.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)

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
            if event.key == SDLK_g:
                if grid.OnOff == True:
                    grid.OnOff = False
                else:
                    grid.OnOff = True

def enter():
    global background, status_board, grid, walls, exit_gate, ship
    background = BackGround.BackGround()
    status_board = Status_Board.Status_Board()
    grid = Grid.Grid()
    walls = [Wall.Wall() for i in range(8)]
    walls[0].x, walls[0].y = 9, 10
    walls[1].x, walls[1].y = 10, 14
    walls[2].x, walls[2].y = 11, 8
    walls[3].x, walls[3].y = 12, 16
    walls[4].x, walls[4].y = 13, 12
    walls[5].x, walls[5].y = 14, 9
    walls[6].x, walls[6].y = 15, 15
    walls[7].x, walls[7].y = 16, 13
    exit_gate = Exit_Gate.Exit_Gate()
    ship = Ship()
    hide_cursor()

def exit():
    pass

def pause():
    pass

def resume():
    pass

def update():
    ship.update()
    ship.collision_check()

def draw():
    clear_canvas()
    background.draw()
    grid.draw()
    for i in range(8):
        walls[i].draw()
    exit_gate.draw()
    ship.draw()
    status_board.draw()
    update_canvas()