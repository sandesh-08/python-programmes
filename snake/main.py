import pygame
import random
import os

pygame.mixer.init()
pygame.init()

# color
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
snakegreen = (35,45,40)
#Game background
bg1 = pygame.image.load("bg.jpg")
bg2 = pygame.image.load("bg2.jpg")
intro = pygame.image.load("intro.png")
outro = pygame.image.load("outro.png")



#creatiing window
screen_width = 900
screen_height = 600
gameWindow=pygame.display.set_mode((screen_width,screen_height))

# Game title
pygame.display.set_caption("SnakeWithAbhay")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont('Harrington', 35)

def text_screen(text,color,x,y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def  plot_snake(gameWindow, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game=False
    while not exit_game:
        gameWindow.blit(intro, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.load("bgm.mp3")
                    pygame.mixer.music.play()
                    gameLoop()
        pygame.display.update()
        clock.tick(40)

#Game loop
def gameLoop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snake_list = []
    snake_length = 1
    #Check if highscore file exists
    if(not os.path.exists("highScore.txt")):
        with open("highScore.txt","w") as  f:
            f.write(0)
    with open("highScore.txt", "r") as f:
        highscore = f.read()


    food_x = random.randint(12, screen_width / 2)
    food_y = random.randint(12, screen_height / 2)
    score = 0
    init_velocity = 5
    snake_size = 15
    fps = 20
    while not exit_game:
        if game_over:
            with open("highScore.txt", "w") as f:
                f.write(str(highscore))
             #Game over screen
            gameWindow.blit(outro,(0,0))
            text_screen("Score: " + str(score), snakegreen, 385, 350)



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type== pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key== pygame.K_a:
                        score +=10
            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                score += 10
                food_x = random.randint(12, screen_width / 2)
                food_y = random.randint(12, screen_height / 2)
                snake_length += 5
                if score > int(highscore):
                    highscore = score

            gameWindow.blit(bg2, (0, 0))
            text_screen("Score: " + str(score) + "  Highscore: " + str(highscore), snakegreen, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:-1]: #it means that all element except last element of the list or when last element come in list it give game over
                game_over = True

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True



            plot_snake(gameWindow, black, snake_list, snake_size)



        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()