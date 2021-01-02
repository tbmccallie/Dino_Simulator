# A food source that the dinosaur can collide with and use
# to eat when its hunger gets high enough

try:
    import pygame, sys
except ImportError:
    print("Couldn't load module")
    sys.exit()

class Food(pygame.sprite.Sprite):
    """A food source that the dinosaur can collide with and \
    use to eat when its hunger gets high enough.
    
    Parameters
    ----------
    image_file : image file you want to represent a food source.
    location : list of two ints representing coordinates 
    that you want top-left point of the food sprite to be at.
    """
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location