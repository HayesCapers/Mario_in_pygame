import pygame

class Background(object):
	def __init__(self, screen, image, mario):
		self.x = 0
		self.y = 0
		self.floor = 290
		self.death_floor = 385
		self.screen = screen
		self.image = pygame.image.load(image)
		self.image = pygame.transform.scale(self.image, (6544, 743))
		self.should_move_down = False
		self.should_move_left = False
		self.should_move_right = False
		self.solid_ground = {
		'1': [0, -1899],
		'2': [-1976, -2424],
		'3': [-2531, -4489],
		'4': [-4571, -6000]
		}
		self.holes = {
		'1': [-1900, -1975],
		'2': [-2425, -2530],
		'3': [-4490, -4570]
		}
		#spawn points have to be divisible by marios speed!
		self.goomba_spawn_points = [-500, -516, -700, -1000, -2000]
		self.block_locations = [-500]

	def draw_background(self, mario):
		if mario.alive:
			if self.should_move_left:
				self.x += mario.speed
			elif self.should_move_right:
				self.x -= mario.speed	
		elif mario.alive == False:
			self.x = self.x
		self.screen.blit(self.image, [self.x, self.y])

	def should_move(self, direction, true_or_false):	
		if direction == 'left':
			self.should_move_left = true_or_false
		elif direction == 'right':
			self.should_move_right = true_or_false		

