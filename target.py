# Target By Brandon Riley
# 11/30/17
# draws a target with five rings
import pygame


class Target:
    def __init__(self, main_surface):
        self.main_surface = main_surface

    def draw_target(self):
        """
        Draws a five ringed target in the middle of the window
        :return:
        """
        pygame.draw.circle(self.main_surface, (255, 255, 255), (500, 500), 375)  # white
        pygame.draw.circle(self.main_surface, (0, 0, 0), (500, 500), 375, 3)  # black ring around the white circle
        pygame.draw.circle(self.main_surface, (0, 0, 0), (500, 500), 300)  # black
        pygame.draw.circle(self.main_surface, (0, 0, 200), (500, 500), 225)  # blue
        pygame.draw.circle(self.main_surface, (255, 0, 0), (500, 500), 150)  # red
        pygame.draw.circle(self.main_surface, (255, 255, 0), (500, 500), 75)  # yellow
        pygame.display.update()
