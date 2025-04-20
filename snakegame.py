import pygame
import time
import random

# Initializa pygame
pygame.init()

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set display diamentions
display_width = 600
display_height = 400

# Set up game
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

# Clock fro controlling game speed
clock = pygame.time.Clock()

# Snake properties
snake_block = 20
snake_speed = 15

# Font style
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def your_score(score):
    """Display the current score"""
    value = score_font.render("Score: " + str(score), True, white)
    game_display.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    """Draw the snake on the screen"""
    for x in snake_list:
        pygame.draw.rect(game_display, green, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    """Display a message on the screen"""
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [display_width / 6, display_height / 3])

def game_loop():
    """Main game loop"""
    game_over = False
    game_close = False

    # Initial snake position
    x1 = display_width / 2
    y1 = display_height / 2

    # Initial snake movement direction
    x1_change = 0
    y1_change = 0

    # Initial snake list and length
    snake_list = []
    length_of_snake = 1

    # Generate first food position
    foodx = round(random.randrange(0, display_width - snake_block) / snake_block) * snake_block
    foody = round(random.randrange(0, display_height - snake_block) / snake_block) * snake_block

    while not game_over:

        # Game over with restart option
        while game_close:
            game_display.fill(black)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            your_score(length_of_snake - 1)
            pygame.display.update()

            # Check restart or quite
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
        
        # Handle keyboard input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        
        # Check for boundary collision
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True

        # Update snake position
        x1 += x1_change
        y1 += y1_change

        # Clear and redraw the display
        game_display.fill(black)

        # Draw food
        pygame.draw.rect(game_display, red, [foodx, foody, snake_block, snake_block])

        # Update snake
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        # Remove extra segments if snake hasn't grown
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check for collision with self
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Draw the snake and score
        our_snake(snake_block, snake_list)
        your_score(length_of_snake - 1)

        # Update display
        pygame.display.update()

        # Check if snake ate food
        if x1 == foodx and y1 == foody:
            # Generate new food position
            foodx = round(random.randrange(0, display_width - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(0, display_height - snake_block) / snake_block) * snake_block
            # Increase snake length
            length_of_snake += 1

        # Control game speed
        clock.tick(snake_speed)

    # Quit pygame and exit
    pygame.quit()
    quit()

# Start the game
game_loop()