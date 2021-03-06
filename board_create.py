import random

class Space:
	def __init__(self, xPos, yPos):
		self.xPos = xPos
		self.yPos = yPos
		self.inhabitants = []
		self.exit = False

top_left = Space(0, 2)
middle_left = Space(0, 1)
bottom_left = Space(0, 0)
top_middle = Space(1, 2)
middle_middle = Space(1, 1)
bottom_middle = Space(1, 0)
top_right = Space(2, 2)
middle_right = Space(2, 1)
bottom_right = Space(2, 0)

all_positions = []

top_location_array = []
middle_location_array = []
bottom_location_array = []

all_positions.append(top_location_array)
all_positions.append(middle_location_array)
all_positions.append(bottom_location_array)

top_location_array.append(top_left)
top_location_array.append(top_middle)
top_location_array.append(top_right)

middle_location_array.append(middle_left)
middle_location_array.append(middle_middle)
middle_location_array.append(middle_right)

bottom_location_array.append(bottom_left)
bottom_location_array.append(bottom_middle)
bottom_location_array.append(bottom_right)

def select_exit():
	selector = random.randint(0, 7)
	print(selector)
	coin_flip = random.randint(0, 1)
	print(coin_flip)
	if selector == 0:
		if coin_flip == 0:
			top_left.exit = 'west'
		else:
			top_left.exit = 'north'
	elif selector == 1:
		middle_left.exit = 'west'
	elif selector == 2:
		if coin_flip == 0:
			bottom_left.exit = 'west'
		else:
			bottom_left.exit = 'south'
	elif selector == 3:
		top_middle.exit = 'north'
	elif selector == 4:
		bottom_middle.exit = 'south'
	elif selector == 5:
		if coin_flip == 0:
			top_right.exit = 'east'
		else:
			top_right.exit = 'north'
	elif selector == 6:
		middle_right.exit = 'east'
	else:
		if coin_flip == 0:
			bottom_right.exit = 'east'
		else:
			bottom_right.exit = 'south'

select_exit()