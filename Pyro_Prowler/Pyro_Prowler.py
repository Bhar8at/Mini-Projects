# Libraries used
import pygame
import os
import random as r
from pygame import mixer
import time

pygame.init()
pygame.font.init()

# Variables declared
speedoffb = 5
FPS = 60  # Frame rate
score = 0
text_font = pygame.font.SysFont("monospace", 50)
clock = pygame.time.Clock()
multiplier = 1
game_time = 0
gui_font = pygame.font.Font(None, 30)


# Button
class Button_main:
    def __init__(self, text, width, height, pos, elevation):
        # Core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elecation = elevation
        self.original_y_pos = pos[1]

        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = (255, 255, 255)

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos, (width, height))
        self.bottom_color = (50, 50, 50)
        # text
        self.text_surf = gui_font.render(text, True, (0, 0, 0))
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self):
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elecation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

        pygame.draw.rect(window, self.bottom_color, self.bottom_rect, border_radius=12)
        pygame.draw.rect(window, self.top_color, self.top_rect, border_radius=12)
        window.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = (200, 0, 0)
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elecation = 0
                self.pressed = True
            else:
                self.dynamic_elecation = self.elevation
                if self.pressed:
                    global  run
                    self.pressed = False
                    mixer.music.stop()
                    run = False
                    main()
        else:
            self.dynamic_elecation = self.elevation
            self.top_color = (255 , 255, 255)
class Button_tryagain:
    def __init__(self, text, width, height, pos, elevation):
        # Core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elecation = elevation
        self.original_y_pos = pos[1]

        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = (255, 255, 255)

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos, (width, height))
        self.bottom_color = (50, 50, 50)
        # text
        self.text_surf = gui_font.render(text, True, (0, 0, 0))
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self):
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elecation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

        pygame.draw.rect(window, self.bottom_color, self.bottom_rect, border_radius=12)
        pygame.draw.rect(window, self.top_color, self.top_rect, border_radius=12)
        window.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = (200, 0, 0)
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elecation = 0
                self.pressed = True
            else:
                self.dynamic_elecation = self.elevation
                if self.pressed:
                    global run
                    run = False
                    mixer.music.stop()
                    self.pressed = False
                    main()
        else:
            self.dynamic_elecation = self.elevation
            self.top_color = (255, 255, 255)

class Button_return_main:
    def __init__(self, text, width, height, pos, elevation):
        # Core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elecation = elevation
        self.original_y_pos = pos[1]

        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = (255, 255, 255)

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos, (width, height))
        self.bottom_color = (50, 50, 50)
        # text
        self.text_surf = gui_font.render(text, True, (0, 0, 0))
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self):
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elecation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

        pygame.draw.rect(window, self.bottom_color, self.bottom_rect, border_radius=12)
        pygame.draw.rect(window, self.top_color, self.top_rect, border_radius=12)
        window.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = (200, 0, 0)
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elecation = 0
                self.pressed = True
            else:
                self.dynamic_elecation = self.elevation
                if self.pressed:
                    global  run
                    run = False
                    mixer.music.stop()
                    self.pressed = False
                    main_page()
        else:
            self.dynamic_elecation = self.elevation
            self.top_color = (255 , 255, 255)

# Predefined functions


def create_window(WIDTH, HEIGHT, CAPTION):
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(CAPTION)
    return window


# To create window w/ dimensions and caption
window = create_window(900, 900, " Pyro Prowler ")

# Background
space = pygame.image.load(os.path.join("dodge_boms_assets", "space.png"))
space = pygame.transform.scale(space, (1800, 1800))
space_1 = space
space_rage = pygame.image.load(os.path.join("dodge_boms_assets", "space_rage.png"))
space_rage = pygame.transform.scale(space_rage, (900, 900))
space_y = [0, 900, 1800]
scroll = 0
speedofbg = 5

# Sprites
mc_c = pygame.image.load(os.path.join("dodge_boms_assets", "mc.png"))  # Main character
mc = pygame.transform.scale(mc_c, (50, 45))
spofmc = 10
act_jetpack = False
jetpack_counter = 0

# COLORS
BLACK = (0, 0, 0)

# FIREBALLS
max_balls = 3
balls_v = []
balls_h = []
ball_v = pygame.image.load(os.path.join("dodge_boms_assets", "fireball-png-pic-25.png"))
ball_v = pygame.transform.scale(ball_v, (100, 90))
ball_counter = 5
v_Fb = h_Fb = False
big_balls = []

# Orbs
orb1_img = pygame.image.load(os.path.join("dodge_boms_assets", "orb1.png"))
orb1_img = pygame.transform.scale(orb1_img, (100, 100))
orbing = r.randrange(10, 15)
activate_orb1 = False
continue_orb1 = False
orbs = []
booster_timer = 0
activate_booster_status = False

# Main page sprites
mainpage = pygame.image.load(os.path.join("dodge_boms_assets", "Mainpage.png"))



# Power up functions

def activate_booster():
    global spofmc, mc, FPS, multiplier, activate_booster_status, space, space_rage, speedoffb
    spofmc = 15
    speedoffb = 20
    FPS = 80
    multiplier = 5
    mc_c = pygame.image.load(os.path.join("dodge_boms_assets", "mc_rage.png"))  # Main character
    mc = pygame.transform.scale(mc_c, (50, 45))
    activate_booster_status = True
    space = space_rage


def deactivate_booster():  # Gets activated by mistake ?
    global spofmc, mc, FPS, multiplier, space_1, space, activate_booster_status
    activate_booster_status = False
    spofmc = 10
    FPS = 60
    multiplier = 1
    mc_c = pygame.image.load(os.path.join("dodge_boms_assets", "mc.png"))  # Main character
    mc = pygame.transform.scale(mc_c, (50, 45))
    space = space_1


# Window Paint

def game_window(mc_hit, mcc, balls, score, orbs, Fb, Fb_big):
    global ball, continue_orb1, activate_orb1, space_y, scroll, speedofbg, ball_counter, boost, act_jetpack, v_Fb, h_Fb, balls_h, jetpack_counter, big_balls

    # to have infinite scrolling display
    if Fb:
        if v_Fb:
            window.blit(space, (0, 0 + scroll))
            window.blit(space, (0, -900 + scroll))
            window.blit(space, (0, -1800 + scroll))
        elif h_Fb:
            window.blit(space, (0 - scroll, 0))
            window.blit(space, (900 - scroll, 0))
            window.blit(space, (1800 - scroll, 0))
    else:
        window.blit(space, (0, 0 + scroll))
        window.blit(space, (0, -900 + scroll))
        window.blit(space, (0, -1800 + scroll))

    if scroll >= 900:
        scroll = 0
    scroll += speedofbg

    # To provide animating fireball and switch between differently oriented fireballs and also the big fireballs
    if Fb:
        if round(ball_counter) == 8 or round(ball_counter) not in (5,6,7,8):
            ball_counter = 5
        else:
            ball_counter += 0.15
        if v_Fb:
            ball = pygame.image.load(os.path.join("dodge_boms_assets", f"fireball-png-pic-2{round(ball_counter)}.png"))
            ball = pygame.transform.scale(ball, (100, 90))
            for i in balls_v:
                window.blit(ball, (i.x, i.y))
        elif h_Fb:
            ball = pygame.image.load(os.path.join("dodge_boms_assets", f"fireball-png-pic-2{round(ball_counter)}l.png"))
            ball = pygame.transform.scale(ball, (100, 90))
            for i in balls_h:
                window.blit(ball, (i.x, i.y))
    elif Fb_big:
        if round(ball_counter) == 5 or round(ball_counter) not in (1,2,3,4):
            ball_counter = 1
        ball = pygame.image.load(os.path.join("dodge_boms_assets", f"bigfire{round(ball_counter)}.png"))
        ball = pygame.transform.scale(ball, (400, 300))
        ball_counter += 0.1
        if big_balls != []:
            x = big_balls[0].x
            y = big_balls[0].y
            window.blit(ball, (x,y))

    # Animating the jetpack
    if act_jetpack:
        if round(jetpack_counter) == 3:
            jetpack_counter = 0
        boost = pygame.image.load(os.path.join("dodge_boms_assets", f"boost{round(jetpack_counter)}.png"))
        boost = pygame.transform.scale(boost, (40, 35))
        window.blit(boost, (mc_hit.x, mc_hit.y + 35))
        window.blit(mcc, (mc_hit.x, mc_hit.y))
        jetpack_counter += 0.1

    # for main character
    window.blit(mcc, (mc_hit.x, mc_hit.y))
    # for scorecard
    window.blit(score, (800, 800))
    # to display orb
    for i in orbs:
        window.blit(orb1_img, (i.x, i.y))
    pygame.display.update(())


# End page
end = pygame.image.load(os.path.join("dodge_boms_assets", "loserpage.png"))
end = pygame.transform.scale(end, (600, 400))
tryagain = Button_tryagain('TRY AGAIN', 200, 70, (350, 600), 5)
mainmenu = Button_return_main('MAIN MENU', 200, 70, (350, 700), 5)



def endgame(score):
    mixer.music.stop()
    mixer.Sound("dodge_boms_assets/gameover.wav").play()
    global balls, act_jetpack, balls_h, balls_v
    balls_h = balls_v = []
    act_jetpack = False
    run = True
    while run:
        clock.tick(FPS)
        window.fill(BLACK)
        window.blit(end, (200, 200))
        window.blit(score, (450, 500))
        tryagain.draw()
        mainmenu.draw()

        # to check for quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
    pygame.quit()


# Title Page
button1 = Button_main('PLAY', 200, 70, (350, 700), 5)
def main_page():
    mixer.music.load("dodge_boms_assets/mainmenubgm.wav")
    mixer.music.play(-1)
    time.sleep(0.25)
    global score, space_y
    score = 0
    run = True
    while run:
        clock.tick(FPS)
        window.blit(space, (0, 0))
        window.blit(mainpage, (0, 0))
        button1.draw()

        for event in pygame.event.get():
            # To check for quit
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
    pygame.quit()

# Victory page
def victory_page(score):
    run = True
    youwin = pygame.image.load(os.path.join("dodge_boms_assets", "youwin.png"))
    while run:
        clock.tick(FPS)
        window.blit(youwin, (0, 0))
        window.blit(score, (450, 700))
        mainmenu.draw()
        for event in pygame.event.get():
            # To check for quit
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
    pygame.quit()

# Game loop

def main():
    mixer.music.load("dodge_boms_assets/gliding.mp3")
    mixer.music.play()
    global balls_v, balls_h, score, text_font, Scoreboard, activate_orb1, booster_timer, activate_booster_status, FPS, speedoffb, speedofbg, game_time, act_jetpack, v_Fb, h_Fb, big_balls, spofmc
    FPS = 60
    v_Fb = True
    speedofbg = speedoffb = 5
    score = 0
    game_time = 0
    mc_hit = pygame.Rect(400, 800, 50, 45)
    mc_hit.x = 450
    clock = pygame.time.Clock()
    run = True
    start_time = time.time()
    Fireballs_wanted = True
    Fireballs_wanted_big = False
    while run:
        current_time = time.time()
        time_taken = round(current_time - start_time)  # To find time taken
        clock.tick(FPS)  # To fix fps

        # to check for quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Fireballs
        if v_Fb:
            if Fireballs_wanted:
                while len(balls_v) < max_balls:
                    x = r.randrange(0, 900)
                    y = pygame.Rect(x, 0, 100, 90)
                    balls_v.append(y)
            if Fireballs_wanted_big:
                while big_balls == []:
                    x = r.randrange(100, 600)
                    y = pygame.Rect(x, -400, 400, 300)
                    big_balls.append(y)
                if big_balls[0].colliderect(mc_hit):
                    run = False
                    booster_timer = 0
                    deactivate_booster()
                    endgame(Scoreboard)
                for i in big_balls:
                    i.y += speedoffb+5
                    if i.y > 900:
                        ball_dodge_sound = mixer.Sound("dodge_boms_assets/scored.mp3")
                        ball_dodge_sound.play()
                        big_balls.remove(i)
                        score += multiplier * max_balls ** -1
                        if activate_booster_status:
                            booster_timer += 1


            for i in balls_v:
                print(speedoffb)
                i.y += speedoffb
                if i.y > 900:
                    ball_dodge_sound = mixer.Sound("dodge_boms_assets/scored.mp3")
                    ball_dodge_sound.play()
                    balls_v.remove(i)
                    score += multiplier * max_balls ** -1
                    if activate_booster_status:
                        booster_timer += 1
                if i.colliderect(mc_hit):
                    run = False
                    booster_timer = 0
                    deactivate_booster()
                    endgame(Scoreboard)
        elif h_Fb:
            if Fireballs_wanted:
                while len(balls_h) < max_balls:
                    x = r.randrange(0, 900)
                    y = pygame.Rect(900, x, 100, 90)
                    balls_h.append(y)
            for i in balls_h:
                i.x -= speedoffb
                if i.x < 0:
                    ball_dodge_sound = mixer.Sound("dodge_boms_assets/scored.mp3")
                    ball_dodge_sound.play()
                    balls_h.remove(i)
                    score += multiplier * max_balls ** -1
                    if activate_booster_status:
                        booster_timer += 1
                if i.colliderect(mc_hit):
                    run = False
                    booster_timer = 0
                    deactivate_booster()
                    endgame(Scoreboard)

        # Hype from song
        if time_taken in range(15, 41):
            FPS = 60
            speedoffb = 15
            speedofbg = 10
            act_jetpack = True

        elif time_taken in range(41, 44):
            balls_h = balls_v = []
            v_Fb = False
            h_Fb = True
            if mc_hit.x > 100:
                mc_hit.x -= 10
            if mc_hit.y > 450:
                mc_hit.y -= 10

        elif time_taken in range(44, 59):
            v_Fb = False
            h_Fb = True

        elif time_taken in range(59, 65):  # switch to left !!
            v_Fb = True
            h_Fb = False
            FPS = 60
            speedoffb = 7
            speedofbg = 8
            if mc_hit.y < 800:
                mc_hit.y += 20
            act_jetpack = False

        elif time_taken in range(65, 80):
            v_Fb = True
            h_Fb = False
            FPS = 60
            Fireballs_wanted = False
            Fireballs_wanted_big = True
            spofmc = 20
        elif time_taken in range(80, 85):
            v_Fb = True
            h_Fb = False
            Fireballs_wanted = True
            Fireballs_wanted_big = False
            speedoffb = 15
        elif time_taken in range(85, 90):
            Fireballs_wanted = False
            mc_hit.y -= 3
        elif time_taken > 90:
            run = False
            victory_page(Scoreboard)

        else:
            v_Fb = True
            h_Fb = False
            FPS = 60
            speedoffb = 7
            speedofbg = 5
            act_jetpack = False
            Fireballs_wanted = True
            Fireballs_wanted_big = False

        # Power ups

        if round(score) % orbing == 0 and score != 0 and len(orbs) < 1:
            orbs.append(pygame.Rect(r.randrange(0, 900), 0, 50, 50))

        for i in orbs:
            i.y += 10
            if i.y > 900:
                orbs.remove(i)
            if i.colliderect(mc_hit):
                booster_timer = 0
                activate_booster()
        if booster_timer > 15 and activate_booster_status:
            deactivate_booster()
            booster_timer = 0

        # Scoreboard
        Scoreboard = text_font.render(f"{round(score)}", 1, (255, 255, 255))

        # Keyboard movements for mc
        key_pressed = pygame.key.get_pressed()
        if v_Fb:
            if key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
                mc_hit.x += spofmc

            if key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
                mc_hit.x -= spofmc
        elif h_Fb:
            if key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]:
                mc_hit.y -= spofmc

            if key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]:
                mc_hit.y += spofmc

        # To check if out of boundary
        if mc_hit.x not in range(0, 900):
            deactivate_booster()
            booster_timer = 0
            score = 0
            mixer.music.stop()
            endgame(Scoreboard)
        # To check if song is done, so game finishes
        if not mixer.music.get_busy() and run == True:
            endgame(Scoreboard)

        # To paint window and update
        game_window(mc_hit, mc, balls_h, Scoreboard, orbs, Fireballs_wanted, Fireballs_wanted_big)
        pygame.display.update()

    # to quit
    pygame.quit()



if __name__ == "__main__":
    main_page()
