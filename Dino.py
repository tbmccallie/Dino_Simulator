# A dinosaur that will move around the enclosure, reverse direction if
# it hits a wall or another sprite, and go to a food source or water source
# if its hunger or thirst gets high enough

try:
    import pygame, sys, random
except ImportError:
    print("Couldn't load module")
    sys.exit()

step = 0
hunger = 0
thirst = 0

class Dino(pygame.sprite.Sprite):
    """A dinosaur that will move around the enclosure, reverse direction \
    if it hits a wall or another sprite, and go to a food source or water \
    source if its hunger or thirst gets high enough.
    
    Parameters
    ----------
    image_file : image file you want to represent the dino.
    speed : list of two ints that represents velocity of the dino.
    location : list of two ints representing coordinates 
    that you want top-left point of the dino sprite to be at.
    """

    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.left, self.rect.top = location

    def move(self):
        """Moves dino sprite, randomizes speed every 40 steps, reverses speed if it hits enclosure \
        walls, reverses image if it hits left or right wall"""

        # Randomizes movement after 40 steps and flips sprite \
        # (if x-value of speed variable changes from positive to negative)
        if step == 40 and 0 < hunger < 205 and thirst < 175 and self.speed[0] not in range(-1000, 0):
            self.speed[0] = random.randint(-5, -1)
            self.speed[1] = random.randint(-7, 7)
            self.image = pygame.transform.flip(self.image, 1, 0)

        # Randomizes movement after 40 steps, but doesn't flip sprite because \
        # x-value of speed variable doesn't change from positive to negative
        elif step == 40 and 0 < hunger < 205 and thirst < 175 and self.speed[0] in range(-1000, 0):
            self.speed[0] = random.randint(-5, -1)
            self.speed[1] = random.randint(-7, 7)

        # Randomizes movement after 80 steps and flips sprite \
        # (if x-value of speed variable changes from negative to positive)
        if step == 80 and 0 < hunger < 205 and thirst < 175 and self.speed[0] not in range(0, 1000):
            self.speed[0] = random.randint(1, 5)
            self.speed[1] = random.randint(-7, 7)
            self.image = pygame.transform.flip(self.image, 1, 0)

        # Randomizes movement after 80 steps, but doesn't flip sprite \
        # because x-value of speed variable doesn't change from positive to negative
        elif step == 80 and 0 < hunger < 205 and thirst < 175 and self.speed[0] in range(0, 1000):
            self.speed[0] = random.randint(1, 5)
            self.speed[1] = random.randint(-7, 7)

        # Flips the dino sprite when it hits the left or right side of the enclosure \
        # and reverses dino's speed
        if self.rect.right > 818 or self.rect.left < 182:
            # Keeps sprite from getting stuck on wall in an endless cycle of flipping
            if step != 40 and step != 80 and 0 < hunger < 205 and thirst < 175:
                self.speed[0] = - self.speed[0]
                self.image = pygame.transform.flip(self.image, 1, 0)

        # Reverses the dino's speed if it hits the top or bottom side of the enclosure
        if self.rect.top < 55 or self.rect.bottom > 542:
            # Keeps sprite from getting stuck on wall in an endless cycle of flipping
            if step != 40 and step != 80 and 0 < hunger < 205 and thirst < 175:
                self.speed[1] = - self.speed[1]

        # Causes dinosaur to go to the tree when hunger is high enough
        if hunger >= 205:
            if step != 40 and step != 80 and 0 < thirst < 175:
                if self.rect.left > 300 and self.speed[0] not in range(-1000, 0):
                    # Speed must be rounded so that speed[0] and speed[1] is in the range functions above \
                    # (range function doesn't take decimal point numbers)
                    self.speed[0] = round((300 - self.rect.left)/30)
                    self.speed[1] = round((340 - self.rect.top)/30)
                    self.image = pygame.transform.flip(self.image, 1, 0)
                elif self.rect.left > 300 and self.speed[0] in range(-1000, 0):
                    self.speed[0] = round((300 - self.rect.left)/30)
                    self.speed[1] = round((340 - self.rect.top)/30)
                if self.rect.left < 300 and self.speed[0] not in range(1, 1000):
                    self.speed[0] = round((300 - self.rect.left)/30)
                    self.speed[1] = round((340 - self.rect.top)/30)
                    self.image = pygame.transform.flip(self.image, 1, 0)
                elif self.rect.left < 300 and self.speed[0] in range(1, 1000):
                    self.speed[0] = round((300 - self.rect.left)/30)
                    self.speed[1] = round((340 - self.rect.top)/30)

        # Causes dinosaur to go to the pond when thirst is high enough
        if thirst == 175:
            if step != 40 and step != 80:
                if self.rect.left > 540 and self.speed[0] not in range(-1000, 0):
                    self.speed[0] = round((540 - self.rect.left)/30)
                    self.speed[1] = round((120 - self.rect.top)/30)
                    self.image = pygame.transform.flip(self.image, 1, 0)
                elif self.rect.left > 540 and self.speed[0] in range(-1000, 0):
                    self.speed[0] = round((540 - self.rect.left)/30)
                    self.speed[1] = round((120 - self.rect.top)/30)
                if self.rect.left < 540 and self.speed[0] not in range(1, 1000):
                    self.speed[0] = round((540 - self.rect.left)/30)
                    self.speed[1] = round((120 - self.rect.top)/30)
                    self.image = pygame.transform.flip(self.image, 1, 0)
                elif self.rect.left < 540 and self.speed[0] in range(1, 1000):
                    self.speed[0] = round((540 - self.rect.left)/30)
                    self.speed[1] = round((120 - self.rect.top)/30)

        # Sets rectangle surrounding dino sprite to new position based on its speed
        newpos = self.rect.move(self.speed)
        self.rect = newpos

    def check_collision(self, sprite1, sprite2):
        """Checks if dino sprite and another sprite are touching, and if so, \
        reverses the dino's direction and flips the dino sprite"""
        col = pygame.sprite.collide_rect(sprite1, sprite2)
        if col == True:
            if step != 40 and step != 80:
                self.speed[0] = - self.speed[0]
                self.speed[1] = - self.speed[1]
                self.image = pygame.transform.flip(self.image, 1, 0)