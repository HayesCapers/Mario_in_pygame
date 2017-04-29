import pygame
import sys
from random import randint
from game_functions import check_events
from background import Background
from mario import Mario
from physics import Physics
from goomba import Goomba
from block import Block
from pygame.sprite import Group


def run_game():
	pygame.init()


	screen_size = (600, 385)
	screen = pygame.display.set_mode(screen_size)
	mario = Mario(screen)
	background = Background(screen, './mario_pics/full_background_no_sky.png', mario)
	question_block = Block(screen, 300)
	physics = Physics()
	# first_goomba = Goomba(screen)
	enemies = Group()
	game_on = True
	tick = 0
	background_color = (93,148,251)
	# r = randint(0, 255)
	# g = randint(0,255)
	# b = randint(0,255)
	
	
	
	while game_on == True:
		# tick += 1
		# background_color = (r, g, b)
		# if tick % 5 == 0:
		# 	r += 10
		# 	g += 15
		# 	b += 16
		# if r > 230:
		# 	r -= 150
		# if g > 230:
		# 	g -= 150
		# if b > 230:
		# 	b -= 150
	
		# print tick
		for i in background.goomba_spawn_points:
			if background.x == i:
				enemies.add(Goomba(screen))
		check_events(background, mario, question_block, screen)
		screen.fill(background_color)
		background.draw_background(mario)
		mario.draw_mario(physics, background)
		question_block.draw_block(mario)
		print enemies		
		for enemy in enemies:
			enemy.draw_goomba(mario, physics, background)
			mario.check_mario_is_alive(background, enemy)
		# first_goomba.draw_goomba(mario)
		
		pygame.display.flip()

run_game()		

	