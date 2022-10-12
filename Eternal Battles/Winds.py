import pygame


SCREEN_WIDTH = 1080
SCREEN_HIGHT = 720
DECK_WIN_W = 1080
DECK_WIN_H = 720
FPS= 60
clock =pygame.time.Clock()

DECK_WIN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HIGHT))
WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
SELECT_DECK = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
GAME_WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
pygame.display.set_caption("Eternal Battles")



def Draw_Background(Color):
    WIN.fill(Color)
    