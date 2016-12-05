import platform
import os

if platform.architecture()[0] == '32bit':
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x86"
else:
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x64"

from pico2d import *
import Game_Framework
import Opening_State
import Title_State
import Playing_State
import Define_File

open_canvas(Define_File.WINWIDTH, Define_File.WINHEIGHT)
Game_Framework.run(Opening_State)
close_canvas()
