from board_create import *

class Character:
	name = 'Argos'
	location = ''

player1 = Character()

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

def move_north(x):
	if player1.location == 'middle left':
		middle_location_array[0].inhabitants.remove(x)
		top_location_array[0].inhabitants.append(x)
		x.location = 'top left'
	elif player1.location == 'middle middle':
		middle_location_array[1].inhabitants.remove(x)
		top_location_array[1].inhabitants.append(x)
		x.location = 'top middle'
	elif player1.location == 'middle right':
		middle_location_array[2].inhabitants.remove(x)
		top_location_array[2].inhabitants.append(x)
		x.location = 'top right'
	elif player1.location == 'bottom left':
		bottom_location_array[0].inhabitants.remove(x)
		middle_location_array[0].inhabitants.append(x)
		x.location = 'middle left'
	elif player1.location == 'bottom middle':
		bottom_location_array[1].inhabitants.remove(x)
		middle_location_array[1].inhabitants.append(x)
		x.location = 'middle middle'
	elif player1.location == 'bottom right':
		bottom_location_array[2].inhabitants.remove(x)
		middle_location_array[2].inhabitants.append(x)
		x.location = 'middle right'
	else:
		pass

def move_east(x):
	if player1.location == 'top left':
		top_location_array[0].inhabitants.remove(x)
		top_location_array[1].inhabitants.append(x)
		x.location = 'top middle'
	elif player1.location == 'top middle':
		top_location_array[1].inhabitants.remove(x)
		top_location_array[2].inhabitants.append(x)
		x.location = 'top right'
	elif player1.location == 'middle left':
		middle_location_array[0].inhabitants.remove(x)
		middle_location_array[1].inhabitants.append(x)
		x.location = 'middle middle'
	elif player1.location == 'middle middle':
		middle_location_array[1].inhabitants.remove(x)
		middle_location_array[2].inhabitants.append(x)
		x.location = 'middle right'
	elif player1.location == 'bottom left':
		bottom_location_array[0].inhabitants.remove(x)
		bottom_location_array[1].inhabitants.append(x)
		x.location = 'bottom middle'
	elif player1.location == 'bottom middle':
		bottom_location_array[1].inhabitants.remove(x)
		bottom_location_array[2].inhabitants.append(x)
		x.location = 'bottom right'
	else:
		pass

def move_south(x):
	if player1.location == 'top left':
		top_location_array[0].inhabitants.remove(x)
		middle_location_array[0].inhabitants.append(x)
		x.location = 'middle left'
	elif player1.location == 'top middle':
		top_location_array[1].inhabitants.remove(x)
		middle_location_array[1].inhabitants.append(x)
		x.location = 'middle middle'
	elif player1.location == 'top right':
		top_location_array[2].inhabitants.remove(x)
		middle_location_array[2].inhabitants.append(x)
		x.location = 'middle right'
	elif player1.location == 'middle left':
		middle_location_array[0].inhabitants.remove(x)
		bottom_location_array[0].inhabitants.append(x)
		x.location = 'bottom left'
	elif player1.location == 'middle middle':
		middle_location_array[1].inhabitants.remove(x)
		bottom_location_array[1].inhabitants.append(x)
		x.location = 'bottom middle'
	elif player1.location == 'middle right':
		middle_location_array[2].inhabitants.remove(x)
		bottom_location_array[2].inhabitants.append(x)
		x.location = 'bottom right'
	else:
		pass

def move_west(x):
	if player1.location == 'top middle':
		top_location_array[1].inhabitants.remove(x)
		top_location_array[0].inhabitants.append(x)
		x.location = 'top left'
	elif player1.location == 'top right':
		top_location_array[2].inhabitants.remove(x)
		top_location_array[1].inhabitants.append(x)
		x.location = 'top middle'
	elif player1.location == 'middle middle':
		middle_location_array[1].inhabitants.remove(x)
		middle_location_array[0].inhabitants.append(x)
		x.location = 'middle left'
	elif player1.location == 'middle right':
		middle_location_array[2].inhabitants.remove(x)
		middle_location_array[1].inhabitants.append(x)
		x.location = 'middle middle'
	elif player1.location == 'bottom middle':
		bottom_location_array[1].inhabitants.remove(x)
		bottom_location_array[0].inhabitants.append(x)
		x.location = 'bottom left'
	elif player1.location == 'bottom right':
		bottom_location_array[2].inhabitants.remove(x)
		bottom_location_array[1].inhabitants.append(x)
		x.location = 'bottom middle'
	else:
		pass

def check_wall():
	for x in all_positions:
		for y in x:
			if len(y.inhabitants) > 0:
				print(y.exit)

check_wall()