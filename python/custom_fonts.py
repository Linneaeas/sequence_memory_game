import pygame
import sys
import os

def main():
    try:
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Custom Fonts Demo')

        # Example of using a custom font
        # First, try to load a custom font from shared directory
        custom_font = None
        try:
            # Try to load a custom font if it exists
            custom_font = pygame.font.Font('shared/custom_font.ttf', 36)
        except:
            # If no custom font is found, use a built-in font
            custom_font = pygame.font.SysFont('comicsansms', 36)
            print("No custom font found in shared directory. Using Comic Sans MS as fallback.")

        # Main loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            # Clear the screen
            screen.fill((0, 0, 0))

            # Display text with custom font
            text = custom_font.render("Hello! This is a custom font!", True, (255, 255, 255))
            screen.blit(text, (100, 300))

            pygame.display.flip()
            pygame.time.delay(100)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    main() 