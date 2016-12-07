from pico2d import *
import Game_Framework
import Title_State
import Playing_State
import Define_File

name = "RankingState"
image = None
font = None
bigfont = None
ranking_data = None

def draw_ranking():
    def my_sort_stagenum(a):
        for i in range(len(a)):
            for j in range(len(a) - 1):
                if a[j]['StageNumber'] < a[j + 1]['StageNumber']:
                    a[j], a[j + 1] = a[j + 1], a[j]

    def my_sort_movecount(a):
        for i in range(len(a)):
            for j in range(len(a) - 1):
                if a[j]['Movecount'] > a[j + 1]['Movecount']:
                    a[j], a[j + 1] = a[j + 1], a[j]

    bigfont.draw(350, 840, "[ RANKING ]", (255, 255, 255))

    if len(ranking_data) > 1:
        my_sort_movecount(ranking_data)
        my_sort_stagenum(ranking_data)

    y = 1
    for data in ranking_data[:10]:
        if y == 1:
            if data['StageNumber'] > 30:
                font.draw(65, 825 - 75 * y, "%2d. [Player %d]   Stage : EARTH Move : %4d)" % (y, data['PlayerNumber'], data['Movecount']), (255, 255, 255))
            else:
                font.draw(65, 825 - 75 * y, "%2d. [Player %d]   Stage : %4d    Move : %4d)" % (y, data['PlayerNumber'], data['StageNumber'], data['Movecount']), (255, 255, 255))
        elif y == 10:
            if data['StageNumber'] > 30:
                font.draw(55, 825 - 75 * y, "%2d. [Player %d]   Stage : EARTH Move : %4d)" % (y, data['PlayerNumber'], data['Movecount']), (255, 255, 255))
            else:
                font.draw(55, 825 - 75 * y, "%2d. [Player %d]   Stage : %4d    Move : %4d)" % (y, data['PlayerNumber'], data['StageNumber'], data['Movecount']), (255, 255, 255))
        else:
            if data['StageNumber'] > 30:
                font.draw(50, 825 - 75 * y, "%2d. [Player %d]   Stage : EARTH Move : %4d)" % (y, data['PlayerNumber'], data['Movecount']), (255, 255, 255))
            else:
                font.draw(50, 825 - 75 * y, "%2d. [Player %d]   Stage : %4d    Move : %4d)" % (y, data['PlayerNumber'], data['StageNumber'], data['Movecount']), (255, 255, 255))

        y += 1

def enter():
    global image, font, bigfont, ranking_data
    image = load_image('resource\Background\RankingScreen.png')
    font = load_font('digital-7.TTF', 50)
    bigfont = load_font('digital-7.TTF', 80)

    ranking_data_file = open('RankingDataFile.txt', 'r')
    ranking_data = json.load(ranking_data_file)
    ranking_data_file.close()

def exit():
    global image, font, bigfont
    del image
    del font
    del bigfont

def pause():
    pass

def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Game_Framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                Game_Framework.change_state(Title_State)

def update():
    pass

def draw():
    global image, ranking_data

    clear_canvas()
    image.draw(Define_File.WINWIDTH / 2, Define_File.WINHEIGHT / 2)
    draw_ranking()

    update_canvas()



