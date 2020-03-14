import pygame
import time
import random


class Snake():

	def __init__(self, surface, first_colour, second_colour, display_width, display_height, x, y):
		self.surface = surface
		self.first_colour = first_colour
		self.second_colour = second_colour
		self.display_width = display_width
		self.display_height = display_height
		self.direction = ["right", "right", "right", "right", "right"]
		self.body = [(329, 275), (353, 275), (377, 275), (401, 275), (425, 275)]
		self.turns = {}
		self.head = self.body[len(self.body)-1]
		self.head_direction = self.direction[len(self.direction)-1]
		
	def create_body_background(self, apple_width, apple_height):
		beginning_height = self.display_height*2//3 - 50
		ending_height = self.display_height//2 - apple_height
		starting_width = self.display_width//2-apple_width
		ending_width = self.display_width//2+apple_width
		first_circle_radius = 10
		next_circle = 15

		last_row = (beginning_height-ending_height)//(next_circle)+1
		for k in range((beginning_height-ending_height)//(next_circle)+2):
			if k%2==0:
				beginning_width = self.display_width//2-apple_width
				if k == last_row:
					for b in range(int(ending_width-beginning_width)//next_circle//2):
						if b == (ending_width-beginning_width)//next_circle//2:
							pygame.draw.circle(self.surface, self.first_colour, (beginning_width, beginning_height), int(first_circle_radius*1.2))
							pygame.draw.circle(self.surface, self.second_colour, (beginning_width, beginning_height), int(first_circle_radius*1.2), 2)
							snake_head = (beginning_width, beginning_height-next_circle, first_circle_radius)
							return snake_head

						pygame.draw.circle(self.surface, self.first_colour, (beginning_width, beginning_height), first_circle_radius)
						pygame.draw.circle(self.surface, self.second_colour, (beginning_width, beginning_height), first_circle_radius, 2)
						beginning_width += next_circle

				else:
					for i in range((ending_width-beginning_width)//next_circle):
						pygame.draw.circle(self.surface, self.first_colour, (beginning_width, beginning_height), first_circle_radius)
						pygame.draw.circle(self.surface, self.second_colour, (beginning_width, beginning_height), first_circle_radius, 2)
						beginning_width += next_circle
			elif k == 3 or k==7:
				pygame.draw.circle(self.surface, self.first_colour, (starting_width-first_circle_radius, beginning_height), first_circle_radius)
				pygame.draw.circle(self.surface, self.second_colour, (starting_width-first_circle_radius, beginning_height), first_circle_radius, 2)
			elif k==1 or k==5 or k==9:
				pygame.draw.circle(self.surface, self.first_colour, (ending_width-next_circle, beginning_height), first_circle_radius)
				pygame.draw.circle(self.surface, self.second_colour, (ending_width-next_circle, beginning_height), first_circle_radius, 2)
			beginning_height -= next_circle
		return snake_head

	def create_head_background(self, x, y, radius, white, black, bright_red, sky_blue):
		pygame.draw.rect(self.surface, bright_red, (x+radius, y+radius//2, radius*3, radius*2))
		pygame.draw.polygon(self.surface, sky_blue, [(x+radius+radius*3, y+radius//2), (x+radius+radius*3, y+radius//2+radius*2), (x+radius+radius*3//2, y+radius//2+radius-2)])

		eyeball_position = (x+radius, y+radius)
		pygame.draw.circle(self.surface, white, (x+radius, y+radius//2), radius)
		pygame.draw.circle(self.surface, black, (x+radius+radius//4, y+radius//2), radius//2)

		pygame.draw.circle(self.surface, white, (x+radius, int(y+radius*2)), radius)
		pygame.draw.circle(self.surface, black, (x+radius+radius//4, int(y+radius*2)), radius//2)

	def create_snake(self, radius, white, black, bright_red, sky_blue):

		x = self.body[len(self.body)-1][0]
		y = self.body[len(self.body)-1][1]

		for a in range(len(self.body)-1):
			pygame.draw.circle(self.surface, self.first_colour, (self.body[a][0], self.body[a][1]), radius)
			pygame.draw.circle(self.surface, self.second_colour, (self.body[a][0], self.body[a][1]), radius, 2)

		pygame.draw.circle(self.surface, self.first_colour, (x, y), radius)
		pygame.draw.circle(self.surface, self.second_colour, (x, y), radius, 2)

		eye_ball_radius = int(radius//1.5)

		if self.head_direction == "right":
			eyeball_position_one = (x+eye_ball_radius, y-eye_ball_radius)
			eyeball_position_two = (x+eye_ball_radius, y+eye_ball_radius)
		elif self.head_direction == "left":
			eyeball_position_one = (x-eye_ball_radius, y-eye_ball_radius)
			eyeball_position_two = (x-eye_ball_radius, y+eye_ball_radius)
		elif self.head_direction == "up":
			eyeball_position_one = (x+eye_ball_radius, y-eye_ball_radius)
			eyeball_position_two = (x-eye_ball_radius, y-eye_ball_radius)
		elif self.head_direction == "down":
			eyeball_position_one = (x+eye_ball_radius, y+eye_ball_radius)
			eyeball_position_two = (x-eye_ball_radius, y+eye_ball_radius)
		
		pygame.draw.circle(self.surface, white, (eyeball_position_one), eye_ball_radius)
		pygame.draw.circle(self.surface, black, (eyeball_position_one), eye_ball_radius//2)

		pygame.draw.circle(self.surface, white, (eyeball_position_two), eye_ball_radius)
		pygame.draw.circle(self.surface, black, (eyeball_position_two), eye_ball_radius//2)

	def update(self):

			for a in range(0, len(self.body)):

				if self.body[a] in self.turns:
					self.direction[a] = self.turns[self.body[a]]
					if a == 0:
						del self.turns[self.body[a]]

				if self.direction[a] == "right":
					self.body[a] = (self.body[a][0]+2, self.body[a][1])
				elif self.direction[a] == "left":
					self.body[a] = (self.body[a][0]-2, self.body[a][1])
				elif self.direction[a] == "up":
					self.body[a] = (self.body[a][0], self.body[a][1]-2)
				elif self.direction[a] == "down":
					self.body[a] = (self.body[a][0], self.body[a][1]+2)

			self.head = self.body[-1]
			self.head_direction = self.direction[-1]	
		