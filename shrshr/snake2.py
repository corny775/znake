import pygame
from pygame.locals import *
import random
pygame.init()

screen_width = 900
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Znake')
#define font
font = pygame.font.SysFont(None, 40)

#setup a rectangle for "Play Again" Option
again_rect = Rect(screen_width // 2 - 80, screen_height // 2, 160, 50)

galaxy = pygame.image.load("ground.png")
galaxy_rect = galaxy.get_rect(topleft = (0, 0))

#define snake variables
snake_pos = [[int(screen_width / 2), int(screen_height / 2)]]
snake_pos.append([450,310])
snake_pos.append([450,320])
snake_pos.append([450,330])
direction = 1 #1 is up, 2 is right, 3 is down, 4 is left
#define game variables
cell_size = 15
update_snake = 0
food = [0, 0]
new_food = True
new_piece = [0, 0]
game_over = False
clicked = False
score = 0

#define colors
bg = (94, 123, 35)
body_inner = (50, 25, 175)
body_outer = (100, 100, 200)

foodcol = pygame.image.load("brain1.png")
foodcol_rect = foodcol.get_rect()
zomhead = pygame.image.load("zombie1.png")
zomhead_rect = zomhead.get_rect()
button = pygame.image.load("correctrestar2.png")
button_rect = button.get_rect()
blue = (0, 0, 255)
red = (255, 0, 0)
black =(0, 0, 0)
white =(255, 255, 255)

def draw_screen():
        screen.fill(bg)
        screen.blit(galaxy, galaxy_rect)
def draw_score():
        score_txt = 'Score: ' + str(score)
        pygame.draw.rect(screen, black, (0, 0, 160, 35))
        score_img = font.render(score_txt, True, blue)
        screen.blit(score_img, (5, 5))
def check_game_over(game_over):
        #first check is to see if the snake has eaten itself by checking if the head has clashed with the rest of the body
        head_count = 0
        for x in snake_pos:
                if snake_pos[0] == x and head_count > 0:
                        game_over = True
                head_count += 1

        #second check is to see if the snake has gone out of bounds
        if snake_pos[0][0] < 0 or snake_pos[0][0] > screen_width or snake_pos[0][1] < 0 or snake_pos[0][1] > screen_height:
                game_over = True   
        return game_over
def draw_game_over():
        over_text = "Game Over!"
        over_img = font.render(over_text, True, white)
        #pygame.draw.rect(screen, white, (screen_width // 2 - 80, screen_height // 2 - 60, 160, 50))
        screen.blit(button, (265, 115))
        screen.blit(over_img, (screen_width // 2 - 80, screen_height // 2 - 50))

run = True
while run:
        draw_screen()
        draw_score()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP and direction != 3:
                                direction = 1
                        if event.key == pygame.K_RIGHT and direction != 4:
                                direction = 2
                        if event.key == pygame.K_DOWN and direction != 1:
                                direction = 3
                        if event.key == pygame.K_LEFT and direction != 2:
                                direction  = 4

        #create food
        if new_food == True:
                new_food = False
                food[0] = cell_size * random.randint(0, int(screen_width / cell_size) - 1)
                food[1] = cell_size * random.randint(0, int(screen_height / cell_size) - 1)

        #draw food
        #pygame.draw.rect(screen, food_col, (food[0], food[1], cell_size, cell_size))
        screen.blit(foodcol, (food[0], food[1]))
        #check if food has been eaten
        if snake_pos[0] == food:
                new_food = True
                #create a new piece at the last point of the snake's tail
                new_piece = list(snake_pos[-1])
                #add an extra piece to the snake
                if direction == 1:
                        new_piece[1] += cell_size
                #heading down
                if direction == 3:
                        new_piece[1] -= cell_size
                #heading right
                if direction == 2:
                        new_piece[0] -= cell_size
                #heading left
                if direction == 4:
                        new_piece[0] += cell_size
                #attach new piece to the end of the snake
                snake_pos.append(new_piece)
                #increase score
                score += 1

        if game_over == False:
                #update snake
                if update_snake > 99:
                        update_snake = 0
                        #first shift the positions of each snake piece back.
                        snake_pos = snake_pos[-1:] + snake_pos[:-1]
                        #now update the position of the head based on direction
                        #heading up
                        if direction == 1:
                                snake_pos[0][0] = snake_pos[1][0]
                                snake_pos[0][1] = snake_pos[1][1] - cell_size
                        #heading down
                        if direction == 3:
                                snake_pos[0][0] = snake_pos[1][0]
                                snake_pos[0][1] = snake_pos[1][1] + cell_size
                        #heading right
                        if direction == 2:
                                snake_pos[0][1] = snake_pos[1][1]
                                snake_pos[0][0] = snake_pos[1][0] + cell_size
                        #heading left
                        if direction == 4:
                                snake_pos[0][1] = snake_pos[1][1]
                                snake_pos[0][0] = snake_pos[1][0] - cell_size
                        game_over = check_game_over(game_over)
        if game_over == True:
                draw_game_over()
                if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                        clicked = True
                if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                        clicked = False
                        #reset variables
                        game_over = False
                        update_snake = 0
                        food = [0, 0]
                        new_food = True
                        new_piece = [0, 0]
                        #define snake variables
                        snake_pos = [[int(screen_width / 2), int(screen_height / 2)]]
                        snake_pos.append([450,310])
                        snake_pos.append([450,320])
                        snake_pos.append([450,330])
                        direction = 1 #1 is up, 2 is right, 3 is down, 4 is left
                        score = 0
        head = 1
        for x in snake_pos:
                if head == 0:
                        #pygame.draw.rect(screen, body_outer, (x[0], x[1], cell_size, cell_size))
                        #pygame.draw.rect(screen, body_inner, (x[0] + 1, x[1] + 1, cell_size - 2, cell_size - 2))
                        screen.blit(zomhead, (x[0], x[1]))
                if head == 1:
                        #pygame.draw.rect(screen, body_outer, (x[0], x[1], cell_size, cell_size))
                        #pygame.draw.rect(screen, (255,0,0), (x[0] + 1, x[1] + 1, cell_size - 2, cell_size - 2))
                        screen.blit(zomhead, (x[0], x[1]))
                        head = 0
        pygame.display.update()
        update_snake += 10
pygame.quit()