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
        
        if self.x < 0:
            self.rect.x = WINDOWWIDTH - 3
            self.x = WINDOWWIDTH - 3
        if self.y < 0:
            self.rect.y = WINDOWHEIGHT - 3
            self.y = WINDOWHEIGHT - 3
        if self.x > WINDOWWIDTH:
            self.rect.x = 3
            self.x = 3
        if self.y > WINDOWHEIGHT:
            self.rect.y = 3
            self.y = 3
        
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
    global algae
    global toothfish
    global penguin
    global whale
    global player_foodlevel
    global player_image
    global player_height
    global player_width
    
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    STANDARDFONT = pygame.font.Font('freesansbold.ttf', 20)
    algae = pygame.image.load("happy-green-algae-md.png")
    toothfish = pygame.image.load("cod.png")
    penguin = pygame.image.load("penguin_cute.png")
    whale = pygame.image.load("rg_1_24_cartoon_whale-1979px.png")
    
    player_foodlevel = 1
    player_image = toothfish
    player_height = 70
    player_width = 31
    
    map1 = pygame.image.load("General map.gif")
    map2 = pygame.image.load("Specific map.gif")
    
    pygame.display.set_caption('Tundra Fun')
    
    showStartScreen()
    while True:
        
        winner = runGame()
        showEndScreen(winner)
        
def showStartScreen():
    
     mainFont = pygame.font.Font('freesansbold.ttf', 80)
     title = mainFont.render('Tundra Fun!!!',True,WHITE,GREEN)
     instructionFont = STANDARDFONT
     intro1 = instructionFont.render("Welcome to the Antarctic Tundra!", True,WHITE,GREEN)
     author = instructionFont.render("By Justin Zeitlinger, Ohm Nabar, and Jeemin Park", True, WHITE, BLUE)
     intro2 = instructionFont.render("This biome is located on the Antarctic Peninsula,", True,WHITE,GREEN)
     intro3 = instructionFont.render("South Georgia and the Falkland Islands, and the surrounding Southern Ocean.", True,WHITE,GREEN)
     intro4 = instructionFont.render("Despite the extreme cold and dryness found here, a small yet diverse amount of life exists.", True,WHITE,GREEN)
     intro5 = instructionFont.render("Many of the organisms found here are unique to the Antarctic tundra.", True,WHITE,GREEN)
     intro6 = instructionFont.render("All of them, however, are specially adapted to deal with the harsh climate.", True,WHITE,GREEN)
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
        titleRect.center = (WINDOWWIDTH/2-50,WINDOWHEIGHT/2-50)
        DISPLAYSURF.blit(title, titleRect)
        authorRect = author.get_rect()
        authorRect.center = (WINDOWWIDTH/2,WINDOWHEIGHT/2)
        DISPLAYSURF.blit(author, authorRect)
        intro1Rect = intro1.get_rect()
        intro1Rect.center = (WINDOWWIDTH/2, WINDOWHEIGHT/2+20)
        DISPLAYSURF.blit(intro1,intro1Rect)
        intro2Rect = intro2.get_rect()
        intro2Rect.center = (WINDOWWIDTH/2, WINDOWHEIGHT/2+40)
        DISPLAYSURF.blit(intro2,intro2Rect)
        intro3Rect = intro3.get_rect()
        intro3Rect.center = (WINDOWWIDTH/2, WINDOWHEIGHT/2+60)
        DISPLAYSURF.blit(intro3,intro3Rect)
        intro4Rect = intro4.get_rect()
        intro4Rect.center = (WINDOWWIDTH/2, WINDOWHEIGHT/2+80)
        DISPLAYSURF.blit(intro4,intro4Rect)
        intro5Rect = intro5.get_rect()
        intro5Rect.center = (WINDOWWIDTH/2, WINDOWHEIGHT/2+100)
        DISPLAYSURF.blit(intro5,intro5Rect)
        intro6Rect = intro6.get_rect()
        intro6Rect.center = (WINDOWWIDTH/2, WINDOWHEIGHT/2+120)
        DISPLAYSURF.blit(intro6,intro6Rect)
      
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
        
    player = Player(playerx, playery, player_image, player_foodlevel, player_width, player_height)
    
    plant1 = ai_Producer(500, 500, algae, 0, 35, 32)
    plant2 = ai_Producer(200, 200, algae, 0, 35, 32)
    plant3 = ai_Producer(300, 450, algae, 0, 35, 32)
    plant4 = ai_Producer(600, 475, algae, 0, 35, 32)
    plant5 = ai_Producer(100, 300, algae, 0, 35, 32)
    
    consumer1 = ai_Consumer(500, 200, toothfish, 1, LEFT, 70, 31)
    consumer2 = ai_Consumer(200, 175, penguin, 2, RIGHT, 70, 90)
    consumer3 = ai_Consumer(400, 400, whale, 3, RIGHT, 100, 54)
    
    ai_consumer_list = [consumer1,consumer2,consumer3]
    ai_producer_list = [plant1,plant2,plant3, plant4,plant5]
    
    while True:
        
        player.move()
        
        DISPLAYSURF.fill(BLUE)
        
        ai_consumer_pos = 0
        ai_producer_pos = 0
        
        player.draw()
        for ai in ai_consumer_list:
            ai.move()
            ai.draw()
            if player.rect.colliderect(ai.rect) and ai.food_level > player.food_level:
                return True
            elif player.rect.colliderect(ai.rect) and ai.food_level < player.food_level:
                print(str(player.food_level) + " eats " + str(ai.food_level))
                del ai_consumer_list[ai_consumer_pos]
            ai_consumer_pos += 1
        for ai in ai_producer_list:
            ai.draw()
            if player.rect.colliderect(ai.rect) and ai.food_level < player.food_level:
                del ai_producer_list[ai_producer_pos]
            ai_producer_pos += 1
        pyramid = pygame.image.load("tundrafoodpyramid.png")
        DISPLAYSURF.blit(pyramid, (0, 0))
        
        if len(ai_producer_list) == 0:
            return True
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
    
def drawPressKeyMsg():
    pressKey = STANDARDFONT.render('Press Space to Play Again',True,GREEN)
    pressKeyRect = pressKey.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 300, WINDOWHEIGHT - 30)   
    DISPLAYSURF.blit(pressKey, pressKeyRect)    
def showEndScreen(winner):
    gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
    if winner:
        gameSurf = gameOverFont.render('Play', True, RED)
        overSurf = gameOverFont.render('Again?', True, RED)
        gameRect = gameSurf.get_rect()
        overRect = overSurf.get_rect()
        gameRect.midtop = (WINDOWWIDTH / 2, 10)
        overRect.midtop = (WINDOWWIDTH / 2, gameRect.height + 10 + 25)
        DISPLAYSURF.blit(gameSurf, gameRect)
        DISPLAYSURF.blit(overSurf, overRect)
    else:
        gameSurf = gameOverFont.render('You', True, RED)
        overSurf = gameOverFont.render('Won!', True, RED)
        gameRect = gameSurf.get_rect()
        overRect = overSurf.get_rect()
        gameRect.midtop = (WINDOWWIDTH / 2, 10)
        overRect.midtop = (WINDOWWIDTH / 2, gameRect.height + 10 + 25)
        DISPLAYSURF.blit(gameSurf, gameRect)
        DISPLAYSURF.blit(overSurf, overRect)
        pygame.display.update()
        pygame.time.wait(2000)
        terminate()
    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(100)
    checkForKeyPress()  
    while True:
        if checkForKeyPress() == K_SPACE:
            pygame.event.get() # clear event queue
            return
    

if __name__ == '__main__':   
    main()