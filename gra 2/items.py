import random

class Item:
    def __init__(self, name, effect, quantity=1):  # Dodaj atrybut quantity
        self.name = name
        self.effect = effect
        self.quantity = quantity  # Ustaw domyślną wartość quantity na 1

    def use(self, target):
        if self.effect == "heal":
            target.health += 20
            print(f"{target.name} uses {self.name}. Health is now {target.health}.")
        elif self.effect == "strength":
            target.attack_power += 5
            print(f"{target.name} uses {self.name}. Attack power is now {target.attack_power}.")
        elif self.effect == "magic":
            damage = random.randint(10, 20)
            target.health -= damage
            print(f"{target.name} uses {self.name}. Deals {damage} magic damage to the enemy.")
        else:
            print("Nothing happens.")

class Inventory:
    def __init__(self):
        self.items = {
            "health potion": Item("Health Potion", "heal"),
            "strength potion": Item("Strength Potion", "strength"),
            "magic scroll": Item("Magic Scroll", "magic")
        }

    def use_item(self, item_name, target):
        if item_name in self.items and self.items[item_name].quantity > 0:  
            self.items[item_name].use(target)
            self.items[item_name].quantity -= 1  
        else:
            print(f"No {item_name} left or item doesn't exist!")