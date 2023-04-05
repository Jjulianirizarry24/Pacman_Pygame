import pygame
from spritesheet import SpriteSheet

pygame.init()



# Code to initialize screen
width = 800
height = 750
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('PACMAN')
black = (0,0,0)
white = (255,255,255)

# Ingame timer
clock = pygame.time.Clock()
crashed = False


# Initialize spriteSheet

spriteSheetFile = SpriteSheet('spriteSheet.png')

# Drawing Map

def mapCreation():
    mapMaze = pygame.image.load('map1.png')
    mapMaze = pygame.transform.scale(mapMaze,(width,height*0.85))
    screen.blit(mapMaze, (0,height*0.1))

# Player Position
playerPositionX = 0
playerPositionY = 0
    
# Creating pacman class

#def pacman(x,y):
index = 0
    
pacSprite1 = spriteSheetFile.getSprite(35,16,24,32,30)
pacSprite2 = spriteSheetFile.getSprite(66,16,30,32,30)
pacSprite3 = spriteSheetFile.getSprite(98,16,34,32,30)
    
pacSprite = [pacSprite1,pacSprite2,pacSprite3]
    


# Drawing Ghost
ghostSprite = pygame.image.load('redGhost.png')
ghostSprite = pygame.transform.scale(ghostSprite,(25,25))

def ghost(x,y):
    screen.blit(ghostSprite, (x,y))
    
ghostPositionX = 80
ghostPositionY = 80
    



while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                index = (index+1) % len(pacSprite)
                
                
            
        
            
        #if event.key == pygame.K_SPACE:
            #index = (index+1)%len 

    # Create the game
    screen.fill(black)
    #pacman(playerPositionX,playerPositionY)
    
    screen.blit(pacSprite[index], (playerPositionX,playerPositionY))
    ghost(ghostPositionX,ghostPositionY)
    mapCreation()
    
    pygame.display.update()
    clock.tick(30)

    
    
    # Player Input
    
    keyInput = pygame.key.get_pressed()
    if keyInput[pygame.K_LEFT]:
        playerPositionX -= 2
    if keyInput[pygame.K_UP]:
        playerPositionY -= 2
    if keyInput[pygame.K_RIGHT]:
        playerPositionX += 2
    if keyInput[pygame.K_DOWN]:
        playerPositionY += 2
    
    # animation
    if clock.tick() % 600 == 0:   
        index +=1
        
        if index >= len(pacSprite):
            index = 0
             
pygame.quit()
quit()






# Code to close tab
#tab = True
#
#while tab:
#
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            tab = False
#
#pygame.quit()
    
    