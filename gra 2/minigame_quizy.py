import random

class Question:
    def __init__(self, prompt, options, correct_answer):
        self.prompt = prompt
        self.options = options
        self.correct_answer = correct_answer

class Category:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

class Game:
    def __init__(self):
        self.categories = [
            Category("History", [
                Question("Who was the first president of the United States?", ["1. George Washington", "2. Thomas Jefferson", "3. Abraham Lincoln", "4. John Adams"], 1),
                Question("In which year did World War I begin?", ["1. 1905", "2. 1914", "3. 1922", "4. 1939"], 2),
                Question("Who was the first man to step on the moon?", ["1. Neil Armstrong", "2. Buzz Aldrin", "3. Yuri Gagarin", "4. Alan Shepard"], 1),
            ]),
            Category("Science", [
                Question("What is the chemical symbol for gold?", ["1. Au", "2. Ag", "3. Cu", "4. Fe"], 1),
                Question("What is the powerhouse of the cell?", ["1. Mitochondrion", "2. Nucleus", "3. Chloroplast", "4. Ribosome"], 1),
                Question("Who developed the theory of relativity?", ["1. Isaac Newton", "2. Albert Einstein", "3. Galileo Galilei", "4. Stephen Hawking"], 2),
            ]),
            Category("Music", [
                Question("Who is known as the 'King of Pop'?", ["1. Michael Jackson", "2. Madonna", "3. Prince", "4. Elvis Presley"], 1),
                Question("Which band performed the song 'Bohemian Rhapsody'?", ["1. The Beatles", "2. Queen", "3. Led Zeppelin", "4. The Rolling Stones"], 2),
                Question("Who wrote the song 'Purple Haze'?", ["1. Jimi Hendrix", "2. Kurt Cobain", "3. David Bowie", "4. Bob Dylan"], 1),
            ]),
            Category("Movies", [
                Question("Who directed the movie 'Pulp Fiction'?", ["1. Quentin Tarantino", "2. Steven Spielberg", "3. Martin Scorsese", "4. Christopher Nolan"], 1),
                Question("Which movie won the Academy Award for Best Picture in 1994?", ["1. Titanic", "2. Forrest Gump", "3. The Shawshank Redemption", "4. Schindler's List"], 2),
                Question("Who played the character 'Neo' in the movie 'The Matrix'?", ["1. Keanu Reeves", "2. Leonardo DiCaprio", "3. Tom Cruise", "4. Brad Pitt"], 1),
            ]),
            Category("Sports", [
                Question("Which country won the FIFA World Cup in 2018?", ["1. France", "2. Brazil", "3. Germany", "4. Argentina"], 1),
                Question("Who is the all-time leading scorer in NBA history?", ["1. LeBron James", "2. Kobe Bryant", "3. Michael Jordan", "4. Kareem Abdul-Jabbar"], 4),
                Question("In which city were the first modern Olympic Games held?", ["1. Athens", "2. Rome", "3. Paris", "4. London"], 1),
            ]),
        ]
        self.difficulty_levels = ["Easy", "Medium", "Hard"]
        self.current_difficulty = None
        self.current_question = None
        self.current_category = None
        self.score = 0

    def select_category(self):
        print("Select a category:")
        for index, category in enumerate(self.categories, start=1):
            print(f"{index}. {category.name}")
        choice = int(input("Your choice: "))
        self.current_category = self.categories[choice - 1]

    def select_difficulty(self):
        print("Select a difficulty level:")
        for index, level in enumerate(self.difficulty_levels, start=1):
            print(f"{index}. {level}")
        choice = int(input("Your choice: "))
        self.current_difficulty = self.difficulty_levels[choice - 1]

    def get_question(self):
        random.shuffle(self.current_category.questions)
        self.current_question = self.current_category.questions[0]

    def ask_question(self):
        print(self.current_question.prompt)
        for option in self.current_question.options:
            print(option)

    def check_answer(self, answer):
        if answer == self.current_question.correct_answer:
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect!")
        print()

    def play(self):
        print("Welcome to the Quiz Game!")
        self.select_category()
        self.select_difficulty()
        while True:
            self.get_question()
            self.ask_question()
            answer = int(input("Your answer (1-4): "))
            self.check_answer(answer)
            play_again = input("Play again? (yes/no): ").lower()
            if play_again != "yes":
                break
        print(f"Your final score: {self.score}")

def start_quiz_game():
    game = Game()
    game.play()
