import random

print("GUESS THE NUMBER :\n\nComputer will generate a random number.\nYou have to guess that number in minimum tries\n")
 
secret_number = random.randint(1, 100)
tries = 0
guess = 0
while(guess != secret_number):
    guess = int(input("Guess a number (between 1 to 100): "))
    if(guess > secret_number):
        print("Lower...")
    elif(guess < secret_number):
        print("Higher...")
    tries += 1
 
print('You guessed it! The number was {} in {} tries'.format(guess,tries))