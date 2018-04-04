import sys, random, pygame, time


FPS = 10
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
WORDS = []
DIFFICULTY = 3
DELAY = FPS * DIFFICULTY * 10000
putin = ""

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
        check_for_quit()
        check_for_input()
        if wait_time == DELAY:
            get_rand_word()
            wait_time = 0
            print(WORDS)
        FPSCLOCK.tick()
        
        
    
def terminate():
    pygame.quit()
    sys.exit()

def check_for_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()

def check_for_input():
    global putin
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key != pygame.K_KP_ENTER:
                print(putin)
                putin+=event.unicode
            else:
                print(event.key)
                pass
            #neco sem chcem dopsat :D

def get_rand_word():
    with open("words.txt") as file:
        word = slovo[random.randint(1,466544)]
        word =  word.rstrip("\n")
        WORDS.append(word)
        print(WORDS)
    
                
if __name__ == '__main__':
    main()
