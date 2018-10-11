import sys
import pygame
from pygame.locals import *
from player import Player
from item import Item
import global_vars as gv
from scene_base import SceneBase
from item_handler import ItemHandler


class GameScene(SceneBase):
	def __init__(self):
		SceneBase.__init__(self)

		# init players
		gv.players.append(Player(gv.blue, K_LEFT, K_RIGHT))
		# gv.players.append(Player(gv.red, K_a, K_s))

		# init ItemHandler
		self.item_handler = ItemHandler()

	def events(self):

		# quit event
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		# player events
		for p in gv.players:
			p.events()

	def update(self):
		# time between two frames
		gv.elapsed_time = gv.clock.tick() / 1000

		# use reversed iterator to make list deletions possible
		for p in reversed(gv.players):
			p.update()

		self.item_handler.update()

	def draw(self):

		# draw all elements
		for p in gv.players:
			p.draw()
		for i in gv.items:
			i.draw()

