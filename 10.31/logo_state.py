from pico2d import *
import game_framework
import title_state
import play_state
running = True
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('tuk_credit.png')


def exit():
    global image
    del image

def update():
    # logo time을 계산하고, 그결과에 따라 1초가 넘으면 런닝을 false로 변경
    global logo_time, running
    if logo_time >= 1.0:
       logo_time = 0.0
       game_framework.change_state(title_state)
    delay(0.01)
    logo_time += 0.01

    pass

def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()

def handle_events():
    events = get_events()





