# Game Title
print('')
print('GUESS THE COMPUTERS MOVE')

# Taking User Input
userMove = input('choose your move:')
print('You Chose', userMove)

# importing method
from random import random
# Random Number
randomNumber = random()

# Logic for Computer Move
if randomNumber < 0.5:
  computerMove = 'heads'
else:
  computerMove = 'tails'
print('Computer Chose:', computerMove)

# Determining Result
if userMove == computerMove:
  result = 'you WIN'
else:
  result = 'you LOSE'
print('Result:', result)