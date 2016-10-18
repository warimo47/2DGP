from pico2d import *
import Define_File

class Tile:
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

    def __init__(self, type_num, _division, mx, my):
        self.x, self.y = mx, my
        self.type = type_num
        self.division = _division
        if Tile.Ship == None:
            Tile.Ship = load_image('resource\space_ship\space_ship0.png')
        if Tile.Exit_Gate == None:
            Tile.Exit_Gate = load_image('resource\Tiles\exit_gate.png')
        if Tile.Portal_Red == None:
            Tile.Portal_Red = load_image('resource\Tiles\portal_red.png')
        if Tile.Portal_Blue == None:
            Tile.Portal_Blue = load_image('resource\Tiles\portal_blue.png')
        if Tile.Portal_Green == None:
            Tile.Portal_Green = load_image('resource\Tiles\portal_green.png')
        if Tile.Portal_Yellow == None:
            Tile.Portal_Yellow = load_image('resource\Tiles\portal_yellow.png')
        if Tile.Portal_Purple == None:
            Tile.Portal_Purple = load_image('resource\Tiles\portal_purple.png')
        if Tile.Portal_Pink == None:
            Tile.Portal_Pink = load_image('resource\Tiles\portal_pink.png')
        if Tile.Portal_Skyblue == None:
            Tile.Portal_Skyblue = load_image('resource\Tiles\portal_skyblue.png')
        if Tile.Wall == None:
            Tile.Wall = load_image('resource\Tiles\wall.png')
        if Tile.Curve1 == None:
            Tile.Curve1 = load_image('resource\Tiles\Curve1.png')
        if Tile.Curve2 == None:
            Tile.Curve2 = load_image('resource\Tiles\Curve2.png')
        if Tile.Curve3 == None:
            Tile.Curve3 = load_image('resource\Tiles\Curve3.png')
        if Tile.Curve4 == None:
            Tile.Curve4 = load_image('resource\Tiles\Curve4.png')
        if Tile.Drill_H_B == None:
            Tile.Drill_H_B = load_image('resource\Tiles\Drill_H_B.png')
        if Tile.Drill_H_A == None:
            Tile.Drill_H_A = load_image('resource\Tiles\Drill_H_A.png')
        if Tile.Drill_W_B == None:
            Tile.Drill_W_B = load_image('resource\Tiles\Drill_W_B.png')
        if Tile.Drill_W_A == None:
            Tile.Drill_W_A = load_image('resource\Tiles\Drill_W_A.png')
        if Tile.Bomb == None:
            Tile.Bomb = load_image('resource\Tiles\Bomb.png')
        if Tile.RButton_Top == None:
            Tile.RButton_Top = load_image('resource\Tiles\RButton_Top.png')
        if Tile.RButton_Right == None:
            Tile.RButton_Right = load_image('resource\Tiles\RButton_Right.png')
        if Tile.RButton_Bottom == None:
            Tile.RButton_Bottom = load_image('resource\Tiles\RButton_Bottom.png')
        if Tile.RButton_Left == None:
            Tile.RButton_Left = load_image('resource\Tiles\RButton_Left.png')
        if Tile.GButton_Top == None:
            Tile.GButton_Top = load_image('resource\Tiles\GButton_Top.png')
        if Tile.GButton_Right == None:
            Tile.GButton_Right = load_image('resource\Tiles\GButton_Right.png')
        if Tile.GButton_Bottom == None:
            Tile.GButton_Bottom = load_image('resource\Tiles\GButton_Bottom.png')
        if Tile.GButton_Left == None:
            Tile.GButton_Left = load_image('resource\Tiles\GButton_Left.png')

    def update(self):
        if self.type == 13 and self.division > 0 and self.division < 361:
            self.division += 1

    def draw(self):
        if self.type == 0:
            Tile.Ship.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
        if self.type == 1:
            Tile.Exit_Gate.clip_draw(self.division * 36, 0, 36, 36, (self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
        if self.type == 2:
            Tile.Portal_Red.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
        if self.type == 3:
            Tile.Portal_Blue.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
        if self.type == 4:
            Tile.Portal_Green.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
        if self.type == 5:
            Tile.Portal_Yellow.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
        if self.type == 6:
            Tile.Portal_Purple.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
        if self.type == 7:
            Tile.Portal_Pink.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
        if self.type == 8:
            Tile.Portal_Skyblue.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
        if self.type == 9:
            Tile.Wall.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
        if self.type == 10:
            if self.division == 1:
                Tile.Curve1.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
            if self.division == 2:
                Tile.Curve2.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
            if self.division == 3:
                Tile.Curve3.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
            if self.division == 4:
                Tile.Curve4.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
        if self.type == 11:
            if self.division == 0:
                Tile.Drill_H_B.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
            else:
                Tile.Drill_H_A.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
        if self.type == 12:
            if self.division == 0:
                Tile.Drill_W_B.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
            else:
                Tile.Drill_W_A.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
        if self.type == 13 and self.division < 361:
            Tile.Bomb.clip_draw((self.division // 36) * 36, 0, 36, 36, (self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
        if self.type == 14:
            if self.division % 10 == 0:
                Tile.RButton_Left.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
            else:
                Tile.GButton_Left.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
            if (self.division % 100) // 10 == 0:
                Tile.RButton_Bottom.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
            else:
                Tile.GButton_Bottom.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
            if (self.division % 1000) // 100 == 0:
                Tile.RButton_Right.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
            else:
                Tile.GButton_Right.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
            if self.division // 1000 == 0:
                Tile.RButton_Top.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)
            else:
                Tile.GButton_Top.draw((self.x + 0.5) * Define_File.TILESIZE, (self.y + 0.5) * Define_File.TILESIZE)