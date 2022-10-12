import game_framework
import project

from pico2d import *

image = None

def enter():
    global image
    image = load_image('start.png')

def exit():
    global image
    del image

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(project)


def draw():
    clear_canvas()
    image.draw(800, 600)
    update_canvas()
