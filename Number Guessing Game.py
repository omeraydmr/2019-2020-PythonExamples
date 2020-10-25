#Number Guessing Game 30.05.2020 written by omeraydmr

import random
import time

print("**************************************** \nGuess the number between 1 to 50. You have 10 rights. \n****************************************")

random_number = random.randint(1 , 50)
guess_right = 10



while True:

    number = int(input("Please guess the number: "))

    if number > random_number :
        print("Progressing...")
        time.sleep(1)
        print("Please enter less than this number.")
        guess_right -=1
        

    elif number < random_number :
        print("Progressing...")
        time.sleep(1)
        print("Please enter bigger than this number.")
        guess_right -=1
        

    else:
        print("Progressing...")
        time.sleep(1)
        print("Great job. You find the number." , random_number)
        break

    if guess_right == 0:
        print("Your rights done. Your number was" , random_number)
        break
        50