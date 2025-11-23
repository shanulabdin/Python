userMove = input('choose your move:')
from random import random
computerMove = 'heads' if random() < 0.5 else 'tails'
result = 'you WIN' if userMove == computerMove else 'you LOSE'
print('Computer Move: ', computerMove)
print('You Chose', userMove.upper())
print('Result:', result)