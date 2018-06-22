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

def select_exit():
	selector = random.randint(0, 7)
	coin_flip = random.randint(0, 1)
	if selector == 0:
		if coin_flip == 0:
			top_left.exit = 'left'
		else:
			top_left.exit = 'top'
	elif selector == 1:
		middle_left.exit = 'left'
	elif selector == 2:
		if coin_flip == 0:
			bottom_left.exit = 'left'
		else:
			bottom_left.exit = 'bottom'
	elif selector == 3:
		top_middle.exit = 'top'
	elif selector == 4:
		bottom_middle.exit = 'bottom'
	elif selector == 5:
		if coin_flip == 0:
			top_right.exit = 'right'
		else:
			top_right.exit = 'top'
	elif selector == 6:
		middle_right.exit = 'right'
	else:
		if coin_flip == 0:
			bottom_right.exit = 'right'
		else:
			bottom_right.exit = 'bottom'

select_exit()

print(top_left.exit)
print(middle_left.exit)
print(bottom_left.exit)
print(top_middle.exit)
print(bottom_middle.exit)
print(top_right.exit)
print(middle_right.exit)
print(bottom_right.exit)

class Character:
	name = 'Argos'

player1 = Character()

player1.first_words = input("hello? world? >>> ")

if player1.first_words == '':
	print("You're very quiet. But are you listening?")
else:
	print("We all know a little bit more about you now. Which is wonderful.")