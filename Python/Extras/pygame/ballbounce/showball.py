import pygame

pygame.init()

size = 500, 500
speed = [.5, 1]
black = 0, 0, 0

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()
print(type(ballrect))
print(ballrect)

screen = pygame.display.set_mode(size)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)
    screen.blit(ball, ballrect)
    ballrect = ballrect.move(speed)

    pygame.display.flip()
