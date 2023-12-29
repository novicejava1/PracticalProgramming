import pygame

def main():
    print("Hello Pygame")
    pygame.init()

    # load a logo and set caption
    logo = pygame.image.load('game_logo.png')
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Simple Example")

    # create a surface
    screen = pygame.display.set_mode((500, 500))

    # define a control loop variable
    running = True

    # main loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == '__main__':
    main()
