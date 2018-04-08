import sys, random, pygame, time

FPS = 60
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
WORDS = []
DIFFICULTY = 3
DELAY = FPS * DIFFICULTY
putin = ""
SCORE = 0
BGCOLOR = (0, 0, 0)
WHITE = (255, 255, 255)

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
            if event.key != pygame.K_RETURN:
                if event.unicode.isalpha() or event.unicode.isdigit():
                    putin+=event.unicode
                    return(event.unicode)
            elif putin in WORDS:
                WORDS.remove(putin)
                SCORE+=1
                putin=""
                return("enter")
            else:
                putin=""
                return("enter")
                pass
            print(putin)
    return None

def get_rand_word():
    with open("words.txt") as file:
        word = slovo[random.randint(1,466544)]
        word =  word.rstrip("\n")
        WORDS.append(word)

def show_text(char):
    global putin
    if char != "enter":
        text_surf=BASICFONT.render(char,True,WHITE)
        text_rect=text_surf.get_rect()
        text_rect.center = (WINDOWWIDTH/25 + (len(putin) - 1) * 11,WINDOWHEIGHT/10 * 9.5)
        DISPLAYSURF.blit(text_surf,text_rect)

    elif char == "enter":
        DISPLAYSURF.fill(BGCOLOR)
        #zmenit potom aby to zacernilo jenom ten text
    pygame.display.update()

if __name__ == '__main__':
    main()
