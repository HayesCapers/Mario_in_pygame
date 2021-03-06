import pygame
from pygame.sprite import Sprite

class Block(Sprite):
	def __init__(self, screen, start_x):
		super(Block,self).__init__()
		self.x = start_x
		self.y = 245
		self.screen = screen
		self.image = pygame.image.load('./mario_pics/question_block.png')
		self.image = pygame.transform.scale(self.image, (27, 27))
		self.should_move_left = False
		self.should_move_right = False

	def draw_block(self, mario):
		if self.should_move_left:
			self.x += mario.speed
		elif self.should_move_right:
			self.x -= mario.speed
		self.screen.blit(self.image, [self.x,self.y])
		
	def should_move(self, direction, true_or_false):
		if direction == 'up':
			self.should_move_up = true_or_false
		if direction == 'right':
			self.should_move_right = true_or_false
		elif direction == 'left':
			self.should_move_left = true_or_false

	# def update_x(self, background):
	# 	self.x = background.x - self.x
	# 	return self.x