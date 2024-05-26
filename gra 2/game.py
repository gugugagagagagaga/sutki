from player import Player
from exploration import Map
from quests import QuestManager, SideQuest
from utils import display_message
from enemy import Boss
from Minigame import space_travel_game
from minigame_adventure import Gra2
from pacman import PacmanGame

from minigame_quizy import start_quiz_game

from hangman import start_hangman_game
from number_guessing_game import start_number_guessing_game
from rock_paper_scissors import start_rock_paper_scissors_game

class Game:
    def __init__(self):
        self.player = None
        self.map = Map()
        available_quests = [
            SideQuest(
                "Journey to the Space Station",
                "Travel through space to reach the space station and rescue the stranded astronauts.",
                "200 gold coins",
                space_travel_game
            ),
            SideQuest(
                "Adventure Quest",
                "Embark on a magical adventure to find the legendary treasure.",
                "500 gold coins",
                Gra2
            ),
            SideQuest(
                "Quiz Challenge",
                "Test your knowledge in various subjects.",
                "100 gold coins",
                start_quiz_game
            ),
            SideQuest(
                "Pacman Challenge",
                "Navigate through the maze and avoid the enemies.",
                "150 gold coins",
                PacmanGame().play
            ),
            SideQuest(
                "Hangman Challenge",
                "Guess the word before you run out of attempts.",
                "100 gold coins",
                start_hangman_game
            ),
            SideQuest(
                "Number Guessing Challenge",
                "Guess the number within limited attempts.",
                "120 gold coins",
                start_number_guessing_game
            ),
            SideQuest(
                "Rock, Paper, Scissors Challenge",
                "Play a classic game of Rock, Paper, Scissors.",
                "80 gold coins",
                start_rock_paper_scissors_game
            ),
        ]
        self.quest_manager = QuestManager(available_quests)  

    



    def start(self):
        display_message("Welcome to the Adventure Game!")
        self.player = Player()
        display_message(f"Welcome, {self.player.name}!")
        self.explore_map()

    def explore_map(self):
        while self.player.is_alive():
            display_message("Where would you like to explore?")
            choice = input("[F]orest, [C]ave, [M]ine, [Ca]stle, [L]ake, [Mo]untain, [D]esert, [V]illage, [G]raveyard, [T]ower, [S]wamp, [Vo]lcano, [B]each, [J]ungle, [P]lains, [R]uins, [Cl]iff, [Y]canyon, [I]ce Cave, [B]oss, [Q]uest, [E]xit: ").lower()
            locations = {
                'f': "forest", 'c': "cave", 'm': "mine", 'ca': "castle", 'l': "lake",
                'mo': "mountain", 'd': "desert", 'v': "village", 'g': "graveyard",
                't': "tower", 's': "swamp", 'vo': "volcano", 'b': "beach", 'j': "jungle",
                'p': "plains", 'r': "ruins", 'cl': "cliff", 'y': "canyon", 'i': "ice cave"
            }
            if choice in locations:
                location = locations[choice]
                self.map.explore_location(location, self.player, self.quest_manager)
            elif choice == 'b':
                self.start_boss_fight()
            elif choice == 'q':
                self.start_side_quest()
            elif choice == 'e':
                display_message("Exiting game.")
                break
            else:
                display_message("Invalid choice. Please try again.")

    def start_boss_fight(self):
        boss = Boss("Dark Wizard", 200, 25)
        display_message(f"You face the mighty {boss.name}!")
        while self.player.is_alive() and boss.is_alive():
            self.show_health_status(self.player, boss)
            action = input(f"{self.player.name}, choose your action: [A]ttack, [D]efend, [U]se item: ").lower()
            if action == 'a':
                self.player.attack(boss)
                if boss.is_alive():
                    boss.special_attack(self.player)
            elif action == 'd':
                self.player.defend(boss)
                if boss.is_alive():
                    boss.attack(self.player)
            elif action == 'u':
                self.player.use_item()
                if boss.is_alive():
                    boss.attack(self.player)
            else:
                display_message("Invalid action. Try again.")
        if self.player.is_alive():
            display_message("Congratulations! You have defeated the Dark Wizard.")
        else:
            display_message("Game Over.")

    def show_health_status(self, player, enemy):
        display_message(f"{player.name} Health: {player.health}")
        display_message(f"{enemy.name} Health: {enemy.health}")

    def start_side_quest(self):
        display_message("You encounter an NPC offering a side quest.")
        if self.quest_manager.start_side_quest(self.player):
            display_message("You accept the side quest.")
        else:
            display_message("You decline the side quest.")

if __name__ == "__main__":
    game = Game()
    game.start()
