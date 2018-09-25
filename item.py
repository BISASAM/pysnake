import numpy as np
import pygame
from pygame.locals import *
from random import randint
import global_vars as gv


class Item():

	def __init__(self, power, life_time):

		self.look = gv.types[power]
		self.width, self.height = gv.game_screen.get_size()
		self.pos = np.array([randint(20, self.width - 20), randint(20, self.height - 20)])
		self.life_time = life_time
		self.timer = 0
		self.power = power

	def update(self):

		self.timer += gv.elapsed_time
		if self.timer > self.life_time:
			self.remove_from_list()

	def draw(self):
		pygame.draw.rect(gv.game_screen, self.look, (*self.pos, 20, 20))

	def remove_from_list(self):
		gv.items.remove(self)
