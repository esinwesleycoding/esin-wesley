# Initialize Pygame and screen dimensions
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

# Initialize display surface and set title
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Adding image and background image')

# Initialize font, render text, and set text position
text = pygame.font.FOnt(None, 36).render('Hello World', True, pygame.Color('black'))
text_rect = text.get_rect(center=SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110)
running = True
while running:
    for event.type == pygame.QUIT:
running = False

display_surface.blit(background_image, (0, 0))
display_surface.blit(penguin_rect)
display_surface.blit(text, text_rect)

pygame.display.flip()
clock.tick(30)

pygame.quit()