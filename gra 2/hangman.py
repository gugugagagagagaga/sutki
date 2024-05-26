import random

def get_random_word():
    words = ["python", "javascript", "hangman", "challenge", "openai"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def play_hangman():
    word_to_guess = get_random_word()
    guessed_letters = set()
    attempts_left = 6

    print("Welcome to Hangman!")
    while attempts_left > 0:
        print(f"Word: {display_word(word_to_guess, guessed_letters)}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Attempts left: {attempts_left}")

        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word_to_guess:
            guessed_letters.add(guess)
            print("Correct guess!")
        else:
            guessed_letters.add(guess)
            attempts_left -= 1
            print("Incorrect guess.")

        if all(letter in guessed_letters for letter in word_to_guess):
            print(f"Congratulations! You guessed the word: {word_to_guess}")
            break
    else:
        print(f"Game over! The word was: {word_to_guess}")

def start_hangman_game():
    play_hangman()
