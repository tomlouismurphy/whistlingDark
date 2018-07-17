from board_create import *
from player_start import *
from movements import *
from pprint import pprint

player1.first_words = input("hello? world? >>> ")

if player1.first_words == '':
	print("You're very quiet. But are you listening?")
else:
	print("We all know a little bit more about you now. Which is wonderful.")

def select_location(x):
	assigned = random.randint(0, 8)
	if assigned == 0:
		top_location_array[0].inhabitants.append(x)
		x.location = 'top left'
	elif assigned == 1:
		top_location_array[1].inhabitants.append(x)
		x.location = 'top middle'
	elif assigned == 2:
		top_location_array[2].inhabitants.append(x)
		x.location = 'top right'
	elif assigned == 3:
		middle_location_array[0].inhabitants.append(x)
		x.location = 'middle left'
	elif assigned == 4:
		middle_location_array[1].inhabitants.append(x)
		x.location = 'middle middle'
	elif assigned == 5:
		middle_location_array[2].inhabitants.append(x)
		x.location = 'middle right'
	elif assigned == 6:
		bottom_location_array[0].inhabitants.append(x)
		x.location = 'bottom left'
	elif assigned == 7:
		bottom_location_array[1].inhabitants.append(x)
		x.location = 'bottom middle'
	else:
		bottom_location_array[2].inhabitants.append(x)
		x.location = 'bottom right'

select_location(player1)
print(player1.location)

escape_complete = False

def grid_check():
	bottom_inhabitants = 0
	vert_middle_inhabitants = 0
	top_inhabitants = 0
	left_inhabitants = 0
	hori_middle_inhabitants = 0
	right_inhabitants = 0
	for x in all_positions:
		for y in x:
			if len(y.inhabitants) > 0:
				protag = y.inhabitants[0]
				if y.yPos == 0:
					bottom_inhabitants += 1
				elif y.yPos == 1:
					vert_middle_inhabitants += 1
				else:
					top_inhabitants += 1
	for x in all_positions:
		for y in x:
			if len(y.inhabitants) > 0:
				protag = y.inhabitants[0]
				if y.xPos == 0:
					left_inhabitants += 1
				elif y.xPos == 1:
					hori_middle_inhabitants += 1
				else:
					right_inhabitants += 1
	if (bottom_inhabitants == 1):
		if (left_inhabitants == 1):
			print("The fog obscures much. You can see walls to your south and west - what lies north and east is unclear.")
		elif (hori_middle_inhabitants == 1):
			print("The fog obscures much. You can see a wall to your south - what lies north, east and west is unclear.")
		else:
			print("The fog obscures much. You can see walls to your south and east - what lies north and west is unclear.")
	elif (vert_middle_inhabitants == 1):
		if (left_inhabitants == 1):
			print("The fog obscures much. You can see a wall to your west - what lies north, east and south is unclear.")
		elif (hori_middle_inhabitants == 1):
			print("The fog obscures much. What lies north, east, south and west is unclear.")
		else:
			print("The fog obscures much. You can see a wall to your east - what lies north, south and west is unclear.")
	elif (top_inhabitants == 1):
		if (left_inhabitants == 1):
			print("The fog obscures much. You can see walls to your north and west - what lies east and south is unclear.")
		elif (hori_middle_inhabitants == 1):
			print("The fog obscures much. You can see a wall to your north - what lies east, south and west is unclear.")
		else:
			print("The fog obscures much. You can see walls to your north and east - what lies south and west is unclear.")
	else:
		pass

def move_one(x):
	chosen_position = input(">>> ")
	chosen_position = chosen_position.lower()
	x.direction_momentary = parse_direction_input(chosen_position)
	print(x.direction_momentary)
	if (x.direction_momentary == 'north'):
		if (len(top_location_array[0].inhabitants) == 1 or len(top_location_array[1].inhabitants) == 1 or len(top_location_array[2].inhabitants) == 1):
			check_wall(x)
		else:
			move_north(x)
	elif (x.direction_momentary == 'east'):
		if (len(top_location_array[2].inhabitants) == 1 or len(middle_location_array[2].inhabitants) == 1 or len(bottom_location_array[2].inhabitants) == 1):
			check_wall(x)
		else:
			move_east(x)
	elif (x.direction_momentary == 'south'):
		if (len(bottom_location_array[0].inhabitants) == 1 or len(bottom_location_array[1].inhabitants) == 1 or len(bottom_location_array[2].inhabitants) == 1):
			check_wall(x)
		else:
			move_south(x)
	elif (x.direction_momentary == 'west'):
		if (len(top_location_array[0].inhabitants) == 1 or len(middle_location_array[0].inhabitants) == 1 or len(bottom_location_array[0].inhabitants) == 1):
			check_wall(x)
		else:
			move_west(x)
	else:
		print('Rocks fall, everyone dies.')
	print(player1.location)

def parse_direction_input(x):
	if (x == 'n' or x == 'go n' or x == 'go north'):
		north = 'north'
		return north
	elif (x == 'e' or x == 'go e' or x == 'go east'):
		east = 'east'
		return east
	elif (x == 's' or x == 'go s' or x == 'go south'):
		south = 'south'
		return south
	elif (x == 'w' or x == 'go w' or x == 'go west'):
		west = 'west'
		return west
	else:
		return x

while (player1.escaped_arena != True):
	grid_check()
	move_one(player1)