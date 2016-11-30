import Game_Framework
import Title_State
from pico2d import *
import Define_File

name = "OpeningState"
image = None
logo_time = 0.0

def enter():
    global image
    image = load_image('resource\Title\kpu_credit.png')

def exit():
    global image
    del(image)

def update():
    global logo_time
    if (logo_time > 1.0):
        logo_time = 0
        Game_Framework.push_state(Title_State)
    delay(0.01)
    logo_time += 0.01

def draw():
    global image
    clear_canvas()
    image.draw(Define_File.WINWIDTH / 2, Define_File.WINHEIGHT / 2)
    update_canvas()

def handle_events():
    events = get_events()

def pause(): pass

def resume(): pass