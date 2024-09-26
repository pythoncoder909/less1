import pygame
import sys

# Initialize Pygame
pygame.init()

# Define screen dimensions and colors
screen_width, screen_height = 800, 600
white = (255, 255, 255)
black = (0, 0, 0)

# Create the display window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pygame Text Display')

# Load fonts with different sizes
font1 = pygame.font.SysFont('Arial', 60)
font2 = pygame.font.SysFont('Comic Sans MS', 40)
font3 = pygame.font.SysFont('Times New Roman', 50)

# Define text surfaces
text1 = font1.render('Hello, World!', True, black)
text2 = font2.render('Welcome to Pygame!', True, black)
text3 = font3.render('This is fun!', True, black)

# Get text positions
text1_rect = text1.get_rect(center=(screen_width // 2, screen_height // 4))
text2_rect = text2.get_rect(center=(screen_width // 2, screen_height // 2))
text3_rect = text3.get_rect(center=(screen_width // 2, 3 * screen_height // 4))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with white color
    screen.fill(white)

    # Draw text to the screen
    screen.blit(text1, text1_rect)
    screen.blit(text2, text2_rect)
    screen.blit(text3, text3_rect)

    # Update the display
    pygame.display.update()
    