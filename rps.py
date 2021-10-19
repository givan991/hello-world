import random

computer_choice = random.randint(0,2)
if computer_choice == 0:
    computer_choice_str = 'rock'
elif computer_choice == 1:
    computer_choice_str = 'paper'
elif computer_choice == 2:
    computer_choice_str = 'scissors'

user_choice_str = input('Do you want rock, paper or scissors?\n')
if user_choice_str == 'rock':
    user_choice = 0
elif user_choice_str == 'paper':
    user_choice = 1
elif user_choice_str == 'scissors':
    user_choice = 2
else:
    print('Wrong input!')

print('\nComputer chose ' + computer_choice_str + '.')

if user_choice-computer_choice == 0:
    print('Tie!')
elif (user_choice-computer_choice == 1) or (user_choice-computer_choice == -2):
    print('User wins!')
else:
    print('Computer wins!')
