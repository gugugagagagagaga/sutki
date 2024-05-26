import random

class NumberGuessingGame:
    def __init__(self):
        self.target_number = random.randint(1, 100)
        self.guesses = 0
        self.max_attempts = 10
        self.game_over = False

    def welcome_message(self):
        print("Welcome to the Number Guessing Game!")
        print("I have selected a number between 1 and 100. Can you guess it?")
        print(f"You have {self.max_attempts} attempts to guess the number.")

    def get_player_guess(self):
        while True:
            try:
                guess = int(input("Enter your guess: "))
                return guess
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def check_guess(self, guess):
        self.guesses += 1
        if guess < self.target_number:
            print("Too low!")
        elif guess > self.target_number:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number {self.target_number} in {self.guesses} attempts.")
            self.game_over = True

    def play(self):
        self.welcome_message()

        while not self.game_over and self.guesses < self.max_attempts:
            guess = self.get_player_guess()
            self.check_guess(guess)

        if not self.game_over:
            print(f"Sorry, you've used all your attempts. The number was {self.target_number}.")

    def play_again(self):
        while True:
            choice = input("Do you want to play again? (yes/no): ").lower()
            if choice == 'yes':
                return True
            elif choice == 'no':
                return False
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

def start_number_guessing_game():
    game = NumberGuessingGame()
    game.play()
    while game.play_again():
        game = NumberGuessingGame()
        game.play()

if __name__ == "__main__":
    start_number_guessing_game()