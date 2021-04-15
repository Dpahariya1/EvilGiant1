import pygame
import sys
pygame.init()

WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 700
FPS = 25
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
ADD_NEW_FLAME_RATE = 25
cactus_img = pygame.image.load('cactus_bricks.png')
cactus_img_rect = cactus_img.get_rect()
cactus_img_rect.left = 0
fire_img = pygame.image.load('fire_bricks.png')
fire_img_rect = fire_img.get_rect()
fire_img_rect.left = 0
CLOCK = pygame.time.Clock()
font = pygame.font.SysFont('algerian', 20)

canvas = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('EVILGIANT')

class Topscore:
    def __init__(self):
        self.high_score = 0
    def top_score(self, score):
        if score > self.high_score:
            self.high_score = score
        return self.high_score

topscore = Topscore()


class Dragon:
    dragon_velocity = 10

    def __init__(self):
        self.dragon_img = pygame.image.load('evil9.jpg')
        self.dragon_img_rect = self.dragon_img.get_rect()
        self.dragon_img_rect.width -= 10
        self.dragon_img_rect.height -= 10
        self.dragon_img_rect.top = WINDOW_HEIGHT/2
        self.dragon_img_rect.right = WINDOW_WIDTH
        self.up = True
        self.down = False

    def update(self):
        canvas.blit(self.dragon_img, self.dragon_img_rect)
        if self.dragon_img_rect.top <= cactus_img_rect.bottom:
            self.up = False
            self.down = True
        elif self.dragon_img_rect.bottom >= fire_img_rect.top:
            self.up = True
            self.down = False

        if self.up:
            self.dragon_img_rect.top -= self.dragon_velocity
        elif self.down:
            self.dragon_img_rect.top += self.dragon_velocity


class Flames:
    flames_velocity = 15

    def __init__(self):
        self.flames = pygame.image.load('fireball.png')
        self.flames_img = pygame.transform.scale(self.flames, (20, 20))
        self.flames_img_rect = self.flames_img.get_rect()
        self.flames_img_rect.right = dragon.dragon_img_rect.left
        self.flames_img_rect.top = dragon.dragon_img_rect.top + 30


    def update(self):
        canvas.blit(self.flames_img, self.flames_img_rect)

        if self.flames_img_rect.left > 0:
            self.flames_img_rect.left -= self.flames_velocity


class Evil:
    velocity = 15

    def __init__(self):
        self.evil_img = pygame.image.load('evil8.jpg')
        self.evil_img_rect = self.evil_img.get_rect()
        self.evil_img_rect.left = 200
        self.evil_img_rect.top = WINDOW_HEIGHT/2 - 100
        self.down = True
        self.up = False


    def update(self):
        canvas.blit(self.evil_img, self.evil_img_rect)
        if self.evil_img_rect.top <= cactus_img_rect.bottom:
            game_over()
            if SCORE > self.evil_score:
                self.evil_score = SCORE
        if self.evil_img_rect.bottom >= fire_img_rect.top:
            game_over()
            if SCORE > self.evil_score:
                self.evil_score = SCORE
        if self.up:
            self.evil_img_rect.top -= 10
        if self.down:
            self.evil_img_rect.bottom += 10

def game_over():


    pygame.mixer.music.stop()
    music = pygame.mixer.Sound('hit.wav')
    music.play()
    topscore.top_score(SCORE)
    smallfont4 = pygame.font.SysFont('algerian',100)
    text4 = smallfont4.render('EVIL GIANT' , True , GREEN)
    canvas.blit(text4 , (WINDOW_WIDTH/500+300,WINDOW_HEIGHT/3))
    smallfont5 = pygame.font.SysFont('algerian',60)
    text5 = smallfont5.render('PRESS ANY KEY TO RESTART' , True , GREEN)
    canvas.blit(text5 , (WINDOW_WIDTH/500+200,WINDOW_HEIGHT/2))
    #game_over_img = pygame.image.load('end.png')
    #game_over_img_rect = game_over_img.get_rect()
    #game_over_img_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    #canvas.blit(game_over_img, game_over_img_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                music.stop()
                game_loop()
        pygame.display.update()



    # updates the frames of the game
pygame.display.update()
def start_game():
    canvas.fill(BLACK)
    smallfont4 = pygame.font.SysFont('algerian',100)
    text4 = smallfont4.render('EVIL GIANT' , True , GREEN)
    canvas.blit(text4 , (WINDOW_WIDTH/500+300,WINDOW_HEIGHT/3))
    smallfont5 = pygame.font.SysFont('algerian',60)
    text5 = smallfont5.render('PRESS ANY KEY TO START' , True , GREEN)
    canvas.blit(text5 , (WINDOW_WIDTH/500+200,WINDOW_HEIGHT/2))
    #start_img = pygame.image.load('space.jpg')
    #start_img = pygame.transform.scale(start_img, (WINDOW_WIDTH, WINDOW_HEIGHT)).convert_alpha()
    #start_img_rect = start_img.get_rect()
    #canvas.blit(text4 , (WINDOW_WIDTH/500+240,WINDOW_HEIGHT/3))


    #start_img_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    #canvas.blit(start_img ,start_img_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                game_loop()
        pygame.display.update()


def check_level(SCORE):
    global LEVEL
    if SCORE in range(0, 20):
        cactus_img_rect.bottom = 50
        fire_img_rect.top = WINDOW_HEIGHT - 50
        LEVEL = 1
    elif SCORE in range(20, 60):
        cactus_img_rect.bottom = 70
        fire_img_rect.top = WINDOW_HEIGHT - 70
        LEVEL = 2
    elif SCORE in range(60, 80):
        cactus_img_rect.bottom = 120
        fire_img_rect.top = WINDOW_HEIGHT - 120
        LEVEL = 3
    elif SCORE > 80:
        cactus_img_rect.bottom = 200
        fire_img_rect.top = WINDOW_HEIGHT - 200
        LEVEL = 4





def game_loop():
    while True:
        global dragon
        dragon = Dragon()
        flames = Flames()
        evil = Evil()
        add_new_flame_counter = 0
        global SCORE
        SCORE = 0
        global  HIGH_SCORE
        flames_list = []
        pygame.mixer.music.load('theme.mp3')
        pygame.mixer.music.play(-1, 0.0)
        while True:
            canvas.fill(BLACK)
            check_level(SCORE)
            dragon.update()
            add_new_flame_counter += 1

            if add_new_flame_counter == ADD_NEW_FLAME_RATE:
                add_new_flame_counter = 0
                new_flame = Flames()
                flames_list.append(new_flame)
            for f in flames_list:
                if f.flames_img_rect.left <= 0:
                    flames_list.remove(f)
                    SCORE += 1
                f.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        evil.up = True
                        evil.down = False
                    elif event.key == pygame.K_DOWN:
                        evil.down = True
                        evil.up = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        evil.up = False
                        evil.down = True
                    elif event.key == pygame.K_DOWN:
                        evil.down = True
                        evil.up = False

            #smallfont4 = pygame.font.SysFont('algerian',100)
            #text4 = smallfont4.render('EVIL GIANT' , True , GREEN)
            #canvas.blit(text4 , (WINDOW_WIDTH/500+240,WINDOW_HEIGHT/3))
            #start_img = pygame.image.load('space.jpg')
            #start_img = pygame.transform.scale(start_img, (WINDOW_WIDTH, WINDOW_HEIGHT)).convert_alpha()
            #start_img_rect = start_img.get_rect()


            score_font = font.render('Score:'+str(SCORE), True, GREEN)
            score_font_rect = score_font.get_rect()
            score_font_rect.center = (200, cactus_img_rect.bottom + score_font_rect.height/2)
            canvas.blit(score_font, score_font_rect)

            level_font = font.render('Level:'+str(LEVEL), True, GREEN)
            level_font_rect = level_font.get_rect()
            level_font_rect.center = (500, cactus_img_rect.bottom + score_font_rect.height/2)
            canvas.blit(level_font, level_font_rect)

            top_score_font = font.render('Top Score:'+str(topscore.high_score),True,GREEN)
            top_score_font_rect = top_score_font.get_rect()
            top_score_font_rect.center = (800, cactus_img_rect.bottom + score_font_rect.height/2)
            canvas.blit(top_score_font, top_score_font_rect)

            canvas.blit(cactus_img, cactus_img_rect)
            canvas.blit(fire_img, fire_img_rect)
            evil.update()
            for f in flames_list:
                if f.flames_img_rect.colliderect(evil.evil_img_rect):
                    game_over()
                    if SCORE > evil.evil_score:
                        evil.evil_score = SCORE
            pygame.display.update()
            CLOCK.tick(FPS)


start_game()
