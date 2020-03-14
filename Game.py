from Draw_Snake import *

import pygame
import time

def arrange_turns(player_snake, direction, x, y):
	"""Returns a set of co-ordinates that is then added to the player snake's turns. This is a co-ordinate at which each part of the snake's body must change direction"""
	new_x = x%100
	new_y = y%100
	hundred_x = x//100*100
	hundred_y = y//100*100
	return_x = None
	return_y = None

	#Set a turn at a specific co-ordinate, if the user wants to go right or left, based on the current direction their snake is going in.
	if direction == "right" or direction == "left":
		if player_snake.head_direction == "up":
			if new_y >=25 and new_y <75:
				return_y = hundred_y+25
			elif new_y >=75:
				return_y = (hundred_y+100)-25
			elif new_y < 25:
				return_y = hundred_y-25
			
		elif player_snake.head_direction == "down":
			if new_y <=25:
				return_y = hundred_y+25
			elif new_y >75:
				return_y = hundred_y+100+25
			elif (new_y >25 and new_y < 75) or new_y==75:
				return_y = hundred_y+100-25

	#Set a turn at a specific co-ordinate, if the user wants to go either up or down, based on the current direction their snake is going in.
	if direction == "up" or direction == "down":
		if player_snake.head_direction == "right":
			if new_x <=25:
				return_x = hundred_x+25
			elif new_x >75:
				return_x = hundred_x+100+25
			elif (new_x >25 and new_x <75) or new_x==75:
				return_x = hundred_x+100-25
		elif player_snake.head_direction == "left":
			if new_x <25:
				return_x = hundred_x-25
			elif new_x >= 75:
				return_x = hundred_x+100-25
			elif (new_x >=25 and new_x <75) or new_x == 25:
				return_x = hundred_x + 25

	if return_y == None:
		return_y = y
	if return_x == None:
		return_x = x

	return (return_x, return_y)

def crashed(game_display, colours, display_height, display_width):
	
	not_clicked = True
	while not_clicked:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		create_background(game_display, colours, display_height, display_width)
		action_one = create_button("Play Again!", game_display, display_width/8, display_height*6.5/10, 200, 100, colours["dark_green"], colours["bright_green"])
		action_two = create_button("Quit Game!", game_display, display_width*5/8, display_height*6.5/10, 200, 100, colours["red"], colours["bright_red"])
		
		if action_one == True:
			return
		elif action_two == True:
			pygame.quit()
			quit()

		small_text = pygame.font.Font(None, 30)
		large_text = pygame.font.Font(None, 70)
		text_surface, text_rectangle = text_object("You crashed!", large_text)
		text_surface_two, text_rectangle_two = text_object("Please choose to play again or quit", small_text)
		text_rectangle.center = (display_width/2, display_height*2/5)
		text_rectangle_two.center = (display_width/2, display_height*2/5+50)
		game_display.blit(text_surface, text_rectangle)
		game_display.blit(text_surface_two, text_rectangle_two)

		pygame.display.update()
		clock.tick(15)


def create_apple(player_snake):
	"""Creates the image of the apple on the screen for the user by returning the x and y co-ordinate positions for the new apple. Since the 
		co-ordinates of the new apple cannot be within the body of the snake, the function runs recursively until a valid set of co-ordinates 
		have been generated. The hit position is +25 on the x-axis and +25 on the y-axis because the image creation begins on the top left of 
		the screen."""
	start_width = 150
	start_height = 50
	x_position, y_position = start_width+(random.randint(0,9)*50), start_height+(random.randint(0,9)*50)
	whether_inside = False

	for a in range(len(player_snake.body)):
		if ((player_snake.body[a][0]-8) < (x_position+25) and (player_snake.body[a][0]+8) > (x_position+25)) and ((player_snake.body[a][1]-8) < (y_position+25) and (player_snake.body[a][1]+8)>(y_position)):
			whether_inside = True
			break

	if whether_inside == True:
		return create_apple(player_snake)
	else:
		return (x_position+25, y_position+25), (x_position, y_position)

def create_background(game_display, colours, display_height, display_width):
	"""Creates the background of the snake game menu. The sky blue colour is for the sky, the green colours are for the field, and the snake and apple image are used to create the middle image."""
	game_display.fill(colours["sky_blue"])
	height = display_height*2//3 -50
	for a in range(height//50):
		x_position = 0
		if a%2==0:
			for i in range(display_width//50):
				if i%2==0:
					pygame.draw.rect(game_display, colours["bright_green"], (x_position,height,50,50))
				elif i%2==1:
					pygame.draw.rect(game_display, colours["green"], (x_position,height,50,50))

				x_position += 50

		elif a%2==1:
			for b in range(display_width//50):
				if b%2==0:
					pygame.draw.rect(game_display, colours["green"], (x_position,height,50,50))
				elif b%2==1:
					pygame.draw.rect(game_display, colours["bright_green"], (x_position, height,50,50))
				x_position +=50
		height += 50

def create_button(button_message, display, x, y, width, height, inactive_colour, active_colour):
	mouse_position = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	if (x + width > mouse_position[0] > x) and (y + height > mouse_position[1] > y):
		pygame.draw.rect(display, active_colour, (x, y, width, height))
		if click[0] == 1:
			return True
	else:
		pygame.draw.rect(display, inactive_colour, (x, y, width, height))

	button_font = pygame.font.Font(None, 40)
	text_surface, text_rectangle = text_object(button_message, button_font)
	text_rectangle.center = ((x+width/2), (y+height/2))
	display.blit(text_surface, text_rectangle)

def create_game_background(game_display, colours, display_width, display_height):
	"""Creates the game background in which the player will be moving in. The default sky blue represents the sky background whereas the green and light green is the 
		field that the snake is moving on"""

	game_display.fill(colours["sky_blue"])
	height = 50

	for a in range(10):
		x_position = 150
		if a%2==0:
			for i in range(10):
				if i%2==0:
					pygame.draw.rect(game_display, colours["bright_green"], (x_position,height,50,50))
				elif i%2==1:
					pygame.draw.rect(game_display, colours["green"], (x_position,height,50,50))
				x_position += 50
		elif a%2==1:
			for b in range(10):
				if b%2==0:
					pygame.draw.rect(game_display, colours["green"], (x_position,height,50,50))
				elif b%2==1:
					pygame.draw.rect(game_display, colours["bright_green"], (x_position, height,50,50))
				x_position +=50
		height += 50


def main_menu(display_width, display_height, game_display, colours):
	"""This is the main menu function that is called by the Game script. When run, this gives the user the option to either quit the game by pressing the red button or begin playing the game by pressing the green 'Start Game' button"""
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		create_background(game_display, colours, display_height, display_width)
		#Draws the snake into the background before the apple to give the effect of the snake being inside the apple
		apple_image = pygame.image.load("new_apple.png")
		apple_image.convert_alpha()
		apple_width, apple_height = (80, 63)

		snake_background = Snake(game_display, colours["orange"], colours["bright_orange"], display_width, display_height, 425, 550//2)
		snake_head_x, snake_head_y, radius = snake_background.create_body_background(apple_width, apple_height)
		snake_background.create_head_background(snake_head_x, snake_head_y, radius, colours["white"], colours["black"], colours["bright_red"], colours["sky_blue"])
		game_display.blit(apple_image, (display_width//2-apple_width//2, display_height//2-apple_height))

		large_text = pygame.font.Font(None, 70)
		text_surface, text_rectangle = text_object("Welcome to Snake Heaven", large_text)
		text_rectangle.center = (display_width/2, display_height/5)
		game_display.blit(text_surface, text_rectangle)

		#Creates the 'interactive' buttons that show a lighter colour when the user's mouse hovers above it. Since green signifies 'go' and red signifies 'stop', we have appropriately assigned these colours to the two buttons.
		action_one = create_button("Start Game!", game_display, display_width/8, display_height*6.5/10, 200, 100, colours["dark_green"], colours["bright_green"])
		action_two = create_button("Quit Game!", game_display, display_width*5/8, display_height*6.5/10, 200, 100, colours["red"], colours["bright_red"])
		
		if action_one == True:
			return 
		elif action_two == True:
			pygame.quit()
			quit()

		pygame.display.update()
		clock.tick(15)

def paused():
	large_text = pygame.font.Font(None, 115)
	text_surface, text_rectangle = text_objects("Paused", large_text)
	text_rectangle.center = (display_width//2, display_height*2//5)
	game_display.blit(text_surface, text_rectangle)
	
	while True:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p:
					return

		action_one = create_button("Resume!", game_display, display_width/8, display_height*6.5/10, 200, 100, colours["dark_green"], colours["bright_green"])
		action_two = create_button("Quit Game!", game_display, display_width*5/8, display_height*6.5/10, 200, 100, colours["red"], colours["bright_red"])
		
		if action_one == True:
			return
		elif action_two == True:
			pygame.quit()
			quit()

		pygame.display.update()
		clock.tick(15)

def show_score(count, black, game_display):
	"""Keeps track of the player's score based on the number of apples that have been eaten"""
	text = pygame.font.Font(None, 30).render("Happiness Level: {}".format(count), True, black)
	game_display.blit(text, (30,8))

def start_game(display_width, display_height, game_display, colours):
	"""This is the main game function that is run when the user clicks the 'play' button from the opening menu. While the snake has not exceeded
		the boundaries of the map or run into itself, the game will continue. The player's score will be kept track of in the top left corner of the
		display screen."""

	#Initialise the constant variables that we do not want to reset inside the game. This includes the apple, player's snake and score.
	clock = pygame.time.Clock()
	snake_body_x = 425
	snake_body_y = 550//2
	snake_body = 16
	count = 0
	pending_turn = []
	player_snake = Snake(game_display, colours["orange"], colours["bright_orange"], display_width, display_height, snake_body_x, snake_body_y)
	apple_image = pygame.image.load("new_apple.png")
	apple_image.convert_alpha()
	apple_image = pygame.transform.scale(apple_image, (50, 50))
	apple_image_two = pygame.transform.scale(apple_image, (30,30))
	hit_position, apple_position = create_apple(player_snake)

	not_crashed = True
	while not_crashed:

		#if the player's snake exceeds the boundaries of the screen or hits any part of its body (visually) then it will end the game by changing not_crashed.
		if player_snake.head[0] >= 650 or player_snake.head[0] <=150 or player_snake.head[1] <= 50 or player_snake.head[1] >= 550:
			not_crashed = False
		for a in range(len(player_snake.body)-1):
			if (player_snake.head[0] >= player_snake.body[a][0]-8 and player_snake.head[0] <= player_snake.body[a][0]+8) and (player_snake.head[1] >= player_snake.body[a][1]-8 and player_snake.head[1] <= player_snake.body[a][1]+8):
				not_crashed = False


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			#if the player presses a directional key, set a turn-point at which each part of the body will change direction. The head of the snake must also change the direction at which it is looking.
			if event.type == pygame.KEYDOWN:
				x = player_snake.head[0]
				y = player_snake.head[1]

				if event.key == pygame.K_p:
					paused()

				elif event.key == pygame.K_LEFT and player_snake.head_direction != "right":
					player_snake.turns[arrange_turns(player_snake, "left", x, y)] = "left"

				elif event.key == pygame.K_RIGHT and player_snake.head_direction != "left":
					player_snake.turns[arrange_turns(player_snake, "right", x, y)] = "right"

				elif event.key == pygame.K_UP and player_snake.head_direction != "down":
					player_snake.turns[arrange_turns(player_snake, "up", x, y)] = "up"

				elif event.key == pygame.K_DOWN and player_snake.head_direction != "up":
					player_snake.turns[arrange_turns(player_snake, "down", x, y)] = "down"
		
		#For every screen refresh, we want to update the game background and re-blit images to the screen. This is because the score and player's snake body changes and we do not want them to overwrite the background.
		create_game_background(game_display, colours, display_width, display_height)
		game_display.blit(apple_image_two, (0,0))
		show_score(count, colours["black"], game_display)
		game_display.blit(apple_image, (apple_position))
		player_snake.create_snake(snake_body, colours["white"], colours["black"], colours["bright_red"], colours["sky_blue"])

		#if the player snake's head reaches the co-ordinate of the apple, we must increase the count for the score, generate a random location for the new apple and increase the size of the player's snake by one.
		if player_snake.head == hit_position:
			new_body_direction = player_snake.direction[0]

			if player_snake.direction[0] == "right":
				player_snake.body.insert(0, (player_snake.body[0][0]-24, player_snake.body[0][1]))
				player_snake.direction.insert(0, new_body_direction)
			elif player_snake.direction[0] == "left":
				player_snake.body.insert(0, (player_snake.body[0][0]+24, player_snake.body[0][1]))
				player_snake.direction.insert(0, new_body_direction)
			elif player_snake.direction[0] == "up":
				player_snake.body.insert(0, (player_snake.body[0][0], player_snake.body[0][1]+24))
				player_snake.direction.insert(0, new_body_direction)
			elif player_snake.direction[0] == "down":
				player_snake.body.insert(0, (player_snake.body[0][0], player_snake.body[0][1]-24))
				player_snake.direction.insert(0, new_body_direction)

			hit_position, apple_position = create_apple(player_snake)
			count += 1
			
		player_snake.update()
		pygame.display.update()
		clock.tick(60)

	if not_crashed == False:
		time.sleep(0.5)
		return

def text_object(text, font):
	text_surface = font.render(text, True, colours["white"])
	return text_surface,text_surface.get_rect()



pygame.init()
display_height = 600
display_width = 800
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
colours = {"white":(255,255,255), "black":(0,0,0), "bright_red":(255,0,0), "red":(200,0,0),
		 "bright_green":(0,255,0), "green":(0,180,0), "dark_green":(0,140,0), 
		 "grey":(166,166,166), "sky_blue":(132,206,250), "dark_blue":(0,0,255), 
		 "bright_orange": (255,83,0), "orange":(255,140,0)}

#Begins the game and runs the main menu. This allows for stacks to be removed 
activity = main_menu(display_width, display_height, game_display, colours)

while True:
	start_game(display_width, display_height, game_display, colours)
	crashed(game_display, colours, display_height, display_width)
	