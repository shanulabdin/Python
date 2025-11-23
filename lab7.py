# Game Title
print('GUESS THE COMPUTERS MOVE')

# Taking User Input
userMove = input('choose your move:')
print('You Chose', userMove.upper())


# importing method
from random import random
# Random Number
randomNumber = random()

computerMove = 'heads' if randomNumber < 0.5 else 'tails'

result = 'you WIN' if userMove == computerMove else 'you LOSE'
print('Result:', result)