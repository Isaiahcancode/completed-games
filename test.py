import pygame

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Image Display Example")
clock = pygame.time.Clock()

# Load the image (ensure the file is in the same folder or provide the full path)
image = pygame.image.load("explode.png")  # Replace with your image path

# Get the image's size
image_rect = image.get_rect()

# Pygame main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a background color
    screen.fill((255, 255, 255))

    # Draw the image at position (100, 100)
    screen.blit(image, (100, 100))

    pygame.display.flip()  # Update the display
    clock.tick(30)

pygame.quit()
