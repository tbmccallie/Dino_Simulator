# Dino Simulator
# A simple simulation of a dinosuar in an enclosure
# A way of learning pygame and increasing my knowledge of python


try:
    import pygame, sys
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
        """ Moves dino sprite, reverses speed if it hits enclosure \
        walls, reverses image if it hits left or right wall"""
        if self.rect.left > 627 or self.rect.left < 173:
            self.speed[0] = - self.speed[0]
            self.image = pygame.transform.flip(self.image, 1, 0) # Turns the dino when it hits the left or right side of the enclosure
        if self.rect.top > 385 or self.rect.top < 15:
            self.speed[1] = - self.speed[1]
        newpos = self.rect.move(self.speed)
        self.rect = newpos


def main():
    pygame.init()
    screen = pygame.display.set_mode([1000, 600])
    screen.fill([255, 255, 255])
    clock = pygame.time.Clock()
    my_dino = Dino("dino_model.png", [5, 7], [400, 130])


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
        screen.blit(my_dino.image, my_dino.rect) # This, combined with the 2 lines above it, draw the dinosaur in its new position and erases it from its previous position
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
