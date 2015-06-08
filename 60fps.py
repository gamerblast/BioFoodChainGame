import random, pygame, sys
from pygame.locals import *   

# fps and screen resolution    
FPS = 60
WINDOWWIDTH = 960
WINDOWHEIGHT = 540 

# colors
WHITE = (255,255,255)
RED =   (255, 0, 0)
GREEN = (0, 255, 0)
ORANGE =(255, 128, 0)
GRAY = (50,50,50)
BLACK = (0,0,0)
DARKRED = (155,0,0)
BLUE = (0, 0, 255)

LEFT = 'left'
RIGHT = 'right'
class Player(object):
    def __init__(self, startx, starty, image, food_level, width, height):
        self.x = startx
        self.y = starty
        self.image = image
        self.food_level = food_level
        self.width = width
        self.height = height
        self.rect = pygame.Rect(startx, starty, width, height)
        self.playerxmove = 0
        self.playerymove = 0
        
    def move(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if(event.key == K_UP):
                    self.playerymove = -3
                if(event.key == K_DOWN):
                    self.playerymove = 3
                if(event.key == K_LEFT):
                    self.playerxmove = -3
                if(event.key == K_RIGHT):
                    self.playerxmove = 3
                if(event.key == K_ESCAPE):
                    terminate()
            elif event.type == KEYUP:
                if(event.key == K_UP):
                    self.playerymove = 0
                if(event.key == K_DOWN):
                    self.playerymove = 0
                if(event.key == K_LEFT):
                    self.playerxmove = 0
                if(event.key == K_RIGHT):
                    self.playerxmove = 0
                if(event.key == K_ESCAPE):
                    terminate()
        self.rect.x += self.playerxmove
        self.x += self.playerxmove
        self.rect.y += self.playerymove
        self.y += self.playerymove
        
    def draw(self):
        DISPLAYSURF.blit(self.image, (self.x, self.y))
class ai_Consumer(object):
    
    def __init__(self, startx, starty, image, food_level, movement, width, height):
        self.food_level = food_level
        self.movement = movement
        self.x = startx
        self.y = starty
        self.image = image
        self.width = width
        self.height = height
        self.rect = pygame.Rect(startx, starty, width, height)
    
    def draw(self):
        DISPLAYSURF.blit(self.image, (self.x, self.y))
        
    def move(self):
        if(self.movement == RIGHT and self.x < WINDOWWIDTH):
            self.rect.x += 3
            self.x += 3
        elif(self.movement == RIGHT and self.x >= WINDOWWIDTH):
            self.movement = LEFT
            self.rect.x -= 3
            self.x -= 3
        elif(self.movement == LEFT and self.x > 0):
            self.rect.x -= 3
            self.x -= 3
        else:
            self.movement = RIGHT
            self.rect.x += 3
            self.x += 3
        
class ai_Producer(object):
    def __init__(self, startx, starty, image, food_level, width, height):
        self.image = image
        self.food_level = food_level
        self.x = startx
        self.y = starty
        self.rect = pygame.Rect(startx, starty, width, height)
    def draw(self):
        DISPLAYSURF.blit(self.image, (self.x, self.y))

def main():
    global FPSCLOCK
    global DISPLAYSURF
    global STANDARDFONT
    global toothfish
    
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    STANDARDFONT = pygame.font.Font('freesansbold.ttf', 20)
    toothfish = pygame.image.load("cod.png")
    map1 = pygame.image.load("General map.gif")
    map2 = pygame.image.load("Specific map.gif")
    
    pygame.display.set_caption('Tundra Fun')
    
    
    while True:
        showStartScreen()
        winner = runGame()
        showEndScreen(winner)
        
def showStartScreen():
    
     mainFont = pygame.font.Font('freesansbold.ttf', 80)
     title = mainFont.render('Tundra Fun!!!',True,WHITE,GREEN)
     instructionFont = STANDARDFONT
     while True:
        DISPLAYSURF.fill(BLACK)
        map1 = pygame.image.load("General map.gif")
        map2 = pygame.image.load("Specific map.gif")
        map1Rect = map1.get_rect()
        map2Rect = map2.get_rect()
        map1Rect.topleft = (0,30)
        DISPLAYSURF.blit(map1, map1Rect)
        map2Rect.topleft = (WINDOWWIDTH/2,30)
        DISPLAYSURF.blit(map2, map2Rect)
        
        titleRect = title.get_rect()
        titleRect.center = (WINDOWWIDTH/2,WINDOWHEIGHT/2)
        DISPLAYSURF.blit(title, titleRect)
      
        startGame()
        key_press = checkForKeyPress()
        
        if key_press == K_SPACE:
            pygame.event.get()
            print("starting game")
            return 1
        pygame.display.update()
        FPSCLOCK.tick(FPS)
    
def runGame():
    playerx = WINDOWWIDTH / 2
    playery = WINDOWHEIGHT /2
    playerfoodlevel = 1
    
    player = Player(playerx, playery, toothfish, 70, 31, playerfoodlevel)
    
    plant1 = ai_Producer(500, 500, toothfish, 0, 70, 31)
    consumer1 = ai_Consumer(200, 200, toothfish, 0, RIGHT, 70, 31)
    ai_consumer_list = [consumer1]
    ai_producer_list = [plant1]
    
    while True:
        player.move()
        if player.x < 0:
            player.x = WINDOWWIDTH - 3
        if player.y < 0:
            player.y = WINDOWHEIGHT - 3
        if player.x > WINDOWWIDTH:
            player.x = 3
        if player.y > WINDOWHEIGHT:
            player.y = 3
        
        DISPLAYSURF.fill(BLUE)
        
        ai_consumer_pos = 0
        ai_producer_pos = 0
        
        player.draw()
        for ai in ai_consumer_list:
            ai.move()
            ai.draw()
            if player.rect.colliderect(ai.rect) and ai.food_level < player.food_level:
                del ai_consumer_list[ai_consumer_pos]
            ai_consumer_pos += 1
        for ai in ai_producer_list:
            ai.draw()
            if player.rect.colliderect(ai.rect) and ai.food_level < player.food_level:
                del ai_producer_list[ai_producer_pos]
            ai_producer_pos += 1
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)
    return(0)
    
def startGame():
    pressKey = STANDARDFONT.render('Press Space to start',True,GREEN)
    pressKeyRect = pressKey.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH -    250, WINDOWHEIGHT - 30)   
    DISPLAYSURF.blit(pressKey, pressKeyRect)
    
        
def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()
    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
        print("terminated")
    return keyUpEvents[0].key

def drawPlayer(x, y):
    DISPLAYSURF.blit(toothfish, (x, y))

def terminate():
    pygame.quit()
    sys.exit()
    
def showEndScreen(winner):
    print("bai")  
    

if __name__ == '__main__':   
    main()