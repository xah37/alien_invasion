import pygame


class Ship:
    """Class to manage a the ship"""

    def __init__(self, ai_game):
        """Init the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.

        self.image = pygame.image.load('assets/ship.bmp')
        self.rect = self.image.get_rect()
        # Start each new ship at bottom center
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw ship at its current location"""
        self.screen.blit(self.image, self.rect)
