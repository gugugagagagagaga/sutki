import random

class RockPaperScissorsGame:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.player_score = 0
        self.computer_score = 0
        self.rounds = 5
        self.current_round = 0

    def welcome_message(self):
        print("Welcome to Rock, Paper, Scissors!")
        print(f"You will play {self.rounds} rounds against the computer. Let's see who wins!")

    def get_computer_choice(self):
        return random.choice(self.choices)

    def get_player_choice(self):
        while True:
            choice = input("Enter your choice (rock, paper, or scissors): ").lower()
            if choice in self.choices:
                return choice
            print("Invalid choice. Try again.")

    def determine_winner(self, player, computer):
        if player == computer:
            return "draw"
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            return "player"
        else:
            return "computer"

    def display_choices(self, player_choice, computer_choice):
        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

    def display_round_winner(self, winner):
        if winner == "player":
            print("You win this round!")
        elif winner == "computer":
            print("Computer wins this round!")
        else:
            print("It's a draw!")

    def update_scores(self, winner):
        if winner == "player":
            self.player_score += 1
        elif winner == "computer":
            self.computer_score += 1

    def display_scores(self):
        print(f"Current Scores - Player: {self.player_score}, Computer: {self.computer_score}")

    def play_round(self):
        self.current_round += 1
        print(f"\nRound {self.current_round}")
        player_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()

        self.display_choices(player_choice, computer_choice)

        winner = self.determine_winner(player_choice, computer_choice)
        self.display_round_winner(winner)
        self.update_scores(winner)
        self.display_scores()

    def play(self):
        self.welcome_message()
        while self.current_round < self.rounds:
            self.play_round()

        self.display_final_scores()

    def display_final_scores(self):
        print("\nGame Over!")
        print(f"Final Scores - Player: {self.player_score}, Computer: {self.computer_score}")
        if self.player_score > self.computer_score:
            print("Congratulations! You win the game!")
        elif self.player_score < self.computer_score:
            print("Sorry! Computer wins the game!")
        else:
            print("It's a tie!")

    def play_again(self):
        while True:
            choice = input("Do you want to play again? (yes/no): ").lower()
            if choice == 'yes':
                return True
            elif choice == 'no':
                return False
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

def start_rock_paper_scissors_game():
    game = RockPaperScissorsGame()
    game.play()
    while game.play_again():
        game = RockPaperScissorsGame()
        game.play()

if __name__ == "__main__":
    start_rock_paper_scissors_game()
