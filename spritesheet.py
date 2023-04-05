import pygame

class SpriteSheet:
    def __init__(self, SpriteSheetFile):
        self.SpriteSheetFile = SpriteSheetFile
        self.sheet = pygame.image.load(SpriteSheetFile).convert_alpha()


# Extract sprites from spriteSheet from spriteSheet.png

    def getSprite(self,x,y,w,h,scale):
        sprite = pygame.Surface((w,h)).convert_alpha()
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sheet,(0,0), (x,y,w,h))
        #sprite = pygame.transform.scale(self.sheet,(scale,scale))
        return sprite
    
    def animation(self,name):
        sprite = self.data['frames'][name]['frame']
        
    