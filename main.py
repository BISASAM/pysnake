import pygame
import global_vars as gv


# init game screen
pygame.init()
pygame.display.set_caption('PySnake!')
gv.game_screen = pygame.display.set_mode((800, 600))

# this import requires an active game_screen
from game_scene import GameScene

# set entry scene here!
active_scene = GameScene()

while active_scene != None:
	# clear screen
	gv.game_screen.fill(gv.black)

	active_scene.events()
	active_scene.update()
	active_scene.draw()

	active_scene = active_scene.next

	# update screen
	pygame.display.update()



