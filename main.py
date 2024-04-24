import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("MyFirstGame")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Player
player_size = 70
player_x = screen_width // 2 - player_size // 2
player_y = screen_height - player_size - 10
player_speed = 15

# Coins
coin_size = 35
coins = []
coin_speed = 5

# Obstacles
obstacle_size = 50
obstacles = []
obstacle_speed = 20

# Score
score = 0
font = pygame.font.Font(None, 36)

# Main game loop
running = True
clock = pygame.time.Clock()

# Game state
game_state = "running"

while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_size:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < screen_height - player_size:
        player_y += player_speed

    # Generate coins
    if random.randint(0, 100) < 2:
        coin_x = random.randint(0, screen_width - coin_size)
        coin_y = 0
        coins.append([coin_x, coin_y])

    # Generate obstacles
    if random.randint(0, 100) < 1:
        obstacle_x = random.randint(0, screen_width - obstacle_size)
        obstacle_y = 0
        obstacles.append([obstacle_x, obstacle_y])

    # Update coins
    for coin in coins:
        coin[1] += coin_speed
        pygame.draw.ellipse(screen, YELLOW, [coin[0], coin[1], coin_size, coin_size])
        # Collision detection with player
        if (player_x < coin[0] + coin_size and player_x + player_size > coin[0] and
                player_y < coin[1] + coin_size and player_y + player_size > coin[1]):
            coins.remove(coin)
            score += 1

    # Update obstacles
    for obstacle in obstacles:
        obstacle[1] += obstacle_speed
        pygame.draw.rect(screen, RED, [obstacle[0], obstacle[1], obstacle_size, obstacle_size])
        # Collision detection with player
        if (player_x < obstacle[0] + obstacle_size and player_x + player_size > obstacle[0] and
                player_y < obstacle[1] + obstacle_size and player_y + player_size > obstacle[1]):
            game_state = "game_over"

    # Draw player
    pygame.draw.rect(screen, BLUE, [player_x, player_y, player_size, player_size])

    # Display score
    score_text = font.render("Score: " + str(score), True, BLUE)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Limit frames per second
    clock.tick(30)

    # Game over
    if game_state == "game_over":
        game_over_text = font.render("Game Over", True, RED)
        screen.blit(game_over_text, (screen_width // 2 - 100, screen_height // 2 - 50))
        
        score_text = font.render("Final Score: " + str(score), True, RED)
        screen.blit(score_text, (screen_width // 2 - 120, screen_height // 2))
        
        pygame.display.flip()

        # Wait for a few seconds before exiting
        pygame.time.wait(2000)

        running = False

# Quit Pygame
pygame.quit()
