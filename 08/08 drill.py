from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
x = TUK_WIDTH // 2
y = TUK_WIDTH // 2
frame = 0
X = 0
state = 0
Y = 0

def handle_events():
    global running
    global X
    global Y
    global state
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                X += 1
                state = 1
            elif event.key == SDLK_LEFT:
                X -= 1
                state = 0
            elif event.key == SDLK_UP:
                Y += 1
            elif event.key == SDLK_DOWN:
                Y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                X -= 1
            elif event.key == SDLK_LEFT:
                X += 1
            elif event.key == SDLK_UP:
                Y -= 1
            elif event.key == SDLK_DOWN:
                Y += 1

open_canvas(TUK_WIDTH, TUK_HEIGHT)
TUK_GROUND = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
running = True

while running:
        clear_canvas()
        TUK_GROUND.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        character.clip_draw(frame * 100, state * 100, 100, 100, x, y)
        update_canvas()
        handle_events()
        frame = (frame + 1) % 8
        x += X * 5
        y += Y * 5
        delay(0.01)

        if (x > TUK_WIDTH or y > TUK_HEIGHT or x < 0 or y < 0):
            break

close_canvas()