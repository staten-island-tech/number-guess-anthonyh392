'''
You will be creating a program that creates a random number and then have the user guess the number. The code must contain all of the following:
- Generate a random number between 1 and 10 (you can do more if you want).
- Use a while loop that breaks only when the user correctly guesses the number.
- Create a guess variable based on user input. There will be a global guess variable equal to 0 and then another guess variable inside the while loop based on user input.
- Using conditional statements, inform the user if their guess is less than or greater than the random number.
- Push the user's incorrect guess into a guess_history list. Print the used letters at every wrong guess.
- When the user guesses correctly, inform them and show them their guess history using a for loop.
'''

# Modules
import random
import os
import time

# Clear the console to avoid clutter
os.system('cls')

# Generate the random number
random_number = random.randint(1, 1000)

# Global guess variable
guess = 0

# Initialize the global guess_history list
guess_history = []

# Use a while loop that breaks only when the user correctly guesses the number
while True:
    os.system('cls')

    guess = int(input('Input your guess: '))

    if guess < random_number:
        print('Your guess is too low! Please try again.')
        guess_history.append(f'Incorrect guess: {guess}')
        time.sleep(1.5) # Wait 1.5s before asking to guess again
    elif guess > random_number:
        print('Your guess is too high! Please try again.')
        guess_history.append(f'Incorrect guess: {guess}')
        time.sleep(1.5) # Wait 1.5s before asking to guess again
    else:
        print(f'You guessed the number correctly in {len(guess_history) + 1} attempts!')
        output = 'Your guess history:\n'

        for guess in guess_history:
            output += f'{str(guess)}\n'
        
        if output != 'Your guess history:\n':
            print(output + f'Correct guess: {random_number}')

        break