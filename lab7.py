from random import random
userMove = input('choose your move:')
computerMove = 'heads' if random() < 0.5 else 'tails'
result = 'you WIN' if userMove == computerMove else 'you LOSE'
print('Computer Chose: ', computerMove, ', You Chose', userMove, ', Result:', result)