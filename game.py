import sys, pygame

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
size = SCREEN_WIDTH, SCREEN_HEIGHT

# game parameters
gap = 50
starting_point_ball = SCREEN_WIDTH/4, SCREEN_HEIGHT/2
gravity = 0.001

screen = pygame.display.set_mode(size)

    # o- - - - > x
    # '
    # '
    # '
    # '
    # y

# ball parameters
black = 0, 0, 0
ball_x, ball_y = starting_point_ball
ball_speed = 0

# lower pipe parameters
lower_pipe_width = 50
lower_pipe_length = SCREEN_HEIGHT/2
lower_pipe_x, lower_pipe_y = SCREEN_WIDTH, SCREEN_HEIGHT - lower_pipe_length

# upper pipe parameters
upper_pipe_width = 50
upper_pipe_length = SCREEN_HEIGHT/2 - gap
upper_pipe_x, upper_pipe_y = SCREEN_WIDTH, 0 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: ball_speed = -0.5

    pygame.draw.circle(screen, (255,0,0), (ball_x, ball_y), 5)
    pygame.draw.rect(screen, (255,0,0), (lower_pipe_x, lower_pipe_y, lower_pipe_width, lower_pipe_length))
    pygame.draw.rect(screen, (255,0,0), (upper_pipe_x, upper_pipe_y, upper_pipe_width, upper_pipe_length))

    pygame.display.flip()
    screen.fill(black)

    ball_y += ball_speed
    ball_speed += gravity
    lower_pipe_x -= 0.21
    upper_pipe_x -= 0.21
