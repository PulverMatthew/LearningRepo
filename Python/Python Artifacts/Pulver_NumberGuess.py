import random

#Variable to keep track of if the game is still going.
gameState = False
#Generates a random number to guess.
number = random.randrange(1, 100)
#Keeps track of guesses.
guesses = 0

#Main gameloop.
while gameState == False:
        print("Guess an integer between 1-100!:\n")
        #Takes input from user.
        guess = input()
        #If the user inputs "exit", changes the game state and breaks out of the loop.
        if guess == "exit":
                gameState = True
                break
        #Else, if the casted integer guessed is too high.
        elif int(guess) > number:
                print("Too high!")
                guesses += 1
        #Else, if the casted integer guessed is too low.
        elif int(guess) < number:
                print("Too low!")
                guesses += 1  
        #Else, guess correctly and print number of guesses.
        else:
                print("You guessed correctly, you guessed in " + str(guesses) + " guesses! ")
                gameState = True
        
   
   
    
