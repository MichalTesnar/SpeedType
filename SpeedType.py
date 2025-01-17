#SpeedType game
#autoři: Přemek Bělka, Michal Tešnar
#repo: https://github.com/MichalTesnar/SpeedType
#fell free to modify share and play <3

import sys, random, pygame, time

FPS = 60
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
WORDS = []
WORDS_ON_SCREEN = []
DIFFICULTY = 3
DELAY = FPS * DIFFICULTY
WORD_MOVE_TIME = FPS * 1
WORDS_POSITION = [-1*x for x in range(0,round(WORD_MOVE_TIME/6))]
putin = ""
SCORE = 0
BGCOLOR = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
LIFECOUNT = 3

def main():
    pygame.init()

    wait_time_delay = 0
    wait_time_word = 0
    global BASICFONT, DISPLAYSURF, FPSCLOCK, slovo, char, DIFFICULTY, DELAY, WORD_MOVE_TIME

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("Speed Type")
    BASICFONT = pygame.font.Font('mocfancyfont.ttf', 20)

    with open("words.txt") as file:
        slovo=file.readlines()

    get_rand_word()
    draw_start_screen("Start")

    while True:
        if check_for_input() == "enter":
            break

    DISPLAYSURF.fill(BGCOLOR)
    draw_ui()

    while True:
        refresh_score()
        check_difficulty()
        check_for_life()
        wait_time_delay += 1
        wait_time_word += 1
        char = check_for_input()
        show_text(char)
        if wait_time_delay >= DELAY:
            get_rand_word()
            wait_time_delay = 0
        for word in WORDS_ON_SCREEN:
            if word.name not in WORDS:
                word.word_remove()
        if wait_time_word == WORD_MOVE_TIME:
            for word in WORDS_ON_SCREEN:
                word.word_move()
                word.word_draw()
            wait_time_word = 0
        FPSCLOCK.tick(FPS)

def terminate():
    pygame.quit()
    sys.exit()

def check_for_input():
    global putin, SCORE
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.KEYDOWN:
            if (event.key != pygame.K_RETURN) and (event.key != pygame.K_BACKSPACE):
                if (len(putin)) <= 30:
                    putin+=event.unicode
            elif event.key == pygame.K_RETURN and (putin in WORDS):
                WORDS.remove(putin)
                SCORE+=1
                putin=""
                #print(SCORE)
                return("enter")
            elif event.key == pygame.K_BACKSPACE:
                putin = putin[0:len(putin) - 1]
                return("backspace")
            else:
                putin=""
                return("enter")
                pass
    return None

def get_rand_word():
    with open("words.txt") as file:
        word = slovo[random.randint(1,466544)]
        word =  word.rstrip("\n")
        WORDS.append(word)
        WORDS_ON_SCREEN.append(word_on_screen(word))

def show_text(char):
    global putin
    text_surf = BASICFONT.render(putin,True,WHITE)
    text_rect = text_surf.get_rect()
    text_rect.bottomleft = (WINDOWWIDTH / 50,WINDOWHEIGHT / 10 * 9.8)
    pygame.draw.rect(DISPLAYSURF, BGCOLOR, text_rect)
    DISPLAYSURF.blit(text_surf,text_rect)

    if char == "backspace":
        remove_text = text_rect
        remove_text[2] = WINDOWWIDTH / 1.5
        pygame.draw.rect(DISPLAYSURF, BGCOLOR, remove_text)
        DISPLAYSURF.blit(text_surf,text_rect)

    if char == "enter":
        remove_text = text_rect
        remove_text[2] = WINDOWWIDTH / 1.5
        pygame.draw.rect(DISPLAYSURF, BGCOLOR, remove_text)

    pygame.display.update()

def draw_ui():
    start_pos = (0,WINDOWHEIGHT/10 * 9.2)
    end_pos = (WINDOWWIDTH,WINDOWHEIGHT/10 * 9.2)
    pygame.draw.line(DISPLAYSURF,GREEN,start_pos,end_pos)
    text_surf=BASICFONT.render("SCORE:",True,WHITE)
    text_rect=text_surf.get_rect()
    text_rect.bottomleft = (WINDOWWIDTH / 1.4,WINDOWHEIGHT / 10 * 9.8)
    DISPLAYSURF.blit(text_surf,text_rect)

def refresh_score():
    text_surf=BASICFONT.render(str(SCORE),True,WHITE)
    text_rect=text_surf.get_rect()
    text_rect.bottomleft = (WINDOWWIDTH / 1.18,WINDOWHEIGHT / 10 * 9.8)
    pygame.draw.rect(DISPLAYSURF, BGCOLOR, text_rect)
    DISPLAYSURF.blit(text_surf,text_rect)

def check_for_life():
    global LIFECOUNT
    position = [round(WINDOWWIDTH / 1.1),round(WINDOWHEIGHT / 10 * 9.53)]
    rectangle = pygame.Rect(round(WINDOWWIDTH / 1.14),round(WINDOWHEIGHT / 10 * 9.3),WINDOWWIDTH,WINDOWHEIGHT)
    DISPLAYSURF.fill(BGCOLOR,rectangle)
    for i in range (LIFECOUNT):
        pygame.draw.circle(DISPLAYSURF,RED, position, 5)
        position[0] += 15

def game_over():
    global WORDS, WORDS_ON_SCREEN, LIFECOUNT
    DISPLAYSURF.fill(BGCOLOR)
    draw_start_screen("Game Over")
    pygame.display.update()
    WORDS = []
    WORDS_ON_SCREEN = []
    LIFECOUNT = 3
    while True:
        if check_for_input() == "enter":
            LIFECOUNT = 3
            main()

def draw_start_screen(text):
    global SCORE
    text_surf = BASICFONT.render(text,True,GREEN)
    text_rect = text_surf.get_rect()
    text_rect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2 - 30)
    DISPLAYSURF.blit(text_surf,text_rect)

    if text == "Start":
        text_surf = BASICFONT.render("To proceed, press enter!",True,GREEN)
        text_rect = text_surf.get_rect()
        text_rect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(text_surf,text_rect)
    else:
        text_surf = BASICFONT.render(text,True,RED)
        text_rect = text_surf.get_rect()
        text_rect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2-30)
        DISPLAYSURF.blit(text_surf,text_rect)
        text_surf = BASICFONT.render("To restart, press enter!",True,GREEN)
        text_rect = text_surf.get_rect()
        text_rect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(text_surf,text_rect)
        text_surf = BASICFONT.render("Score: "+str(SCORE),True,GREEN)
        text_rect = text_surf.get_rect()
        text_rect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2+30)
        DISPLAYSURF.blit(text_surf,text_rect)
        SCORE = 0

    pygame.display.update()


def check_difficulty():
    global SCORE, DIFFICULTY, DELAY, WORD_MOVE_TIME
    if DIFFICULTY <= 1.25:
        pass

    else:
        DIFFICULTY = 3 - SCORE / 20
        DELAY = int(FPS * DIFFICULTY)

    if SCORE >= 75:
        WORD_MOVE_TIME = FPS * 0.9

    if SCORE >= 100:
        WORD_MOVE_TIME = FPS * 0.8



class word_on_screen:

    def __init__(self, word):
        global name, position, WORDS_POSITION
        self.name = word
        self.position = [0,round(random.randint(1,WINDOWHEIGHT-46)/23)*23]
        while self.position[1] in WORDS_POSITION:
            self.position[1] = round(random.randint(1,WINDOWHEIGHT-46)/23)*23
        WORDS_POSITION.pop()
        WORDS_POSITION.insert(0,self.position[1])
        #print(WORDS_POSITION)

    def word_move(self):
        self.position[0] += WINDOWWIDTH / 64

    def word_draw(self):
        global LIFECOUNT
        color = [GREEN, YELLOW, RED]
        text_surf = BASICFONT.render(self.name,True,WHITE)
        text_rect = text_surf.get_rect()
        delete_rect = text_surf.get_rect()
        text_rect.bottomleft = tuple(self.position)
        delete_rect.bottomleft = tuple(self.position)
        delete_rect.left -= WINDOWWIDTH / 64
        pygame.draw.rect(DISPLAYSURF, BGCOLOR, delete_rect)
        if text_rect.center[0] < 1/3 * WINDOWWIDTH:
            text_surf = BASICFONT.render(self.name,True,color[0])
        if text_rect.center[0] > 1/3 * WINDOWWIDTH:
            text_surf = BASICFONT.render(self.name,True,color[1])
        if text_rect.center[0] > 2/3 * WINDOWWIDTH:
            text_surf = BASICFONT.render(self.name,True,color[2])
        DISPLAYSURF.blit(text_surf,text_rect)
        if text_rect.right >= WINDOWWIDTH:
            LIFECOUNT-=1
            self.word_remove()
            if LIFECOUNT == 0:
                game_over()

    def word_remove(self):
        WORDS_ON_SCREEN.remove(self)
        text_surf = BASICFONT.render(self.name,True,WHITE)
        delete_rect = text_surf.get_rect()
        delete_rect.bottomleft = tuple(self.position)
        pygame.draw.rect(DISPLAYSURF, BGCOLOR, delete_rect)




if __name__ == '__main__':
    main()
