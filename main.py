import pygame

pygame.init()



# Code to initialize screen
width = 800
height = 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('PACMAN')
black = (0,0,0)
white = (255,255,255)
clock = pygame.time.Clock()
crashed = False


# Drawing Player
pacSprite = pygame.image.load('pacman.png')

def pacman():
    screen.blit(pacSprite, (0.1,0.1))
    



while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    screen.fill(white)
    pacman()
    pygame.display.update()
    clock.tick(60)

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
    
    