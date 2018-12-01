import pygame
import global_vars as gv


class SceneBase:
	def __init__(self):
		self.next = self

	def events(self):
		print("uh-oh, you didn't override this in the child class")

	def update(self):
		print("uh-oh, you didn't override this in the child class")

	def draw(self):
		print("uh-oh, you didn't override this in the child class")

	def switch_to_scene(self, next_scene):
		self.next = next_scene

	def terminate(self):
		self.switch_to_scene(None)