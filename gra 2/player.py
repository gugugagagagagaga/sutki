import random
from items import Inventory
from utils import display_message

class Player:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.country = input("Enter your country of birth: ")
        self.health = 100
        self.attack_power = 10
        self.defense = 5
        self.level = 1
        self.experience = 0
        self.inventory = Inventory()

    def attack(self, enemy):
        damage = random.randint(1, self.attack_power)
        enemy.health -= damage
        display_message(f"{self.name} attacks {enemy.name} for {damage} damage.")

    def defend(self, enemy):
        reduced_damage = max(0, enemy.attack_power - self.defense)
        self.health -= reduced_damage
        display_message(f"{self.name} defends against {enemy.name}. Takes {reduced_damage} damage.")

    def use_item(self):
        print("Available items:")
        for item_name, item in self.inventory.items.items():
            print(f"{item_name} (x{item.quantity})")  
        item_choice = input("Choose an item to use: ").lower()
        if item_choice in self.inventory.items:
            self.inventory.use_item(item_choice, self)
        else:
            display_message("Invalid item choice!")



    def gain_experience(self, amount):
        self.experience += amount
        display_message(f"{self.name} gains {amount} experience points.")
        if self.experience >= 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.health += 10
        self.attack_power += 2
        self.defense += 1
        self.experience = 0
        display_message(f"{self.name} leveled up! Now at level {self.level}. Health: {self.health}, Attack Power: {self.attack_power}, Defense: {self.defense}")

    def is_alive(self):
        return self.health > 0

    def receive_reward(self, reward):
        if reward == "health":
            self.health += 10
            display_message(f"{self.name} received a health reward. Health increased by 10.")
        elif reward == "attack_power":
            self.attack_power += 5
            display_message(f"{self.name} received an attack power reward. Attack power increased by 5.")
        elif reward == "defense":
            self.defense += 3
            display_message(f"{self.name} received a defense reward. Defense increased by 3.")
        else:
            display_message("Invalid reward type!")
