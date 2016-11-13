from pico2d import *
import tkinter as tk
from tkinter import filedialog
import Define_File
import Grid
import Tile

global MakingMap, grid, tiles, TileCount
global MouseX, MouseY
global TileChoice, TileDivision
global portal_red_num, portal_blue_num, portal_green_num, portal_yellow_num, portal_purple_num, portal_pink_num, portal_skyblue_num
global StageData

tiles, TileCount = None, None
MouseX, MouseY = None, None
TileChoice, TileDivision = None, None
portal_red_num = None
portal_blue_num = None
portal_green_num = None
portal_yellow_num = None
portal_purple_num = None
portal_pink_num = None
portal_skyblue_num = None
StageData = None
root = tk.Tk()
root.withdraw()

class BackGround:
    def __init__(self):
        self.image = load_image('resource\Background\MapToolBack.png')
    def draw(self):
        self.image.draw(Define_File.WINWIDTH / 2, Define_File.WINHEIGHT / 2)

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
            if 900 < MouseX and MouseX <= 1008:
                select_tile()
            else:
                input_tile()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_g:
                if grid.OnOff == True:
                    grid.OnOff = False
                else:
                    grid.OnOff = True
            elif event.key == SDLK_ESCAPE:
                MakingMap = False

def save_file():
    global tiles, StageData

    filename = filedialog.asksaveasfilename(filetypes=(("text files", ".txt"), ("All files", "*.*")))

    for tile in tiles:
        StageData[tiles.index(tile)] = {"Tile_Type" : tile.type, "Division" : tile.division, "x" : tile.x, "y" : tile.y}

    StageFile = open(filename, 'w')
    json.dump(StageData, StageFile)
    StageFile.close()

def all_clear():
    global tiles
    tiles = []

def select_tile():
    global MouseX, MouseY
    global TileChoice, TileDivision
    TileChoice = -1
    TileDivision = 0
    if 864 < MouseY and MouseY <= 900 and 900 < MouseX and MouseX <= 1008:
        save_file()
    if 792 < MouseY and MouseY <= 828 and 900 < MouseX and MouseX <= 1008:
        all_clear()
    if 252 < MouseY and MouseY <= 288 and 900 < MouseX and MouseX <= 936:
        TileChoice = 13
    if 252 < MouseY and MouseY <= 288 and 936 < MouseX and MouseX <= 972:
        TileChoice = 0
    if 216 < MouseY and MouseY <= 252 and 900 < MouseX and MouseX <= 936:
        TileChoice = 5
    if 216 < MouseY and MouseY <= 252 and 936 < MouseX and MouseX <= 972:
        TileChoice = 6
    if 216 < MouseY and MouseY <= 252 and 972 < MouseX and MouseX <= 1008:
        TileChoice = 8
    if 180 < MouseY and MouseY <= 216 and 900 < MouseX and MouseX <= 936:
        TileChoice = 3
    if 180 < MouseY and MouseY <= 216 and 936 < MouseX and MouseX <= 972:
        TileChoice = 4
    if 180 < MouseY and MouseY <= 216 and 972 < MouseX and MouseX <= 1008:
        TileChoice = 7
    if 144 < MouseY and MouseY <= 180 and 900 < MouseX and MouseX <= 936:
        TileChoice = 9
    if 144 < MouseY and MouseY <= 180 and 936 < MouseX and MouseX <= 972:
        TileChoice = 14
    if 144 < MouseY and MouseY <= 180 and 972 < MouseX and MouseX <= 1008:
        TileChoice = 2
    if 108 < MouseY and MouseY <= 144 and 900 < MouseX and MouseX <= 936:
        TileChoice = 10
        TileDivision = 1
    if 108 < MouseY and MouseY <= 144 and 936 < MouseX and MouseX <= 972:
        TileChoice = 10
        TileDivision = 2
    if 72 < MouseY and MouseY <= 108 and 900 < MouseX and MouseX <= 936:
        TileChoice = 10
        TileDivision = 4
    if 72 < MouseY and MouseY <= 108 and 936 < MouseX and MouseX <= 972:
        TileChoice = 10
        TileDivision = 3
    if 36 < MouseY and MouseY <= 72 and 900 < MouseX and MouseX <= 936:
        TileChoice = 1
    if 36 < MouseY and MouseY <= 72 and 936 < MouseX and MouseX <= 972:
        TileChoice = 1
        TileDivision = 1
    if 36 < MouseY and MouseY <= 144 and 972 < MouseX and MouseX <= 1008:
        TileChoice = 11
    if 0 < MouseY and MouseY <= 36 and 900 < MouseX and MouseX <= 1008:
        TileChoice = 12

def input_tile():
    if TileChoice == 0:
        for tile in tiles:
            if tile.type == 0:
                tiles.remove(tile)
                break
    elif TileChoice == 1:
        for tile in tiles:
            if tile.type == 1:
                tiles.remove(tile)
                break
    elif TileChoice == 2:
        portal_red_num  = 0
        for tile in tiles:
            if tile.type == 2:
                portal_red_num += 1
        if portal_red_num > 1:
            for tile in tiles:
                if tile.type == 2:
                    tiles.remove(tile)
                    break
    elif TileChoice == 3:
        portal_blue_num = 0
        for tile in tiles:
            if tile.type == 3:
                portal_blue_num += 1
        if portal_blue_num > 1:
            for tile in tiles:
                if tile.type == 3:
                    tiles.remove(tile)
                    break
    elif TileChoice == 4:
        portal_green_num = 0
        for tile in tiles:
            if tile.type == 4:
                portal_green_num += 1
        if portal_green_num > 1:
            for tile in tiles:
                if tile.type == 4:
                    tiles.remove(tile)
                    break
    elif TileChoice == 5:
        portal_yellow_num = 0
        for tile in tiles:
            if tile.type == 5:
                portal_yellow_num += 1
        if portal_yellow_num > 1:
            for tile in tiles:
                if tile.type == 5:
                    tiles.remove(tile)
                    break
    elif TileChoice == 6:
        portal_purple_num = 0
        for tile in tiles:
            if tile.type == 6:
                portal_purple_num += 1
        if portal_purple_num > 1:
            for tile in tiles:
                if tile.type == 6:
                    tiles.remove(tile)
                    break
    elif TileChoice == 7:
        portal_pink_num = 0
        for tile in tiles:
            if tile.type == 7:
                portal_pink_num += 1
        if portal_pink_num > 1:
            for tile in tiles:
                if tile.type == 7:
                    tiles.remove(tile)
                    break
    elif TileChoice == 8:
        portal_skyblue_num = 0
        for tile in tiles:
            if tile.type == 8:
                portal_skyblue_num += 1
        if portal_skyblue_num > 1:
            for tile in tiles:
                if tile.type == 8:
                    tiles.remove(tile)
                    break
    elif TileChoice == 11:
        if 1 > (MouseY // 36) or (MouseY // 36) > 23: return
        isdelete = True
        while(isdelete):
            isdelete = False
            for tile in tiles:
                if tile.x == (MouseX // 36) and tile.y == (MouseY // 36) - 2 and tile.type == 11:
                    tiles.remove(tile)
                    isdelete = True
                    break
                if tile.x == (MouseX // 36) and tile.y == (MouseY // 36) - 1:
                    tiles.remove(tile)
                    isdelete = True
                    break
                if tile.x == (MouseX // 36) - 1 and tile.y == (MouseY // 36) - 1 and tile.type == 12:
                    tiles.remove(tile)
                    isdelete = True
                    break
                if tile.x == (MouseX // 36) + 1 and tile.y == (MouseY // 36) - 1 and tile.type == 12:
                    tiles.remove(tile)
                    isdelete = True
                    break
                if tile.x == (MouseX // 36) and tile.y == (MouseY // 36):
                    tiles.remove(tile)
                    isdelete = True
                    break
                if tile.x == (MouseX // 36) and tile.y == (MouseY // 36) + 1:
                    tiles.remove(tile)
                    isdelete = True
                    break
                if tile.x == (MouseX // 36) - 1 and tile.y == (MouseY // 36) + 1 and tile.type == 12:
                    tiles.remove(tile)
                    isdelete = True
                    break
                if tile.x == (MouseX // 36) + 1 and tile.y == (MouseY // 36) + 1 and tile.type == 12:
                    tiles.remove(tile)
                    isdelete = True
                    break
                if tile.x == (MouseX // 36) and tile.y == (MouseY // 36) + 2 and tile.type == 11:
                    tiles.remove(tile)
                    isdelete = True
                    break
    elif TileChoice == 12:
        if 1 > (MouseX // 36) or (MouseX // 36) > 23: return
        isdelete = True
        while(isdelete):
            isdelete = False
            for tile in tiles:
                if tile.x == (MouseX // 36) - 2 and tile.y == (MouseY // 36) and tile.type == 12:
                    tiles.remove(tile)
                    isdelete = True
                    break
                if tile.x == (MouseX // 36) - 1 and tile.y == (MouseY // 36):
                    tiles.remove(tile)
                    isdelete = True
                    break
                if tile.x == (MouseX // 36) - 1 and tile.y == (MouseY // 36) - 1 and tile.type == 11:
                    tiles.remove(tile)
                    isdelete = True
                    break
                if tile.x == (MouseX // 36) - 1 and tile.y == (MouseY // 36) + 1 and tile.type == 11:
                    tiles.remove(tile)
                    isdelete = True
                    break
                if tile.x == (MouseX // 36) and tile.y == (MouseY // 36):
                    tiles.remove(tile)
                    isdelete = True
                    break
                if tile.x == (MouseX // 36) + 1 and tile.y == (MouseY // 36):
                    tiles.remove(tile)
                    isdelete = True
                    break
                if tile.x == (MouseX // 36) + 1 and tile.y == (MouseY // 36) - 1 and tile.type == 11:
                    tiles.remove(tile)
                    isdelete = True
                    break
                if tile.x == (MouseX // 36) + 1 and tile.y == (MouseY // 36) + 1 and tile.type == 11:
                    tiles.remove(tile)
                    isdelete = True
                    break
                if tile.x == (MouseX // 36) + 2 and tile.y == (MouseY // 36) and tile.type == 12:
                    tiles.remove(tile)
                    isdelete = True
                    break
    isdelete = True
    while (isdelete):
        isdelete = False
        for tile in tiles:
            if tile.x == (MouseX // 36) - 1 and tile.y == (MouseY // 36) and tile.type == 12:
                tiles.remove(tile)
                isdelete = True
                break
            if tile.x == (MouseX // 36) and tile.y == (MouseY // 36) - 1 and tile.type == 11:
                tiles.remove(tile)
                isdelete = True
                break
            if tile.x == (MouseX // 36) and tile.y == (MouseY // 36):
                tiles.remove(tile)
                isdelete = True
                break
            if tile.x == (MouseX // 36) + 1 and tile.y == (MouseY // 36) and tile.type == 12:
                tiles.remove(tile)
                isdelete = True
                break
            if tile.x == (MouseX // 36) and tile.y == (MouseY // 36) + 1 and tile.type == 11:
                tiles.remove(tile)
                isdelete = True
                break
    if TileChoice != -1:
        tiles.append(Tile.Tile(TileChoice, TileDivision, MouseX // 36, MouseY // 36))

# 메인 함수
def main():
    global MakingMap, grid, tiles, TileCount
    global MouseX, MouseY
    global TileChoice, TileDivision
    global portal_red_num, portal_blue_num, portal_green_num, portal_yellow_num, portal_purple_num, portal_pink_num, portal_skyblue_num
    global MapToolSetupData, StageData

    MapToolSetupFile = open('MapToolSetup.txt', 'r')
    MapToolSetupData = json.load(MapToolSetupFile)
    MapToolSetupFile.close()

    open_canvas(Define_File.WINWIDTH, Define_File.WINHEIGHT)

    background = BackGround()
    MakingMap = True
    grid = Grid.Grid()
    grid.OnOff = True
    tiles = []
    StageData = {}

    TileCount = MapToolSetupData["TileCount"]
    TileChoice = MapToolSetupData["TileChoice"]
    TileDivision = MapToolSetupData["TileDivision"]
    MouseX, MouseY = MapToolSetupData["MouseX"], MapToolSetupData["MouseY"]
    portal_red_num = MapToolSetupData["Portal_Red_Num"]
    portal_blue_num = MapToolSetupData["Portal_Blue_Num"]
    portal_green_num = MapToolSetupData["Portal_Green_Num"]
    portal_yellow_num = MapToolSetupData["Portal_Yellow_Num"]
    portal_purple_num = MapToolSetupData["Portal_Purple_Num"]
    portal_pink_num = MapToolSetupData["Portal_Pink_Num"]
    portal_skyblue_num = MapToolSetupData["Portal_Skyblue_Num"]

    while MakingMap:
        handle_events()

        clear_canvas()
        background.draw()
        if grid.OnOff == True:
            grid.draw()
        for tile in tiles:
            tile.draw()
        update_canvas()

    close_canvas()

# 초기화 함수
def setup():
    pass

if __name__ == '__main__':
    main()


