import pygame
from math import fabs

class Mario(object):
	def __init__(self, screen):
		#///////////////////
		#//////IMAGES//////
		#/////////////////
		self.mario_stand = pygame.image.load('./mario_pics/Mario_stand.png')
		self.mario_stand_scale = pygame.transform.scale(self.mario_stand, (55, 44))
		#right mvoement images
		self.mario_move_1_load = pygame.image.load('./mario_pics/mario_move_1.png')
		self.mario_move_1 = pygame.transform.scale(self.mario_move_1_load, (44, 44))
		self.mario_move_2_load = pygame.image.load('./mario_pics/mario_move_2.png')
		self.mario_move_2 = pygame.transform.scale(self.mario_move_2_load, (44, 44))
		self.mario_move_3_load = pygame.image.load('./mario_pics/mario_move_3.png')
		self.mario_move_3 = pygame.transform.scale(self.mario_move_3_load, (44, 44))
		#left movement images
		self.mario_left_1_load = pygame.image.load('./mario_pics/mario_move_1_left.png')
		self.mario_left_1 = pygame.transform.scale(self.mario_left_1_load, (44, 44))
		self.mario_left_2_load = pygame.image.load('./mario_pics/mario_move_2_left.png')
		self.mario_left_2 = pygame.transform.scale(self.mario_left_2_load, (44, 44))
		self.mario_left_3_load = pygame.image.load('./mario_pics/mario_move_3_left.png')
		self.mario_left_3 = pygame.transform.scale(self.mario_left_3_load, (44, 44))
		#jumping
		self.mario_jump_right_load = pygame.image.load('./mario_pics/mario_jump_right.png')
		self.mario_jump_right = pygame.transform.scale(self.mario_jump_right_load, (44, 44))
		self.mario_jump_left_load = pygame.image.load('./mario_pics/mario_jump_left.png')
		self.mario_jump_left = pygame.transform.scale(self.mario_jump_left_load, (44, 44))
		#Dead
		self.mario_dead_load = pygame.image.load('./mario_pics/mario_death.png')
		self.mario_dead = pygame.transform.scale(self.mario_dead_load, (44, 44))	
		#/////////////////
		#///ATTRIBUTES///
		#///////////////
		self.x = 200
		self.y = 290
		self.speed = 4
		self.jump_speed = 15
		self.max_jump_height = 175
		self.screen = screen
		self.should_move_up = False
		self.should_move_right = False
		self.should_move_left = False
		self.mario_moves_right = [self.mario_move_1, self.mario_move_2, self.mario_move_3, self.mario_jump_right]
		self.mario_moves_left = [self.mario_left_1, self.mario_left_2, self.mario_left_3, self.mario_jump_left]
		self.move_timer = 0	
		self.alive = True
		self.fall = False		

	def draw_mario(self, physics, background):

		def update_timer():
			if self.should_move_right:
				self.move_timer += 1
				if self.move_timer > 30:
					self.move_timer = 0
			elif self.should_move_left:
				self.move_timer += 1
				if self.move_timer > 30:
					self.move_timer = 0
		if self.alive:
			update_timer()
			if self.should_move_up:
				self.y -= self.jump_speed - physics.gravity
			elif self.should_move_up == False:
				self.y += physics.gravity
			if self.y <= self.max_jump_height:
				self.should_move_up = False
				self.y += self.speed
			self.should_fall(background)			
			self.screen.blit(self.image_selector(self.move_timer), [self.x, self.y])
		elif self.alive == False:
			self.y = 250
			self.screen.blit(self.mario_dead, [self.x, self.y])
			

		# print self.move_timer
		# print background.x
		


	def should_move(self, direction, true_or_false):
		if direction == 'up':
			self.should_move_up = true_or_false
		if direction == 'right':
			self.should_move_right = true_or_false
		elif direction == 'left':
			self.should_move_left = true_or_false
						
	def image_selector(self, timer):
		current_image_right = self.mario_moves_right[0]
		current_image_left = self.mario_moves_left[0]
		mario_jump_right_currently = self.mario_moves_right[3]
		mario_jump_left_currently = self.mario_moves_left[3]
		if self.should_move_up and self.should_move_right:
			return mario_jump_right_currently
		elif self.should_move_up and self.should_move_left:
			return mario_jump_left_currently

		while self.should_move_right and (self.should_move_up == False):
			if (timer > 0) and (timer <= 10):
				current_image_right = self.mario_moves_right[0]
			elif (timer > 10) and (timer <= 20):
				current_image_right = self.mario_moves_right[1] 
			elif (timer > 20) and (timer <= 30):
				current_image_right = self.mario_moves_right[2] 
			return current_image_right
		while self.should_move_left and (self.should_move_up == False):
			if (timer > 0) and (timer <= 10):
				current_image_left = self.mario_moves_left[0]
			elif (timer > 10) and (timer <= 20):
				current_image_left = self.mario_moves_left[1]
			elif (timer > 20) and (timer <= 30):
				current_image_left = self.mario_moves_left[2]
			return current_image_left
		else:
			timer = 0
			return self.mario_stand_scale

	def should_fall(self, background):
		# for i in background.holes:
		# 	if background.x < background.holes[i][0] and background.x > background.holes[i][1]:
		# 		self.y += physics.gravity
		for i in background.solid_ground:
			if background.x <= background.solid_ground[i][0] and background.x >= background.solid_ground[i][1]:
				if self.y > background.floor:
					self.y = background.floor
		for i in background.holes:	
				if (self.x > background.floor + 20):
					if (background.x <= background.holes[i][1] + 20) and (background.x > background.holes[i][1]-50):
						background.x = background.holes[i][1] + 20

	def check_mario_is_alive(self, background, enemy):
		distance_from_enemy = fabs(self.x - enemy.x) + fabs(self.y - enemy.y)
		if self.y >= background.death_floor:
			self.alive = False
		if distance_from_enemy < 20:
			enemy.x = self.x - 20
			self.alive = False
		return self.alive


















