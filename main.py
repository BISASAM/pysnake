import sys
import pygame
from pygame.locals import *
from player import Player
from item import Item
import global_vars as gv


def events():
	# quit event
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	# player events
	for p in gv.players:
		p.events()


def update():
	# time between two frames
	gv.elapsed_time = gv.clock.tick() / 1000

	# use reversed iterator to make list deletions possible
	for p in reversed(gv.players):
		p.update()

	for i in reversed(gv.items):
		i.update()


def draw():
	# clear screen
	gv.game_screen.fill(gv.black)

	# draw all elements
	for p in gv.players:
		p.draw()
	for i in gv.items:
		i.draw()

	# update screen
	pygame.display.update()


if __name__ == "__main__":

	# init game screen
	pygame.init()
	pygame.display.set_caption('PySnake!')
	gv.game_screen = pygame.display.set_mode((800, 600))

	# init players
	gv.players.append(Player(gv.blue, K_LEFT, K_RIGHT))
	# gv.players.append(Player(gv.red, K_a, K_s))

	# init items
	gv.items.append(Item('slow', 20))
	gv.items.append(Item('fast', 20))

	while True:
		events()
		update()
		draw()
