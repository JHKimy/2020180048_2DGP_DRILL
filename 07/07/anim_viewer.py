from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('attack.png')
attack = load_image('attack2.png')
walking = load_image('walking.png')

frame = 0

def animation(A,frameX,sizeX,sizeY,y,frameN):
    global frame
    clear_canvas()
    grass.draw(400, 30)
    A.clip_draw(frame * frameX, 0, sizeX, sizeY, x, y)
    update_canvas()
    frame = (frame + 1) % frameN
    delay(0.1)
    get_events()

for x in range(100, 400, 7):
    animation(walking,80,80,80,90,11)

for x in range(400,600,3):
    animation(attack,100,100,85,90,15)

for x in range(600, 610, 10):
    clear_canvas()
    grass.draw(400, 30)
    attack.clip_draw(frame * 100, 0, 100, 85, x, 110,125,125)
    update_canvas()
    frame = (frame + 1) % 15
    delay(0.1)
    get_events()

for x in range(610, 800, 15):
    animation(character, 147, 147, 110, 100, 9)

close_canvas()
