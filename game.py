import sys, pygame, random
from pipe import Pipe
from ball import Ball
FPS = 60 
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SIZE = SCREEN_WIDTH, SCREEN_HEIGHT
GAP = 50
PIPE_WIDTH = 50
DISTANCE_BETWEEN_PIPES = 300
PERSISTENT_X = SCREEN_WIDTH/4
PIPELINE = []
PIPELINE_SIZE = 3
GRAVITY = 0.25
ROLL_RATE = 2
BOUNCE = 6
BALL_RADIUS = 10
USER_SCORE = 0 
WHITE = (255, 255, 255)

fps_clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode(SIZE)

def randomPipeHeight(): 
    return SCREEN_HEIGHT - random.randint((SCREEN_HEIGHT - GAP)//4, (3*SCREEN_HEIGHT - GAP)//4)

def generatePipe(last_pipe, pipeline):
        pipe_x = last_pipe.x + DISTANCE_BETWEEN_PIPES  
        pipe_height = randomPipeHeight()
        pipe_y = SCREEN_HEIGHT - pipe_height
        return Pipe(pipe_x, pipe_y, pipe_height, PIPE_WIDTH)

def generateInitialPipeline(pipeline, pipeline_size):
    pipe_x, pipe_y = SCREEN_WIDTH, SCREEN_HEIGHT
    for i in range(pipeline_size):
        pipe_height = randomPipeHeight()
        pipe_y = SCREEN_HEIGHT - pipe_height
        pipeline.append(Pipe(pipe_x, pipe_y, pipe_height, PIPE_WIDTH))
        pipe_x += DISTANCE_BETWEEN_PIPES  

def drawPipes(pipeline):
    for pipe in pipeline:
        pygame.draw.rect(screen, WHITE, (pipe.x, pipe.y, pipe.width, pipe.height))
        pygame.draw.line(screen, WHITE, (pipe.x - 10, pipe.y), (pipe.x + pipe.width + 10, pipe.y))
        pygame.draw.line(screen, WHITE, (pipe.x - 10, pipe.y - GAP), (pipe.x + pipe.width + 10, pipe.y - GAP))
        lower_pipe_height = SCREEN_HEIGHT - pipe.height - GAP
        pygame.draw.rect(screen, WHITE, (pipe.x, 0, pipe.width, lower_pipe_height))

def updatePipeline(pipeline):
    new_pipe = generatePipe(pipeline[-1], pipeline)
    for pipe in pipeline:
        pipe.x -= ROLL_RATE

    if pipeline[0].x < -1*PIPE_WIDTH:
        pipeline.append(new_pipe)
        pipeline.pop(0)
        global USER_SCORE
        USER_SCORE += 1
        print(USER_SCORE)

def drawBall(ball):
    pygame.draw.circle(screen, WHITE, (ball.x, ball.y), BALL_RADIUS)

def checkCollision(pipeline, ball):
    for pipe in pipeline:
        if pipe.doesCollide(ball.x, ball.y, GAP, BALL_RADIUS):
            return True
    if (ball.y < 0 or ball.y > SCREEN_HEIGHT):
        return True

    return False

generateInitialPipeline(PIPELINE, PIPELINE_SIZE)
ball = Ball(SCREEN_WIDTH/5, SCREEN_HEIGHT/2, 0,  GRAVITY)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: ball.speed += -1*BOUNCE

    ball.update()
    updatePipeline(PIPELINE)
    
    if checkCollision(PIPELINE, ball): break

    drawBall(ball)
    drawPipes(PIPELINE)

    pygame.display.flip()
    screen.fill((0, 0, 0))
    fps_clock.tick(FPS)
