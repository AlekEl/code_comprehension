#Program asks for users name and a random number between 1 and 20, then compares it with previously randomized number
#then says if the users number is smaller, bigger or equal to number randomized by the program, user has 6 tries to
#guess the number

import random #Import random module, so we can use functions from this module

guesses_taken = 0 # Assign 0 to guesses_taken variable

print('Hello! What is your name?') #Print 'Hello! What is your name?' in the console
myName = input() #Take input from the user in a form of a string and assign it to myName variable

number = random.randint(1, 20) #Randomize number from 1 to 20 and assign it to number variable
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') #Print in the console sentence with
#variable myName that contains string taken from the user

while guesses_taken < 6: #Start while loop that is executed as long as guesses_taken variable is less than 6
    print('Take a guess.') #Print 'Take a guess.' in the console
    guess = input() #Take input from user in a form of a string and assign it to guess variable
    guess = int(guess) #Change guess from string to integer

    guesses_taken += 1 #Add 1 to guesses_taken variable

    if guess < number: #Execute function inside if guess variable is smaller than number variable
        print('Your guess is too low.') #Print 'Your guess is too low.' in the console

    if guess > number: #Execute function inside if guess variable is greater than number variable
        print('Your guess is too high.') #Print 'Your guess is too high.' in the console

    if guess == number: #Execute function inside if guess variable equals number variable
        break #Come out of the while loop

if guess == number: #Execute function inside if guess variable equals number variable
    guesses_taken = str(guesses_taken) #Change guesses_taken variable from integer to string
    print('Good job, ' + myName + '! You guessed my number in ' + guesses_taken + ' guesses!') #Print sentence in
    #the console with variable myName and guesses_taken inside it

if guess != number: #Execute function inside if guess variable is not equal to number variable
    number = str(number) #Change number variable from integer to string
    print('Nope. The number I was thinking of was ' + number) #Print sentence in the console with number
    #variable at the end of it
