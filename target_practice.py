# Target Practice By Brandon Riley
# 11/30/17
# Lets you "shoot arrows" at a target and counts your score

import target
import pygame
import sys
from pygame.locals import *


def print_score(main_surface, score):
    """
    Covers original score and prints updated score in top right corner
    :param main_surface: the main drawing surface
    :param score: old score
    :return: The score of your "shot"
    """
    pygame.draw.rect(main_surface, (255, 255, 255), (0, 0, 275, 200))
    my_font = pygame.font.SysFont("helvetica", 75)
    score_label = my_font.render("Score:", 1, (0, 0, 0))
    main_surface.blit(score_label, (10, 10))
    actual_score = my_font.render(str(score), 1, (0, 0, 0))
    main_surface.blit(actual_score, (175, 12))
    pygame.display.update()
    return score


def main():
    #  sets up window
    number_of_clicks = 0
    pygame.init()
    main_surface = pygame.display.set_mode((1000, 10000), 0, 32)
    pygame.display.set_caption("Target Practice")
    main_surface.fill((255, 255, 255))
    my_target = target.Target(main_surface)
    my_target.draw_target()
    score = 0
    print_score(main_surface, score)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                #  closes window when pressing the quit button
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                #  checks where the mouse was clicked and adds the score to the top corner 
                mouse_position = pygame.mouse.get_pos()
                height_by_base = (500 - mouse_position[0]) ** 2 + (500 - mouse_position[1]) ** 2
                distance_from_center = height_by_base ** .5
                number_of_clicks += 1
                if number_of_clicks < 6:
                    if distance_from_center < 75:
                        score += 9
                        print_score(main_surface, score)
                    elif 75 < distance_from_center < 150:
                        score += 7
                        print_score(main_surface, score)
                    elif 150 < distance_from_center < 225:
                        score += 5
                        print_score(main_surface, score)
                    elif 225 < distance_from_center < 300:
                        score += 3
                        print_score(main_surface, score)
                    elif 300 < distance_from_center < 375:
                        score += 1
                        print_score(main_surface, score)
                if number_of_clicks == 5:
                    # checks to see if you have clicked five times and prompts the end game screen
                    pygame.draw.rect(main_surface, (255, 255, 255), (0, 0, 1000, 1500))
                    my_font = pygame.font.SysFont("helvetica", 75)
                    next_screen = my_font.render("Click to get final score", 1, (0, 0, 0))
                    main_surface.blit(next_screen, (225, 500))
                    pygame.display.update()
                elif number_of_clicks >= 6:
                    # pulls up the end game screen 
                    pygame.draw.rect(main_surface, (0, 0, 0), (0, 0, 1000, 1500))
                    my_font = pygame.font.SysFont("helvetica", 200)
                    game_over = my_font.render("GAME OVER", 1, (255, 255, 255))
                    main_surface.blit(game_over, (75, 250))
                    final_score = score
                    final_score_font = pygame.font.SysFont("helvetica", 100)
                    final_score_text = final_score_font.render("Final Score:", 1, (255, 255, 255))
                    main_surface.blit(final_score_text, (300, 425))
                    end_score = my_font.render(str(final_score), 1, (255, 255, 255))
                    main_surface.blit(end_score, (425, 525))
                    pygame.display.update()


main()
