import sys, random, pygame, time

FPS = 60
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
WORDS = []
WORDS_ON_SCREEN = []
DIFFICULTY = 3
DELAY = FPS * DIFFICULTY
putin = ""
SCORE = 0
BGCOLOR = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

def main():
    pygame.init()

    wait_time = 0
    global BASICFONT, DISPLAYSURF, FPSCLOCK, slovo

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 20)

    with open("words.txt") as file:
        slovo=file.readlines()

    get_rand_word()

    while True:
        draw_ui()
        wait_time += 1
        char = check_for_input()
        show_text(char)
        if wait_time == DELAY:
            get_rand_word()
            wait_time = 0
            print(WORDS)
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
                putin+=event.unicode
            elif event.key == pygame.K_RETURN and (putin in WORDS):
                WORDS.remove(putin)
                SCORE+=1
                putin=""
                print(SCORE)
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
    DISPLAYSURF.blit(text_surf,text_rect)

    if char == "backspace":
        DISPLAYSURF.fill(BGCOLOR)
        #zmenit potom aby to zacernilo jenom ten text

    if char == "enter":
        remove_text = text_rect
        remove_text[2] += WINDOWWIDTH / 1.5
        pygame.draw.rect(DISPLAYSURF, BGCOLOR, remove_text)

    pygame.display.update()

def draw_ui():
    start_pos = (0,WINDOWHEIGHT/10 * 9.2)
    end_pos = (WINDOWWIDTH,WINDOWHEIGHT/10 * 9.2)
    pygame.draw.line(DISPLAYSURF,GREEN,start_pos,end_pos)
    text_surf=BASICFONT.render("SCORE:",True,WHITE)
    text_rect=text_surf.get_rect()
    text_rect.bottomleft = (WINDOWWIDTH / 1.4,WINDOWHEIGHT / 10 * 9.8)
    text_surf2=BASICFONT.render(str(SCORE),True,WHITE)
    text_rect2=text_surf.get_rect()
    text_rect2.bottomleft = (WINDOWWIDTH / 1.18,WINDOWHEIGHT / 10 * 9.8)
    DISPLAYSURF.blit(text_surf,text_rect)
    DISPLAYSURF.blit(text_surf2,text_rect2)

class word_on_screen:

    def __init__(self, word):
        self.name = word
        self.position = [0,random.randint(0,WINDOWHEIGHT/10*9.0)]

    def word_move():
        self.position[0] += 10


if __name__ == '__main__':
    main()
