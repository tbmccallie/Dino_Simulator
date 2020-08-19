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
        """Moves dino sprite, randomizes speed every 40 steps, reverses speed if it hits enclosure \
        walls, reverses image if it hits left or right wall"""
        if step == 40 and 0 < hunger < 205 and thirst < 175 and self.speed[0] not in range(-1000, 0): # Randomizes movement after 40 steps and flips sprite (if x-value of speed variable changes from positive to negative
            self.speed[0] = random.randint(-5, -1)
            self.speed[1] = random.randint(-7, 7)
            self.image = pygame.transform.flip(self.image, 1, 0)
        elif step == 40 and 0 < hunger < 205 and thirst < 175 and self.speed[0] in range(-1000, 0): # Randomizes movement after 40 steps, but doesn't flip sprite because x-value of speed variable doesn't change from positive to negative
            self.speed[0] = random.randint(-5, -1)
            self.speed[1] = random.randint(-7, 7)
        if step == 80 and 0 < hunger < 205 and thirst < 175 and self.speed[0] not in range(0, 1000): # Randomizes movement after 80 steps and flips sprite (if x-value of speed variable changes from negative to positive
            self.speed[0] = random.randint(1, 5)
            self.speed[1] = random.randint(-7, 7)
            self.image = pygame.transform.flip(self.image, 1, 0)
        elif step == 80 and 0 < hunger < 205 and thirst < 175 and self.speed[0] in range(0, 1000): # Randomizes movement after 80 steps, but doesn't flip sprite because x-value of speed variable doesn't change from positive to negative
            self.speed[0] = random.randint(1, 5)
            self.speed[1] = random.randint(-7, 7)
        if self.rect.right > 818 or self.rect.left < 182:
            if step != 40 and step != 80 and 0 < hunger < 205 and thirst < 175: # Keeps sprite from getting stuck on wall in an endless cycle of flipping
                self.speed[0] = - self.speed[0]
                self.image = pygame.transform.flip(self.image, 1, 0) # Turns the dino when it hits the left or right side of the enclosure
        if self.rect.top < 55 or self.rect.bottom > 542:
            if step != 40 and step != 80 and 0 < hunger < 205 and thirst < 175:
                self.speed[1] = - self.speed[1]
        if hunger >= 205: # Causes dinosaur to go to the tree when hunger is high enough
            if step != 40 and step != 80 and 0 < thirst < 175:
                if self.rect.left > 300 and self.speed[0] not in range(-1000, 0):
                    self.speed[0] = round((300 - self.rect.left)/30) # Must be rounded so that speed[0] is in the range functions above (range function doesn't take decimal point numbers)
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
        if thirst == 175: # Causes dinosaur to go to the pond when thirst is high enough
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
        newpos = self.rect.move(self.speed)
        self.rect = newpos
    def check_collision(self, sprite1, sprite2):
        """Checks if dino sprite and food sprite are touching, and if so, reverses the dino's direction"""
        col = pygame.sprite.collide_rect(sprite1, sprite2)
        if col == True:
            if step != 40 and step != 80:
                self.speed[0] = - self.speed[0]
                self.speed[1] = - self.speed[1]
                self.image = pygame.transform.flip(self.image, 1, 0)

class Food(pygame.sprite.Sprite):
    """A food source that the dinosaur can collide with and use to eat when it's hunger meter gets low enough"""
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

def main():
    # Initialises pygame and screen and creates an instance of the Dino class and Food class
    pygame.init()
    screen = pygame.display.set_mode([1000, 600])
    screen.fill([255, 255, 255])
    clock = pygame.time.Clock()
    my_dino = Dino("dino_model.png", [5, 7], [400, 130])
    dino_food = Food("food.png", [300, 340])
    global step
    step = 0
    global hunger
    hunger = 0
    global thirst
    thirst = 0

    # Creates the background surface on which to draw everything else, fills background white,
    # and draws the food, pond, and enclosure onto the background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    background.blit(dino_food.image, dino_food.rect)
    pygame.draw.rect(background, [0, 0, 0], (180, 60, 640, 480), 5) # Draws enclosure
    pond = pygame.image.load("pond.png").convert_alpha()
    background.blit(pond, [540,120])

    # Displays the title on the background
    t_font = pygame.font.SysFont("calibri", 48, bold=True)
    t_text = t_font.render("Dino Simulator", 1, (0, 0, 0))
    t_textpos = t_text.get_rect()
    t_textpos.centerx, t_textpos.centery = background.get_rect().centerx, 25
    background.blit(t_text, t_textpos)

    # Displays a hunger bar
    pygame.draw.rect(background, [0,0,0], (12.5, 200, 150, 24), 3) # Hunger bar outline
    pygame.draw.rect(background, [0,128,0], (13, 202, 148, 20)) # Fills hunger bar with green

    # Displays a thirst bar
    pygame.draw.rect(background, [0,0,0], (12.5, 270, 150, 24), 3) # Thirst bar outline
    pygame.draw.rect(background, [0,0,190], (13, 272, 148, 20)) # Fills thirst bar with blue

    # Displays the hunger bar label above the hunger bar
    h_font = pygame.font.SysFont("calibri", 20, bold=True)
    h_text = h_font.render("Hunger", 1, (0, 0, 0))
    h_textpos = h_text.get_rect()
    h_textpos.centerx, h_textpos.centery = 81.25, 185
    background.blit(h_text, h_textpos)

    # Displays the thirst bar label above the thirst bar
    th_font = pygame.font.SysFont("calibri", 20, bold=True)
    th_text = th_font.render("Thirst", 1, (0, 0, 0))
    th_textpos = th_text.get_rect()
    th_textpos.centerx, th_textpos.centery = 81.25, 255
    background.blit(th_text, th_textpos)

    # Blit the background and everything on it to the screen
    screen.blit(background, (0, 0))
    screen.blit(my_dino.image, my_dino.rect) # so the time.delay below doesn't cause the dino to be drawn later than the background
    pygame.display.flip()

    # This is the event loop, which is what "runs" the game
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
        if hunger >= 205: # Changes hunger bar color to red when Dinosaur hits hunger threshold
            pygame.draw.rect(background, [200,0,0], (13, 202, hunger/2, 20))
        if thirst >= 175: # Changes thirst bar color to red when Dinosaur hits thirst threshold
            pygame.draw.rect(background, [200,0,0], (13, 272, thirst/2, 20))
        pygame.draw.rect(background, [255,255,255], (160.5, 202, -hunger/2, 20)) # Draws white rectangle over green hunger bar rectangle, which grows to the left as hunger increases
        pygame.draw.rect(background, [255,255,255], (160.5, 272, -thirst/2, 20)) # Draws white rectangle over blue thirst bar rectangle, which grows to the left as thirst increases
        my_dino.move()
        my_dino.check_collision(my_dino, dino_food)
        step += 1
        if step > 80:
            step = 0
        hunger += 1
        if hunger > 292 or pygame.sprite.collide_rect(my_dino, dino_food) and hunger >= 205: # 148 is the length the green bar can be without covering up the rect outline
            hunger = 0
            pygame.draw.rect(background, [0,128,0], (13, 202, 148, 20)) # Redraws full green hunger bar when dinosaur "eats"
        thirst += 1
        if thirst > 292 or my_dino.rect.collidepoint(550,140) and thirst >= 175:
            thirst = 0
            pygame.draw.rect(background, [0,0,190], (13, 272, 148, 20)) # Redraws full blue hunger bar when dinosaur "drinks"
        screen.blit(my_dino.image, my_dino.rect) # This, combined with my_dino.move() and screen.blit(background), draw the dinosaur in its new position and erases it from its previous position
        pygame.display.flip()
    pygame.quit()

# Calls the 'main' function when this script is executed
if __name__ == "__main__":
    main()
