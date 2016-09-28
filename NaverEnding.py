from pico2d import *

WINWIDTH = 900
WINHEIGHT = 900
TILESIZE = 36
x = 0
frame = 0
MAPx25x25 = [[0 for col in range(25)] for row in range(25)]

open_canvas(WINWIDTH, WINHEIGHT)

#이미지 로드
ship = load_image('resource\space_ship\space_ship0.png')
stage1 = load_image('resource\Map\stage1.png')
grid = load_image('resource\Map\grid_white.png')

#화면 그리기
clear_canvas()
stage1.draw(WINWIDTH / 2, WINHEIGHT / 2)
grid.draw(WINWIDTH / 2, WINHEIGHT / 2)
ship.draw(10.5 * TILESIZE, 10.5 * TILESIZE)

update_canvas()
frame = (frame + 1) % 8
delay(5.0)
get_events()

close_canvas()

