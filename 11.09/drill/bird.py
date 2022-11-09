from pico2d import *
import game_framework
import random

PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 30.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5


class Bird:

    def __init__(self):
        self.x, self.y = random.randint(100,1550) ,random.randint(300,500)
        self.frame = random.randint(0,4)
        self.dir = 1
        self.image = load_image('bird_animation.png')
        self.font = load_font('ENCR10B.TTF', 16)



    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        if self.x > 1550:
            self.x = 1550
            self.dir = -1
        elif self.x < 100:
            self.x = 100
            self.dir = 1
        self.x = clamp(0, self.x, 1600)

    def draw(self):

        if self.dir == 1:
            self.image.clip_draw(int(self.frame)*182, 0, 182, 150, self.x, self.y,50,50)
        elif self.dir == -1:
            self.image.clip_composite_draw(int(self.frame)*182, 0, 182, 150,0,'h', self.x, self.y,50,50)

        self.font.draw(self.x - 60, self.y + 50, f'(Time: {get_time():.2f})', (255, 255, 0))

