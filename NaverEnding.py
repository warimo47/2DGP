from pico2d import *

# 변수 선언
WINWIDTH = 900
WINHEIGHT = 900
TILESIZE = 36
GamePlaying = True
CharX = 10
CharY = 10
CharDirection = 0
MAPx25x25 = [[0 for col in range(25)] for row in range(25)]

# 오픈 캔버스
open_canvas(WINWIDTH, WINHEIGHT)

# 이미지 로드
ship = load_image('resource\space_ship\space_ship0.png')
stage1 = load_image('resource\Map\stage1.png')
grid = load_image('resource\Map\grid_white.png')

# 키보드, 마우스 이벤트
def handle_events():
    global GamePlaying
    global CharDirection
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            GamePlaying = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                CharDirection = 1
            elif event.key == SDLK_LEFT:
                CharDirection = 3
            elif event.key == SDLK_UP:
                CharDirection = 4
            elif event.key == SDLK_DOWN:
                CharDirection = 2
            elif event.key == SDLK_ESCAPE:
                GamePlaying = False

# 화면 그리기
while(GamePlaying):
    handle_events()
    clear_canvas()
    if CharDirection == 1:
        CharX  = CharX + 1
    elif CharDirection == 2:
        CharY = CharY - 1
    elif CharDirection == 3:
        CharX = CharX - 1
    elif CharDirection == 4:
        CharY = CharY + 1

    stage1.draw(WINWIDTH / 2, WINHEIGHT / 2)
    grid.draw(WINWIDTH / 2, WINHEIGHT / 2)
    ship.draw((CharX + 0.5) * TILESIZE, (CharY + 0.5) * TILESIZE)
    update_canvas()
    delay(0.1)

# 클로스 캔버스
close_canvas()

