import pygame
import constants as c
from logger import log_state

def main():
    pygame.init()
    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f'''Screen width: {c.SCREEN_WIDTH}
Screen height: {c.SCREEN_HEIGHT}''')

    while True:
        log_state()
        for event in pygame.event.get():
            pass
        screen.fill(("black"))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

if __name__ == "__main__":
    main()
