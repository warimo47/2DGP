from pico2d import *

# 변수 선언
WINWIDTH = 900
WINHEIGHT = 900
TILESIZE = 36
MakingMap = True
MouseX = 0
MouseY = 0
index_x = 0
index_y = 0
ViewGrid = True
MAPx25x25 = [[0 for col in range(25)] for row in range(25)]
TileChoice = 0

# 오픈 캔버스
open_canvas(WINWIDTH + 108, WINHEIGHT)

# 이미지 로드
blbackground = load_image('resource\\background\Blackbackground.png')
ship = load_image('resource\space_ship\space_ship0.png')
stage1 = load_image('resource\Map\stage1.png')
grid = load_image('resource\Map\grid_white.png')
wall = load_image('resource\Tiles\wall.png')
exit_gate = load_image('resource\Tiles\exit_gate.png')
bomb = load_image('resource\Tiles\\bomb.png')
curve1 = load_image('resource\Tiles\curve1.png')
curve2 = load_image('resource\Tiles\curve2.png')
curve3 = load_image('resource\Tiles\curve3.png')
curve4 = load_image('resource\Tiles\curve4.png')
drill_height = load_image('resource\Tiles\drill_height.png')
drill_width = load_image('resource\Tiles\drill_width.png')
portal_red = load_image('resource\Tiles\portal_red.png')
portal_blue = load_image('resource\Tiles\portal_blue.png')
portal_skyblue = load_image('resource\Tiles\portal_skyblue.png')
portal_green = load_image('resource\Tiles\portal_green.png')
portal_yellow = load_image('resource\Tiles\portal_yellow.png')
portal_purple = load_image('resource\Tiles\portal_purple.png')
portal_pink = load_image('resource\Tiles\portal_pink.png')

# 키보드, 마우스 이벤트
def handle_events():
    global MakingMap
    global ViewGrid
    global MouseX
    global MouseY
    global TileChoice
    global TILESIZE
    global MAPx25x25
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            MakingMap = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            MouseX, MouseY = event.x, (WINHEIGHT - 1) - event.y
            # 선택 확인
            if 900 <= MouseX and MouseX < 1008 and 0 <= MouseY and MouseY < 36:
                TileChoice = 1
            elif 972 <= MouseX and MouseX < 1008 and 36 <= MouseY and MouseY < 144:
                TileChoice = 2
            elif 900 <= MouseX and MouseX < 936 and 36 <= MouseY and MouseY < 72:
                TileChoice = 3
            elif 936 <= MouseX and MouseX < 972 and 36 <= MouseY and MouseY < 72:
                TileChoice = 4
            elif 900 <= MouseX and MouseX < 936 and 72 <= MouseY and MouseY < 108:
                TileChoice = 5
            elif 936 <= MouseX and MouseX < 972 and 72 <= MouseY and MouseY < 108:
                TileChoice = 6
            elif 900 <= MouseX and MouseX < 936 and 108 <= MouseY and MouseY < 144:
                TileChoice = 7
            elif 936 <= MouseX and MouseX < 972 and 108 <= MouseY and MouseY < 144:
                TileChoice = 8
            elif 900 <= MouseX and MouseX < 936 and 144 <= MouseY and MouseY < 180:
                TileChoice = 9
            elif 936 <= MouseX and MouseX < 972 and 144 <= MouseY and MouseY < 180:
                TileChoice = 10
            elif 972 <= MouseX and MouseX < 1008 and 144 <= MouseY and MouseY < 180:
                TileChoice = 11
            elif 900 <= MouseX and MouseX < 936 and 180 <= MouseY and MouseY < 216:
                TileChoice = 12
            elif 936 <= MouseX and MouseX < 972 and 180 <= MouseY and MouseY < 216:
                TileChoice = 13
            elif 972 <= MouseX and MouseX < 1008 and 180 <= MouseY and MouseY < 216:
                TileChoice = 14
            elif 900 <= MouseX and MouseX < 936 and 216 <= MouseY and MouseY < 252:
                TileChoice = 15
            elif 936 <= MouseX and MouseX < 972 and 216 <= MouseY and MouseY < 252:
                TileChoice = 16
            elif 972 <= MouseX and MouseX < 1008 and 216 <= MouseY and MouseY < 252:
                TileChoice = 17
            elif 900 <= MouseX and MouseX < 1008 and 252 <= MouseY and MouseY < 900:
                TileChoice = 0
            else:
                etc_x = MouseX // TILESIZE
                etc_y = MouseY // TILESIZE
                MAPx25x25[etc_x][etc_y] = TileChoice
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_g:
                if ViewGrid == True:
                    ViewGrid = False
                else:
                    ViewGrid = True
            elif event.key == SDLK_ESCAPE:
                MakingMap = False

# 화면 그리기
while(MakingMap):
    handle_events()
    clear_canvas()
    stage1.draw(WINWIDTH / 2, WINHEIGHT / 2)
    if ViewGrid == True:
        grid.draw(WINWIDTH / 2, WINHEIGHT / 2)
    # 팔레트 그리기
    blbackground.draw(54 + WINWIDTH, WINHEIGHT / 2)
    drill_width.draw(54 + WINWIDTH, 18)
    drill_height.draw(90 + WINWIDTH, 90)
    bomb.clip_draw(0, 0, TILESIZE, TILESIZE, 18 + WINWIDTH, (1 + 0.5) * TILESIZE)
    exit_gate.draw(54 + WINWIDTH, 54)
    curve1.draw(54 + WINWIDTH, 90)
    curve2.draw(18 + WINWIDTH, 90)
    curve3.draw(18 + WINWIDTH, 126)
    curve4.draw(54 + WINWIDTH, 126)
    portal_red.draw(18 + WINWIDTH, 162)
    portal_blue.draw(54 + WINWIDTH, 162)
    portal_green.draw(90 + WINWIDTH, 162)
    portal_yellow.draw(18 + WINWIDTH, 198)
    portal_purple.draw(54 + WINWIDTH, 198)
    portal_pink.draw(90 + WINWIDTH, 198)
    portal_skyblue.draw(18 + WINWIDTH, 234)
    wall.draw(54 + WINWIDTH, 234)
    ship.draw(90 + WINWIDTH, 234)
    # 맵 그리기
    while(index_y < 25):
        while(index_x < 25):
            if MAPx25x25[index_y][index_x] == 1:
                pass
            elif MAPx25x25[index_y][index_x] == 2:
                pass
            elif MAPx25x25[index_y][index_x] == 3:
                bomb.clip_draw(0, 0, TILESIZE, TILESIZE, (index_x + 0.5) * TILESIZE, (index_y + 0.5) * TILESIZE)
            index_x = index_x + 1
        index_y = index_y + 1

update_canvas()
delay(0.1)

# 클로스 캔버스
close_canvas()

