from game import Game
from utils import display_message

def main():
    while True:
        display_message("\nMain Menu:")
        display_message("1. Start Game")
        display_message("2. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            game = Game()
            game.start()
        elif choice == '2':
            display_message("Exiting game.")
            break
        else:
            display_message("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
