import random
from random import randint


def computerchoice():
    selection = randint(0, 2)
    if selection == 0:
        computerchoice = 'Rock'
        return computerchoice
    if selection == 1:
        computerchoice = 'Scissors'
        return computerchoice
    if selection == 2:
        computerchoice = 'Paper'
        return computerchoice


def playerchoice():
    choice = input('ready? enter R, P, S to start.')
    if choice == 'r' or choice == 'R':
        play = 'Rock'
        return play
    if choice == 's' or choice == 'S':
        play = 'Scissors'
        return play
    if choice == 'p' or choice == 'P':
        play = 'Paper'
        return play

user = playerchoice()
computer = computerchoice()

if computer == user:
    print('Your Choice: ', user, '\nComputer choice: ', computer)
    print("looks like it's a tie")
elif computer == 'Rock':
    if user == 'Paper':
        print('Your choice: ', user, '\nComputer chose', computer)
        print('Paper covers rock!! win!')
    else:
        print('Your choice: ', user, ',\nComputer choice: ', computer)
        print('unlucky,', computer, 'beats', user)
elif computer == 'Scissors':
    if user == 'Rock':
        print('Your Choice: ', user, '\nComputer choice: ', computer)
        print('Rock blunts scissors!! win!')
    else:
        print('Your Choice: ', user, '\nComputer choice: ', computer)
        print('unlucky,', computer, 'beats', user)
elif computer == 'Paper':
    if user == 'Scissors':
        print('Your Choice: ', user, '\nComputer choice: ', computer)
        print('Scissors cuts paper! win!')
    else:
        print('Your Choice: ', user, '\nComputer choice: ', computer)
        print('unlucky,', computer, 'beats', user)


