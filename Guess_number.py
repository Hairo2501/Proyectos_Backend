import random
import time

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("You have 5 chances to guess the correct number.")
print("")
print("Please select the difficulty level:")

print("1. Easy 10 chances")
print("2. Medium 5 chances")
print("3. Hard 3 chances")
print("")


num_aleatorio = random.randint(1, 100)

dificult = int(input("Enter your choice: "))

chances = 0
  

if dificult == 1:
    print("Great! You have selected the Easy difficulty level.")
    print("Let's start the game!")
    print("")

    while chances < 10:
        num = int(input("Enter your guest: "))
        if num != num_aleatorio:
            chances += 1
            
            if num_aleatorio > num:
                print("Incorrect! The number is greater than " + str(num) + ".")
            elif num_aleatorio < num:
                print("Incorrect! The number is less than " + str(num) + ".")
        else:
            print("Congratulations! You guessed the correct number in " + str(chances + 1) + " attempts.")
            break


        if chances == 10:
            print("Game Over")
            print("The number was " + str(num_aleatorio) + " .")   


if dificult == 2:
    print("Great! You have selected the Mediun difficulty level.")
    print("Let's start the game!")
    print("")

    while chances < 5:
        num = int(input("Enter your guest: "))
        if num != num_aleatorio:
            chances += 1
            
            if num_aleatorio > num:
                print("Incorrect! The number is greater than " + str(num) + ".")
            elif num_aleatorio < num:
                print("Incorrect! The number is less than " + str(num) + ".")
        else:
            print("Congratulations! You guessed the correct number in " + str(chances + 1) + " attempts.")
            break

            

        if chances == 5:
            print("Game Over")
            print("The number was " + str(num_aleatorio) + " .")


if dificult == 3:
    print("Great! You have selected the difficulty level.")
    print("Let's start the game!")
    print("")

    while chances < 3:
        
        num = int(input("Enter your guest: "))
        if num != num_aleatorio:
            chances += 1
            
            if num_aleatorio > num:
                print("Incorrect! The number is greater than " + str(num) + ".")
            elif num_aleatorio < num:
                print("Incorrect! The number is less than " + str(num) + ".")

        else:
            print("Congratulations! You guessed the correct number in " + str(chances + 1) + " attempts.")
            break
            


        if chances == 3:
            print("Game Over")
            print("The number was " + str(num_aleatorio) + " .")

time.sleep(60)