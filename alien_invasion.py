import sys
import pygame


class AlienInvasion:
    """Class to manage assets and behavior"""

    def __init__(self):
        """Init the game, generate game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("OH NOEZ ALIENZ!")

        # Set the background color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Watch for mouse/kb events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redrawing the screen each pass through the loop.
            self.screen.fill(self.bg_color)

            # Make the most recently drawn screen avaliable
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()  # LOL FORGOT PARENS HERE DIDNT WORK KTHNX
