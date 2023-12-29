import pygame

screenSize = 500, 500
black = 0, 0, 0

# Load image
def loadImage():

    pic = pygame.image.load("ball.gif")
    dimension = pic.get_rect()
    print(dimension)

    return pic, dimension

# Main Function
def main():

    # Initialize and Prepare the screen
    pygame.init()
    screen = pygame.display.set_mode(screenSize)

    # Capture the Image and Dimensions
    pic, dimension = loadImage()

    # Display the Image on the screen
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(pic, dimension)
        #dimension = dimension.move([2, 2])
        screen.blit(pic, (10, 10, 10, 10))
        screen.blit(pic, (20, 20, 20, 20))
        screen.blit(pic, (30, 30, 30, 30))
        screen.blit(pic, (40, 40, 40, 40))
        screen.blit(pic, (50, 50, 50, 50))

        for i in range(10):
            screen.blit(pic, (i + 50, 10, 10, i + 10))

        pygame.display.flip()


if __name__ == '__main__':
    main()
