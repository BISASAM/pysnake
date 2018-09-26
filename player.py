import numpy as np
import pygame
from pygame.locals import *
from random import randint
import global_vars as gv


class Player():

	def __init__(self, color, left_key, right_key):
		self.width, self.height = gv.game_screen.get_size()  # instance attributes
		self.pos = np.array([randint(20, self.width-20), randint(20, self.height-20)])
		self.color = color
		self.r = np.array([1., 0.])  # Richtungsvektor

		self.tail = []
		self.tail.append(self.pos.astype(int))
		self.left = left_key
		self.right = right_key
		self.turn_speed = 5
		self.speed = 100
		self.thickness = 8

	def events(self):
		keys = pygame.key.get_pressed()

		n = np.array([-self.r[1], self.r[0]])
		if keys[self.left]:
			self.r -= n * gv.elapsed_time * self.turn_speed
		if keys[self.right]:
			self.r += n * gv.elapsed_time * self.turn_speed
		self.r /= np.linalg.norm(self.r)

	def update(self):
		self.collision()

		self.pos = self.pos + self.r * gv.elapsed_time * self.speed
		self.pos[0] %= self.width
		self.pos[1] %= self.height
		self.tail.append(self.pos.astype(int))

	def draw(self):
		pygame.draw.lines(gv.game_screen, self.color, False, self.tail, self.thickness)
		pygame.draw.circle(gv.game_screen, self.color, self.pos.astype(int), int(self.thickness/2))

	def change_speed(self, speed_factor, turn_factor):
		self.speed *= speed_factor
		self.turn_speed *= turn_factor

	def change_thickness(self, factor):
		self.thickness *= factor

	def collision(self):
		for item in gv.items:
			if np.linalg.norm(self.pos - item.pos) < 15:
				self.item_eaten(item.power)
				item.remove_from_list()

	def item_eaten(self, power):
		if power == 'slow':
			self.change_speed(.5, .5)
		elif power == 'fast':
			self.change_speed(2, 2)
		elif power == 'thin':
			self.change_thickness(.5)
		elif power == 'thick':
			self.change_thickness(2)


