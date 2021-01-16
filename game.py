import sys, pygame, random
from pipe import Pipe

pygame.init()

    # o- - - - > x
    # '
    # '
    # '
    # '
    # y

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SIZE = SCREEN_WIDTH, SCREEN_HEIGHT

# game parameters
GAP = 100
PIPE_WIDTH = 50
DISTANCE_BETWEEN_PIPES = 300
starting_point_ball = SCREEN_WIDTH/4, SCREEN_HEIGHT/2
GRAVITY = 0.02
PIPELINE = []
PIPELINE_SIZE = 3

screen = pygame.display.set_mode(SIZE)

# ball parameters
black = 0, 0, 0
ball_x, ball_y = starting_point_ball
ball_speed = 0


def randomPipeHeight(): 
    return SCREEN_HEIGHT - random.randint((SCREEN_HEIGHT - GAP)//4, (SCREEN_HEIGHT - GAP)//2)

def generateInitialPipeline(pipeline, pipeline_size):
    pipe_x, pipe_y = SCREEN_WIDTH, SCREEN_HEIGHT
    for i in range(pipeline_size):
        pipe_height = randomPipeHeight()
        pipe_y = SCREEN_HEIGHT - pipe_height
        pipeline.append(Pipe(pipe_x, pipe_y, pipe_height, PIPE_WIDTH))
        pipe_x += DISTANCE_BETWEEN_PIPES  

def drawPipes(pipeline):
    for pipe in pipeline:
        # lower pipeline
        pygame.draw.rect(screen, (255,0,0), (pipe.x, pipe.y, pipe.width, pipe.height))
        # upper pipeline 
        lower_pipe_height = SCREEN_HEIGHT - pipe.height - GAP
        pygame.draw.rect(screen, (255,0,0), (pipe.x, 0, pipe.width, lower_pipe_height))

def updatePipeline(pipeline):
    for pipe in pipeline:
        print(pipe.__dict__)
        pipe.x -= 1


def drawBall():
    pygame.draw.circle(screen, (255,0,0), (ball_x, ball_y), 5)

generateInitialPipeline(PIPELINE, PIPELINE_SIZE)

print(randomPipeHeight())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: ball_speed = -1.5

    drawPipes(PIPELINE)
    pygame.display.flip()
    screen.fill(black)
    ball_y += ball_speed
    ball_speed += GRAVITY
    updatePipeline(PIPELINE)
