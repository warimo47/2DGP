from pico2d import *
import Define_File
import Status_Board
import Grid

class BackGround:
    def __init__(self):
        self.image = load_image('resource\Background\MapToolBack.png')
    def draw(self):
        self.image.draw(Define_File.WINWIDTH / 2, Define_File.WINHEIGHT / 2)

class Tiles:
    Ship = None
    Exit_Gate = None
    Wall = None
    Portal_Red = None
    Portal_Blue = None
    Portal_Green = None
    Portal_Yellow = None
    Portal_Skyblue = None
    Portal_Purple = None
    Portal_Pink = None
    Curve1 = None
    Curve2 = None
    Curve3 = None
    Curve4 = None
    Drill_H_B = None
    Drill_H_A = None
    Drill_W_B = None
    Drill_W_A = None
    Bomb = None
    RButton_Top = None
    RButton_Right = None
    RButton_Bottom = None
    RButton_Left = None
    GButton_Top = None
    GButton_Right = None
    GButton_Bottom = None
    GButton_Left = None

    def __init__(self, type_num):
        self.x, self.y = 0, 0
        self.type = type_num
        self.division = 0
        if Tiles.Ship == None:
            Tiles.Ship = load_image('resource\space_ship\space_ship0.png')
        if Tiles.Exit_Gate == None:
            Tiles.Exit_Gate = load_image('resource\Tiles\exit_gate.png')
        if Tiles.Portal_Red == None:
            Tiles.Portal_Red = load_image('resource\Tiles\portal_red.png')
        if Tiles.Portal_Blue == None:
            Tiles.Portal_Blue = load_image('resource\Tiles\portal_blue.png')
        if Tiles.Portal_Green == None:
            Tiles.Portal_Green = load_image('resource\Tiles\portal_green.png')
        if Tiles.Portal_Yellow == None:
            Tiles.Portal_Yellow = load_image('resource\Tiles\portal_yellow.png')
        if Tiles.Portal_Purple == None:
            Tiles.Portal_Purple = load_image('resource\Tiles\portal_purple.png')
        if Tiles.Portal_Pink == None:
            Tiles.Portal_Pink = load_image('resource\Tiles\portal_pink.png')
        if Tiles.Portal_Skyblue == None:
            Tiles.Portal_Skyblue = load_image('resource\Tiles\portal_skyblue.png')
        if Tiles.Wall == None:
            Tiles.Wall = load_image('resource\Tiles\wall.png')
        if Tiles.Curve1 == None:
            Tiles.Curve1 = load_image('resource\Tiles\Curve1.png')
        if Tiles.Curve2 == None:
            Tiles.Curve2 = load_image('resource\Tiles\Curve2.png')
        if Tiles.Curve3 == None:
            Tiles.Curve3 = load_image('resource\Tiles\Curve3.png')
        if Tiles.Curve4 == None:
            Tiles.Curve4 = load_image('resource\Tiles\Curve4.png')
        if Tiles.Drill_H_B == None:
            Tiles.Drill_H_B = load_image('resource\Tiles\Drill_H_B.png')
        if Tiles.Drill_H_A == None:
            Tiles.Drill_H_A = load_image('resource\Tiles\Drill_H_A.png')
        if Tiles.Drill_W_B == None:
            Tiles.Drill_W_B = load_image('resource\Tiles\Drill_W_B.png')
        if Tiles.Drill_W_A == None:
            Tiles.Drill_W_A = load_image('resource\Tiles\Drill_W_A.png')
        if Tiles.Bomb == None:
            Tiles.Bomb = load_image('resource\Tiles\Bomb.png')
        if Tiles.RButton_Top == None:
            Tiles.RButton_Top = load_image('resource\Tiles\RButton_Top.png')
        if Tiles.RButton_Right == None:
            Tiles.RButton_Right = load_image('resource\Tiles\RButton_Right.png')
        if Tiles.RButton_Bottom == None:
            Tiles.RButton_Bottom = load_image('resource\Tiles\RButton_Bottom.png')
        if Tiles.RButton_Left == None:
            Tiles.RButton_Left = load_image('resource\Tiles\RButton_Left.png')
        if Tiles.GButton_Top == None:
            Tiles.GButton_Top = load_image('resource\Tiles\GButton_Top.png')
        if Tiles.GButton_Right == None:
            Tiles.GButton_Right = load_image('resource\Tiles\GButton_Right.png')
        if Tiles.GButton_Bottom == None:
            Tiles.GButton_Bottom = load_image('resource\Tiles\GButton_Bottom.png')
        if Tiles.GButton_Left == None:
            Tiles.GButton_Left = load_image('resource\Tiles\GButton_Left.png')

    def draw(self):
        if self.type == 0:
            Tiles.Ship.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
        if self.type == 1:
            Tiles.Exit_Gate.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
        if self.type == 2:
            Tiles.Portal_Red.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
        if self.type == 3:
            Tiles.Portal_Blue.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
        if self.type == 4:
            Tiles.Portal_Green.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
        if self.type == 5:
            Tiles.Portal_Yellow.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
        if self.type == 6:
            Tiles.Portal_Purple.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
        if self.type == 7:
            Tiles.Portal_Pink.daw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
        if self.type == 8:
            Tiles.Portal_Skyblue.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
        if self.type == 9:
            Tiles.Wall.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
        if self.type == 10:
            if self.division == 0:
                Tiles.Curve1.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
            if self.division == 1:
                Tiles.Curve2.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
            if self.division == 2:
                Tiles.Curve3.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
            if self.division == 3:
                Tiles.Curve4.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
        if self.type == 11:
            Tiles.Drill_H_B.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
        if self.type == 12:
            Tiles.Drill_H_A.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
        if self.type == 13:
            Tiles.Drill_W_B.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
        if self.type == 14:
            Tiles.Drill_W_A.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
        if self.type == 15:
            Tiles.Bomb.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
        if self.type == 16:
            Tiles.Bomb.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
        if self.type == 17:
            if self.division % 10 == 0:
                Tiles.RButton_Left.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
            else:
                Tiles.GButton_Left.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
            if (self.division % 100) // 10 == 0:
                Tiles.RButton_Bottom.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
            else:
                Tiles.GButton_Bottom.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
            if (self.division % 1000) // 100 == 0:
                Tiles.RButton_Right.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
            else:
                Tiles.GButton_Right.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
            if self.division // 1000 == 0:
                Tiles.RButton_Top.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
            else:
                Tiles.GButton_Top.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)

# 키보드, 마우스 이벤트
def handle_events():
    global MakingMap
    global MouseX, MouseY
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            MakingMap = False
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            MouseX, MouseY = event.x, (Define_File.WINHEIGHT - 1) - event.y
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_g:
                if grid.OnOff == True:
                    grid.OnOff = False
                else:
                    grid.OnOff = True
            elif event.key == SDLK_ESCAPE:
                MakingMap = False

# 메인 함수
def main():
    open_canvas(Define_File.WINWIDTH, Define_File.WINHEIGHT)

    global MakingMap, grid, tiles
    background = BackGround()
    MakingMap = True
    TileChoice = 0
    grid = Grid.Grid()
    status_board = Status_Board.Status_Board()
    MouseX = 0
    MouseY = 0
    tiles = []

    while MakingMap:
        handle_events()

        clear_canvas()
        background.draw()
        if grid.OnOff == True:
            grid.draw()
        for tile in tiles:
            tile.draw()
        status_board.draw()
        update_canvas()

    close_canvas()

#초기화 함수
def setup():
    pass

if __name__ == '__main__':
    main()


