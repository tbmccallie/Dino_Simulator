# Dino Simulator
# A simple simulation of a dinosuar in an enclosure
# A way of learning pygame and increasing my knowledge of python


try:
    import pygame, sys, random
except ImportError:
    print("Couldn't load module")
    sys.exit()


class Dino(pygame.sprite.Sprite):
    """A dinosaur that will move around the enclosure and reverse direction \
    if it hits a wall"""
    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.left, self.rect.top = location
    def move(self):
        """ Moves dino sprite, randomizes speed every 40 steps, reverses speed if it hits enclosure \
        walls, reverses image if it hits left or right wall"""
        if step == 40 and self.speed[0] not in range(-5, 0): # Randomizes movement after 40 steps and flips sprite (if x-value of speed variable changes from positive to negative
            self.speed[0] = random.randint(-5, -1)
            self.speed[1] = random.randint(-7, 7)
            self.image = pygame.transform.flip(self.image, 1, 0)
        elif step == 40 and self.speed[0] in range(-5, 0): # Randomizes movement after 40 steps, but doesn't flip sprite because x-value of speed variable doesn't change from positive to negative
            self.speed[0] = random.randint(-5, -1)
            self.speed[1] = random.randint(-7, 7)
        if step >= 80 and self.speed[0] not in range(1, 6): # # Randomizes movement after 80 steps and flips sprite (if x-value of speed variable changes from negative to positive)
            self.speed[0] = random.randint(1, 5)
            self.speed[1] = random.randint(-7, 7)
            self.image = pygame.transform.flip(self.image, 1, 0)
        elif step >= 80 and self.speed[0] in range(1, 6): # Randomizes movement after 80 steps, but doesn't flip sprite because x-value of speed variable doesn't change from negative to positive
            self.speed[0] = random.randint(1, 5)
            self.speed[1] = random.randint(-7, 7)
        if self.rect.left > 627 or self.rect.left < 173:
            if step != 40 and step != 80: # Keeps sprite from getting stuck on the wall in an endless cycle of flipping
                self.speed[0] = - self.speed[0]
                self.image = pygame.transform.flip(self.image, 1, 0) # Turns the dino when it hits the left or right side of the enclosure
        if self.rect.top > 385 or self.rect.top < 15:
            if step != 40 and step != 80:
                self.speed[1] = - self.speed[1]
        newpos = self.rect.move(self.speed)
        self.rect = newpos


def main():
    pygame.init()
    screen = pygame.display.set_mode([1000, 600])
    screen.fill([255, 255, 255])
    clock = pygame.time.Clock()
    my_dino = Dino("dino_model.png", [5, 7], [400, 130])
    global step
    step = 0


    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    # Draws the enclosure onto the background
    enclosure = pygame.draw.rect(background, [0, 0, 0], (180, 60, 640, 480), 5)

    # Displays the title on the background
    font = pygame.font.SysFont("calibri", 48, bold=True)
    text = font.render("Dino Simulator", 1, (0, 0, 0))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = 25
    background.blit(text, textpos)

    screen.blit(background, (0, 0))
    screen.blit(my_dino.image, my_dino.rect) # so the time.delay below doesn't cause the dino to be drawn later than the background
    pygame.display.flip()

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
        pygame.time.delay(300)
        screen.blit(background, (0, 0))
        my_dino.move()
        step += 1
        if step > 80:
            step = 0
        screen.blit(my_dino.image, my_dino.rect) # This, combined with the 2 lines above it, draw the dinosaur in its new position and erases it from its previous position
        pygame.display.update(my_dino.rect)
    pygame.quit()

if __name__ == "__main__":
    main()
