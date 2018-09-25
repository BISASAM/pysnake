import pygame

blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)
clock = pygame.time.Clock()
elapsed_time = 0
players = []
items = []
game_screen = 0

types = {
			"slow": (236, 112, 99), "fast": (82, 190, 128),
			"thin": (255, 255, 0), "thick": (36, 113, 163)
		}