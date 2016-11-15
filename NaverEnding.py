from pico2d import *
import Game_Framework
import Opening_State
import Playing_State
import Define_File

open_canvas(Define_File.WINWIDTH, Define_File.WINHEIGHT)
Game_Framework.run(Opening_State)
close_canvas()