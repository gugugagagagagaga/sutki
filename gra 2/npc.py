import random
from player import Player
from utils import display_message

class NPC:
    def __init__(self, name, quest_description):
        self.name = name
        self.quest_description = quest_description

    def offer_quest(self, player):
        display_message(f"{self.name}: Hello, traveler! I have a quest for you: {self.quest_description}")
        accept_quest = input("Do you accept this quest? [Y]es/[N]o: ").lower()
        if accept_quest == 'y':
            display_message("Quest accepted!")
            # Tutaj możesz dodać logikę związana z akceptacją zadania
        else:
            display_message("Maybe next time!")

class Map:
    def __init__(self):
        self.enemies = ["Goblin", "Troll", "Orc", "Dragon", "Dark Wizard"]
        self.npcs = [NPC("Blacksmith", "Retrieve the legendary sword from the ruins."),
                     NPC("Witch", "Collect 10 herbs from the forest.")]

    def explore_location(self, location, progress, player):
        display_message(f"Exploring the {location}...")
        
        # Losowanie przeciwnika lub NPC
        encounter = random.choice(["enemy", "npc"])
        
        if encounter == "enemy":
            self.encounter_enemy(location, player)
        elif encounter == "npc":
            self.encounter_npc(location, player)

    def encounter_enemy(self, location, player):
        # Implementacja spotkania z przeciwnikiem
        pass

    def encounter_npc(self, location, player):
        npc = random.choice(self.npcs)
        display_message(f"You encounter {npc.name} in the {location}!")
        npc.offer_quest(player)