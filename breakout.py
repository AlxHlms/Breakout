import pygame
from pygame.locals import*

pygame.init()

size = width, height = 510, 510
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))

ImageOnScreen1 = pygame.Rect(4, 155, 10, 10)
ImageOnScreen2 = pygame.Rect(69, 150, 10, 10)
ImageOnScreen3 = pygame.Rect(70, 200, 10, 10)
ImageOnScreen4 = pygame.Rect(68, 250, 10, 10)
ImageOnScreen5 = pygame.Rect(69, 150, 10, 10)

theendSound = pygame.mixer.Sound('theendsound.wav')
winSound = pygame.mixer.Sound('winner.wav')

thanksImage = pygame.image.load('thanks.png')
gameoverImage = pygame.image.load('gameovercard.png')
pauseImage = pygame.image.load('pause.png')
spaceImage = pygame.image.load('press_space.png')
introImage = pygame.image.load('intro.png')

clock = pygame.time.Clock()

pause = False


def lose():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(theendSound)
    coords = []
    runx, runy = 0, 0
    screen.fill((0, 0, 0))
    screen.blit(gameoverImage, ImageOnScreen1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()

        pygame.display.update()
        clock.tick(50)
        
def win():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(winSound)
    runx, runy = 0, 0
    screen.fill((255, 255, 255))
    screen.blit(thanksImage, ImageOnScreen2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()

        pygame.display.update()
        clock.tick(50)


def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False

def paused():
    pygame.mixer.music.pause()

    

    while pause:
        screen.blit(pauseImage, ImageOnScreen3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    unpause()

        pygame.display.update()
        clock.tick(50)

def intro():
    pygame.mixer.music.load('intromusic.wav')
    pygame.mixer.music.play(-1, 0.0)
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()
                
        screen.fill((0, 0, 0))
        screen.blit(spaceImage, ImageOnScreen4)
        screen.blit(introImage, ImageOnScreen5)

        pygame.display.update()
        clock.tick(50)

def game():
    global pause
    
    pygame.mixer.music.load('background.wav')
    pygame.mixer.music.play(-1, 0.0)
    musicPlaying = True
    
    posx = 250
    posy = 250
    runx = 1
    runy = 3
    constant_x, constant_y = 220, 500
    left_number = 0
    right_number = 0
    kleft_flag = False
    kright_flag = False

    hitSound = pygame.mixer.Sound('hitbrick.wav')

    gameExit = False
    
    pygame.draw.rect(screen, pygame.Color(255, 255, 255),
                     (constant_x, constant_y, 60, 5), 0)
    coords = [((10, 10), (40, 20)), ((60, 10), (40, 20)), ((110, 10), (40, 20)),
              ((160, 10), (40, 20)), ((210, 10), (40, 20)), ((260, 10),(40, 20)),
              ((310, 10), (40, 20)), ((360, 10), (40, 20)), ((410, 10), (40, 20)),
              ((460, 10), (40, 20)),
              ((10, 40), (40, 20)), ((60, 40), (40, 20)), ((110, 40), (40, 20)),
              ((160, 40), (40, 20)), ((210, 40), (40, 20)), ((260, 40),(40, 20)),
              ((310, 40), (40, 20)), ((360, 40), (40, 20)), ((410, 40), (40, 20)),
              ((460, 40), (40, 20)),
              ((10, 70), (40, 20)), ((60, 70), (40, 20)), ((110, 70), (40, 20)),
              ((160, 70), (40, 20)), ((210, 70), (40, 20)), ((260, 70),(40, 20)),
              ((310, 70), (40, 20)), ((360, 70), (40, 20)), ((410, 70), (40, 20)),
              ((460, 70), (40, 20)),
              ((10, 100), (40, 20)), ((60, 100), (40, 20)), ((110, 100), (40, 20)),
              ((160, 100), (40, 20)), ((210, 100), (40, 20)), ((260, 100),(40, 20)),
              ((310, 100), (40, 20)), ((360, 100), (40, 20)), ((410, 100), (40, 20)),
              ((460, 100), (40, 20))]
 
    while not gameExit:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()
                if event.key == pygame.K_LEFT:
                    if constant_x > 0:
                        constant_x -= 25
                        kleft_flag = True
                if event.key == pygame.K_RIGHT:
                    if constant_x < 460:
                        constant_x += 25
                        kright_flag = True
                if event.key == K_m:
                    if musicPlaying:
                        pygame.mixer.music.stop()
                    else:
                        pygame.mixer.music.play(-1, 0.0)
                    musicPlaying = not musicPlaying
                if event.key == pygame.K_p:
                    pause = True
                    paused()

                    
        if kleft_flag == True:
            left_number += 1

        if left_number == 15:
            left_number = 0
            kleft_flag = False
        
        if kright_flag == True:
            right_number += 1
        
        if right_number == 15:
            right_number = 0
            kright_flag = False
        
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, pygame.Color(255, 255, 255),
                         (constant_x, constant_y, 60, 5), 0)
        posx += runx
        posy += runy
                    
    
    
        if posy >= 495:
            if constant_x < posx < constant_x + 60:
                runy = -3
            if left_number > 0:
                runx = -3
            if right_number > 0:
                runx = 3
            if left_number > 5:
                runx = -2
            if right_number > 5:
                runx = 2
            if left_number > 10:
                runx = -1
            if right_number > 10:
                runx = 1


        if posy < 5:
            runy = -runy
        if posx < 5:
            runx = -runx
        if posx > 500:
            runx = -runx
        for coord in coords:
            if coord[0][0] < posx < (coord[0][0] + coord[1][0]):
                if coord[0][1] < posy < (coord[0][1] + coord[1][1]):
                    if musicPlaying:
                        hitSound.play()
                    del coords[coords.index(coord)]
                    runy = -runy

            pygame.draw.rect(screen, pygame.Color(255, 150, 150), coord)

        if coords == []:
            win()
                
        pygame.draw.circle(screen, (255, 150, 255), (posx, posy), 10)

        if posy > 520:
            lose()
        
        pygame.display.update()
        clock.tick(50)
        

intro()
game()

pygame.quit()
