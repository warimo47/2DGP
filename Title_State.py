import Game_Framework
import Playing_State
from pico2d import *
import Define_File

name = "TitleState"
image = None
start_button = None
exit_button = None
select_start = False
select_exit = False

def enter():
    global image, start_button, exit_button
    image = load_image('resource\Title\Title.png')
    start_button = load_image('resource\Title\Start_Button.png')
    exit_button = load_image('resource\Title\Exit_Button.png')

def exit():
    global image, start_button, exit_button
    del(image)
    del(start_button)
    del(exit_button)

def handle_events():
    global select_start, select_exit

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Game_Framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            MouseX, MouseY = event.x, (Define_File.WINHEIGHT - 1) - event.y
            if 221 < MouseX and MouseX < 788 and 256 < MouseY and MouseY <= 324:
                select_start = True
            else:
                select_start = False
            if 401 < MouseX and MouseX < 607 and 118 < MouseY and MouseY <= 182:
                select_exit = True
            else:
                select_exit = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            MouseX, MouseY = event.x, (Define_File.WINHEIGHT - 1) - event.y
            if 221 < MouseX and MouseX < 788 and 256 < MouseY and MouseY <= 324:
                Game_Framework.change_state(Playing_State)
            if 401 < MouseX and MouseX < 607 and 118 < MouseY and MouseY <= 182:
                Game_Framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                Game_Framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                Game_Framework.change_state(Playing_State)

def draw():
    global select_start, select_exit
    clear_canvas()
    image.draw(Define_File.WINWIDTH / 2, Define_File.WINHEIGHT / 2)
    if select_start == True:
        start_button.draw(Define_File.WINWIDTH / 2, 290)
    if select_exit == True:
        exit_button.draw(Define_File.WINWIDTH / 2, 150)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass






