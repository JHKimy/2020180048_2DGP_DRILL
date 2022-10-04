from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
x = TUK_WIDTH // 2
y = TUK_WIDTH // 2
frame = 0
dirX = 0
dirY = 0
state = 3
dir_state = 0

def handle_events():
    global running
    global dirX
    global dirY
    global state
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirX += 1
                state = 1
            elif event.key == SDLK_LEFT:
                dirX -= 1
                state = 0
            elif event.key == SDLK_UP:
                dirY += 1
                if state == 2:
                    state = 0
                if state == 3:
                    state = 1
            elif event.key == SDLK_DOWN:
                dirY -= 1
                if state == 2:
                    state = 0
                if state == 3:
                    state = 1
            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirX -= 1
                state = 3
            elif event.key == SDLK_LEFT:
                dirX += 1
                state = 2
            elif event.key == SDLK_UP:
                dirY -= 1
                if state == 0:
                    state = 2
                if state == 1:
                    state = 3
            elif event.key == SDLK_DOWN:
                dirY += 1
                if state == 0:
                    state = 2
                if state == 1:
                    state = 3

open_canvas(TUK_WIDTH, TUK_HEIGHT)
TUK_GROUND = load_image('TUK_GROUND.png')
character = load_image('mario55.png')
running = True

while running:
        clear_canvas()
        TUK_GROUND.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        character.clip_draw(frame * 100, state * 100, 100, 100, x, y,150,150)
        update_canvas()
        handle_events()
        frame = (frame + 1) % 3
        x += dirX * 10
        y += dirY * 10
        delay(0.01)

        if (x > TUK_WIDTH or y > TUK_HEIGHT-90 or x < 0 or y < 90):
            break

close_canvas()