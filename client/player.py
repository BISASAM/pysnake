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
		self.active_items = []

		# hole creation
		self.timer = 0
		self.hole_creation_time = 3
		self.hole_creation_time_range = (1, 5)  # min, max
		self.hole_distance = 0
		self.hole_distance_range = (10, 100)  # min, max
		self.draw_hole = False

		self.thickness = 8
		self.tail = []
		self.tail.append((self.pos.astype(int), self.pos.astype(int), self.thickness))
		self.left = left_key
		self.right = right_key
		self.turn_speed = 5
		self.speed = 100

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
		self.update_tail()

	def draw(self):
		for start_p, end_p, thick in self.tail:
			pygame.draw.line(gv.game_screen, self.color,  start_p, end_p, thick)
		pygame.draw.circle(gv.game_screen, self.color, self.pos.astype(int), int(self.thickness/2))

	def update_tail(self):
		self.timer += gv.elapsed_time
		if self.timer > self.hole_creation_time and not self.draw_hole:
			self.draw_hole = True
			self.hole_creation_time = randint(*self.hole_creation_time_range)
			self.hole_distance = randint(*self.hole_distance_range)

		if self.draw_hole:
			if np.linalg.norm(self.pos - self.tail[-1][1]) > self.hole_distance:
				self.draw_hole = False
				self.timer = 0

		# update tail
		old_pos = self.pos
		self.pos = self.pos + self.r * gv.elapsed_time * self.speed
		if not self.draw_hole:
			self.tail_append(old_pos)

	def tail_append(self, old_pos):

		rest_1, self.pos[0] = divmod(self.pos[0], self.width)
		rest_2, self.pos[1] = divmod(self.pos[1], self.height)

		# check if out of margin
		if rest_1 != 0 or rest_2 != 0:
			aux_pos_1 = old_pos
			aux_pos_2 = old_pos

			if rest_1 > 0:
				aux_pos_1[0] = self.width
				aux_pos_2[0] = 0
			elif rest_1 < 0:
				aux_pos_1[0] = 0
				aux_pos_2[0] = self.width

			if rest_2 > 0:
				aux_pos_1[1] = self.height
				aux_pos_2[1] = 0
			elif rest_2 < 0:
				aux_pos_1[1] = 0
				aux_pos_2[1] = self.height

			self.tail.append((old_pos.astype(int), aux_pos_1.astype(int), self.thickness))
			self.tail.append((aux_pos_2.astype(int), self.pos.astype(int), self.thickness))
		else:
			self.tail.append((old_pos.astype(int), self.pos.astype(int), self.thickness))


	def change_speed(self, speed_factor, turn_factor):
		self.speed *= speed_factor
		self.turn_speed *= turn_factor

	def change_thickness(self, factor):
		self.thickness = int(self.thickness * factor)
		self.thickness = 1 if self.thickness == 0 else self.thickness

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


