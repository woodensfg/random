import random

def guess_number():
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Guess the Number game!")
    print("I've selected a number between 1 and 100. Can you guess it?")

    while True:
        guess = input("Enter your guess (or 'q' to quit): ")

        # Check if the user wants to quit
        if guess.lower() == 'q':
            print("Thanks for playing! The number was:", target_number)
            break

        # Validate user input
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        # Check if the guess is correct
        if guess == target_number:
            print("Congratulations! You guessed the number", target_number, "in", attempts, "attempts!")
            break
        elif guess < target_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if __name__ == "__main__":
    guess_number()
