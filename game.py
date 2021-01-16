import sys, pygame
pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
size = SCREEN_WIDTH, SCREEN_HEIGHT

screen = pygame.display.set_mode(size)

# --------> x
# |
# |
# |
# y

# ball parameters
black = 0, 0, 0
ballx, bally = 1, 1

# pipe parameters
pipeWidth = 50
pipeLength = SCREEN_HEIGHT/2
pipex, pipey = 0, SCREEN_HEIGHT - pipeLength

# game parameters
gap = 50




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    pygame.draw.circle(screen, (255,0,0), (ballx, bally), 5)
    pygame.draw.rect(screen, (255,0,0), (pipex, pipey, pipeWidth, pipeLength))
    pygame.display.flip()
    screen.fill(black)
    ballx,bally = map(lambda x: x + 1, [ballx, bally])
