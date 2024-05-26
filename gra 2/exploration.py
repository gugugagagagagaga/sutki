import random
from utils import display_message
from enemy import Enemy
from quests import QuestManager

class Map:
    def explore_location(self, location, player, quest_manager):
        display_message(f"You explore the {location}.")
        event = random.choice(["enemy", "npc", "nothing"])
        if event == "enemy":
            enemy = Enemy("Wild Boar", 50, 10)
            display_message(f"You encounter a {enemy.name}!")
            self.battle(player, enemy)
        elif event == "npc":
            display_message("You meet an NPC with a quest for you.")
            quest_manager.start_side_quest(player)
        else:
            display_message(f"You find nothing special in the {location}.")

    def battle(self, player, enemy):
        while player.is_alive() and enemy.is_alive():
            display_message(f"{player.name} Health: {player.health}")
            display_message(f"{enemy.name} Health: {enemy.health}")
            action = input(f"{player.name}, choose your action: [A]ttack, [D]efend, [U]se item: ").lower()
            if action == 'a':
                player.attack(enemy)
                if enemy.is_alive():
                    enemy.attack(player)
            elif action == 'd':
                player.defend(enemy)
                if enemy.is_alive():
                    enemy.attack(player)
            elif action == 'u':
                player.use_item()
                if enemy.is_alive():
                    enemy.attack(player)
            else:
                display_message("Invalid action. Try again.")
        if player.is_alive():
            display_message(f"You defeated the {enemy.name}.")
        else:
            display_message("Game Over.")
