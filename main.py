# Dino Simulator
# A simple simulation of a dinosuar in an enclosure
# A way of learning pygame and increasing my knowledge of python
# Created by Trenton McCallie


try:
    import pygame, sys, Food, Dino, Label
except ImportError:
    print("Couldn't load module")
    sys.exit()

def main():

    # Initialises pygame and screen and creates an instance of the Dino class and Food class
    pygame.init()
    screen = pygame.display.set_mode([1000, 600])
    screen.fill([255, 255, 255])
    clock = pygame.time.Clock()
    my_dino = Dino.Dino("dino_model.png", [5, 7], [400, 130])
    dino_food = Food.Food("food.png", [300, 340])

    # Creates the background surface on which to draw everything else
    background = pygame.Surface(screen.get_size())
    background = background.convert()

    # Fills background white
    background.fill((255, 255, 255))

    # Draws enclosure onto the background
    pygame.draw.rect(background, [0, 0, 0], (180, 60, 640, 480), 5)

    # Fills enclosure with green "grass"
    pygame.draw.rect(background, [0, 160, 0], (182, 62, 636, 476))

    # Draws the food onto the background
    background.blit(dino_food.image, dino_food.rect)

    # Initializes and draws the pond onto the background
    pond = pygame.image.load("pond.png").convert_alpha()
    background.blit(pond, [540,120])

    # Displays the title on the background
    Label.label(48, "Dinosaur Simulator", (0, 0, 0), background, (background.get_rect().centerx, 25))

    # Displays the hunger bar label above the hunger bar
    Label.label(20, "Hunger", (0, 0, 0), background, (81.25, 185))

    # Displays the thirst bar label above the thirst bar
    Label.label(20, "Thirst", (0, 0, 0), background, (81.25, 255))

    # Displays a hunger bar
    pygame.draw.rect(background, [0,0,0], (12.5, 200, 150, 24), 3) # Hunger bar outline
    pygame.draw.rect(background, [0,128,0], (13, 202, 148, 20)) # Fills hunger bar with green

    # Displays a thirst bar
    pygame.draw.rect(background, [0,0,0], (12.5, 270, 150, 24), 3) # Thirst bar outline
    pygame.draw.rect(background, [0,0,190], (13, 272, 148, 20)) # Fills thirst bar with blue

    # Blit the background and everything on it to the screen
    screen.blit(background, (0, 0))

    # Used to draw the dino on the screen at the same time as the background so \
    # the time.delay function below doesn't cause the dino to be drawn later than \
    # the background
    screen.blit(my_dino.image, my_dino.rect)

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

        # Changes hunger bar color to red when Dinosaur hits hunger threshold
        if Dino.hunger >= 205:
            pygame.draw.rect(background, [200,0,0], (13, 202, Dino.hunger/2, 20))

        # Changes thirst bar color to red when Dinosaur hits thirst threshold
        if Dino.thirst >= 175:
            pygame.draw.rect(background, [200,0,0], (13, 272, Dino.thirst/2, 20))

        # Draws white rectangle over green hunger bar rectangle, \
        # which grows to the left as hunger increases
        pygame.draw.rect(background, [255,255,255], (160.5, 202, -Dino.hunger/2, 20))

        # Draws white rectangle over blue thirst bar rectangle, \
        # which grows to the left as thirst increases
        pygame.draw.rect(background, [255,255,255], (160.5, 272, -Dino.thirst/2, 20))

        # Function that causes dino to "walk" around
        my_dino.move()

        # Checks to see if dino sprite has collided with food sprite
        my_dino.check_collision(my_dino, dino_food)

        Dino.step += 1
        if Dino.step > 80:
            Dino.step = 0

        Dino.hunger += 1

        # 148 is the length the green bar can be without covering up the rect outline
        # Checks if dino sprite is touching food sprite when hunger is high enough
        if Dino.hunger > 292 or pygame.sprite.collide_rect(my_dino, dino_food) and Dino.hunger >= 205:
            Dino.hunger = 0

            # Redraws full green hunger bar when dinosaur "eats"
            pygame.draw.rect(background, [0,128,0], (13, 202, 148, 20))

        Dino.thirst += 1

        # Checks if dino has touched the pond when thirst is high enough
        if Dino.thirst > 292 or my_dino.rect.collidepoint(550,140) and Dino.thirst >= 175:
            Dino.thirst = 0

            # Redraws full blue thirst bar when dinosaur "drinks"
            pygame.draw.rect(background, [0,0,190], (13, 272, 148, 20))

        # This, combined with my_dino.move() and screen.blit(background), \
        # draws the dinosaur in its new position and erases it from its previous position
        screen.blit(my_dino.image, my_dino.rect)
        pygame.display.flip()
    pygame.quit()

# Calls the 'main' function when this script is executed
if __name__ == "__main__":
    main()
