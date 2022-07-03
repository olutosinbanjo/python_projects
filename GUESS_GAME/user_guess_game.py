"""

A Guessing game: The computer generates a secret number for the player to guess

03-07-2022

"""

import random

# user does not have any limit
def unlimited_user_guess(user_name, x):
    
    number = random.randint(1, x)
    guess = 0

    while (guess != number):
        guess = int(input(f"Make a guess between 1 and {x}: "))
        print('\n')
        if (guess < number):
            print("Low, make another guess!\n")
        elif (guess > number):
            print("High, make another guess!\n")
                
    print("Exact! You guessed the number correctly\n")
    print(f"Well done, {user_name}!\n")


# user has only 3 trials to play game      
def limited_user_guess(user_name, x):

    number = random.randint(1, x)
    trial_limit = 0
    guess = 0

    while (guess != number):
            
        if (trial_limit != 3):
            trial_limit += 1
            trial_left = 3 - trial_limit
            
            if (trial_left <= 1):
                print(f"Trial {trial_limit}: You have {3 - trial_limit} trial left, guess right!\n")
            else:
                print(f"Trial {trial_limit}: You have {3 - trial_limit} trials left, guess right!\n")
                
            guess = int(input(f"Make a guess between 1 and {x}: "))
            print('\n')
            if (guess < number):
                if (trial_left != 0):
                    print("Low, make another guess!\n")
                else:
                    print("Low!\n")
            elif (guess > number):
                if (trial_left != 0):
                    print("High, make another guess!\n")
                else:
                    print("High!\n")
            elif (guess == number):      
                print("Exact! You guessed the number correctly\n")
                print(f"Well done, {user_name}!\n")

        else:
           print(f"Sorry {user_name}, you have exceeded the number of trials!\n")
           print(f"You should have guessed {number}\n")
           print("Play again!")
           exit()


def main():
    
    user_name = input("Enter player name: ")
    print('\n')
    print(f"Hey {user_name}, this is a guess game!\n")
    print('INSTRUCTION: The Computer will generate a secret number from "1" to "x". Then, you are are to guess the generated number.')
    print('             "1" is the lower bound and "x" is the upper bound for generated number\n')
    
    type_play = int(input("Enter 0 for unlimited play and 1 for limited play: "))
    print('\n')
    
    if(type_play == 0):
        print("You have selected the unlimited play\n")
        upper_number = int(input("Enter upper bound (x): "))
        print('\n')
        unlimited_user_guess(user_name, upper_number)
    else:
        print("You have selected the limited play, you have only 3 trials. Good luck!\n")
        upper_number = int(input("Enter upper bound (x): "))
        print('\n')
        limited_user_guess(user_name, upper_number)

main()

