from pico2d import *

# 게임 오브젝트 클래스 정의
class BackGround:
    def __init__(self):
        self.image = load_image('resource\Map\stage1.png')
        self.StageNum = 1
    def draw(self):
        self.image.draw(WINWIDTH / 2, WINHEIGHT / 2)
class Status_board:
    def __init__(self):
        self.image = load_image('resource\Background\Blackbackground.png')
    def draw(self):
        self.image.draw(WINWIDTH + 54, WINHEIGHT / 2)
class Grid:
    def __init__(self):
        self.image = load_image('resource\Map\grid_white.png')
        self.OnOff = False
    def draw(self):
        if self.OnOff == True:
            self.image.draw(WINWIDTH / 2, WINHEIGHT / 2)
class Wall:
    def __init__(self):
        self.image = load_image('resource\Tiles\wall.png')
        self.x, self.y = -1, -1
    def draw(self):
        self.image.draw((self.x + 0.5) * TILESIZE, (self.y + 0.5) * TILESIZE)
class Bomb:
    def __init__(self):
        self.image = load_image('resource\Tiles\\bomb.png')
        self.x, self.y = -1, -1
    def draw(self):
        self.image.draw((self.x + 0.5) * TILESIZE, (self.y + 0.5) * TILESIZE)
class Exit_gate:
    def __init__(self):
        self.image = load_image('resource\Tiles\exit_gate.png')
        self.x, self.y = 8, 11
    def draw(self):
        self.image.draw((self.x + 0.5) * TILESIZE, (self.y + 0.5) * TILESIZE)
class Ship:
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
        self.image.draw((self.x + 0.5) * TILESIZE, (self.y + 0.5) * TILESIZE)

# 키보드, 마우스 이벤트
def handle_events():
    global GamePlaying
    global ship
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            GamePlaying = False
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
                    GamePlaying = False
            if event.key == SDLK_g:
                if grid.OnOff == True:
                    grid.OnOff = False
                else:
                    grid.OnOff = True

# 초기화 코드
WINWIDTH = 900
WINHEIGHT = 900
TILESIZE = 36
GamePlaying = True
open_canvas(WINWIDTH + 108, WINHEIGHT)
background = BackGround()
status_board = Status_board()
grid = Grid()
walls = [Wall() for i in range(8)]
walls[0].x, walls[0].y = 9, 10
walls[1].x, walls[1].y = 10, 14
walls[2].x, walls[2].y = 11, 8
walls[3].x, walls[3].y = 12, 16
walls[4].x, walls[4].y = 13, 12
walls[5].x, walls[5].y = 14, 9
walls[6].x, walls[6].y = 15, 15
walls[7].x, walls[7].y = 16, 13
exit_gate = Exit_gate()
ship = Ship()
hide_cursor()

# 게임 루프 코드
while(GamePlaying):
    handle_events()

    # update
    ship.update()
    ship.collision_check()
    clear_canvas()

    # draw
    background.draw()
    grid.draw()
    for i in range(8):
        walls[i].draw()
    exit_gate.draw()
    ship.draw()
    status_board.draw()

    update_canvas()
    delay(0.05)

# 종료 코드
close_canvas()

