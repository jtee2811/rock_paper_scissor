'''class yeet:
	def __init__(meep):
		meep.name = input('enter name = ')
		meep.age = int(input('enter age = '))

	def greet(meep):
		print('helo ' + meep.name)

ehh = yeet()
ehh.greet()
print(meep.age)'''
import random

class game:
	def __init__(meep):
		play = 'yes'
		while play == 'yes':
			meep.choice = input('rock, paper or scissors? = ')
			if meep.choice == 'rock':
				reply = random.choice(['rock', 'paper', 'scissors'])
				print(reply)
				if reply == 'scissors':
					print('you lose')
				elif reply == 'paper':
					print('you win')
				else:
					print("it's a draw")

			elif meep.choice == 'paper':
				reply2 = random.choice(['rock', 'paper', 'scissors'])
				print(reply2)
				if reply2 == 'scissors':
					print('you lose')
				elif reply2 == 'paper':
					print("it's a draw")
				else:
					print('you win')

			elif meep.choice == 'scissors':
				reply3 = random.choice(['rock', 'paper', 'scissors'])
				print(reply3)
				if reply3 == 'scissors':
					print("it's a draw")
				elif reply3 == 'paper':
					print('you win')
				else:
					print('you lose')

			play = input('would you like to play again?(yes or no) = ')

	def ehh(meep, rock, paper, scissors):
		meep.rock = rock
		meep.paper = paper
		meep.scissors = scissors

uhh = game()


