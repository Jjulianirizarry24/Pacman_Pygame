import pygame

pygame.init()



# Code to initialize screen
width = 800
height = 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('PACMAN')
black = (0,0,0)
white = (255,255,255)

# Ingame timer
clock = pygame.time.Clock()
crashed = False



# Drawing Player
pacSprite = pygame.image.load('pacman.png')
pacSprite = pygame.transform.scale(pacSprite,(20,20))
    
    # Player Position
playerPositionX = 0
playerPositionY = 0

# Creating pacman class
def pacman(x,y):
    screen.blit(pacSprite, (x,y))

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

    # Create the game
    screen.fill(black)
    pacman(playerPositionX,playerPositionY)
    ghost(ghostPositionX,ghostPositionY)
    pygame.display.update()
    clock.tick(60)
    
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
    
    