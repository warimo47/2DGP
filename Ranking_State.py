from pico2d import *
import Game_Framework
import Title_State
import Playing_State


name = "RankingState"
image = None
font = None
ranking_data = None

def draw_ranking():

    def my_sort(a):
        for i in range(len(a)):
            for j in range(i + 1, len(a) - 1):
                if a[i]['time'] < a[j]['time']:
                    a[i], a[j] = a[j], a[i]

    f = open('ranking_data.txt', 'r')
    ranking_data = json.load(f)
    f.close()

    print('[RANKING]')
    my_sort(ranking_data)
    for data in ranking_data[:10]:
        print("(Time : %4.1f,       x : %3d,        y : %d)" % (data['time'], data['x'], data['y']))

    font.draw(300, 550, "[RANKING]", (255, 255, 255))
    y = 0
    for data in ranking_data[:10]:
        font.draw(50, 500 - 50 * y, "(Time : %4.1f, x : %3d, y : %d)" % (data['time'], data['x'], data['y']), (255, 255, 255))
        y += 1

def enter():
    global image, font, ranking_data
    image = load_image('blackboard.png')
    font = load_font('ENCR10B.TTF', 40)
    ranking_data_file = open('ranking_data_file.txt', 'r')
    ranking_data = json.load(ranking_data_file)
    ranking_data_file.close()

def exit():
    global image, font
    del(image)
    del(font)

def pause():
    pass

def resume():
    pass

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Game_Framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                Game_Framework.change_state(Title_State)

def update(frame_time):
    pass

def draw(frame_time):
    global image, ranking_data

    clear_canvas()
    image.draw(400, 300)
    draw_ranking()

    update_canvas()



