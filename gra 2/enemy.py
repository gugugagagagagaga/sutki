import random

class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, player):
        damage = random.randint(1, self.attack_power)
        player.health -= damage
        print(f"{self.name} attacks {player.name} for {damage} damage.")

    def is_alive(self):
        return self.health > 0

class Boss(Enemy):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)
        self.special_attack_power = attack_power * 2

    def special_attack(self, player):
        damage = random.randint(1, self.special_attack_power)
        player.health -= damage
        print(f"{self.name} uses special attack on {player.name} for {damage} damage.")

class MiniBoss(Enemy):
    BLOCK_CHANCE = 0.2  

    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)

    def block(self):
        if random.random() < self.BLOCK_CHANCE:
            print(f"{self.name} blocks the player's attack!")
            return True
        return False

class Dragon(Enemy):
    def __init__(self):
        super().__init__("Dragon", 150, 20)

    def special_attack(self, player):
        print(f"The mighty {self.name} breathes fire on {player.name}!")
        player.health -= 30

class Goblin(Enemy):
    def __init__(self):
        super().__init__("Goblin", 30, 5)

    def flee(self):
        print(f"{self.name} tries to run away!")
        if random.random() < 0.5:  
            print("The goblin successfully flees!")
            return True
        print("The goblin failed to flee!")
        return False

class Troll(Enemy):
    def __init__(self):
        super().__init__("Troll", 60, 8)

    def regenerate(self):
        print(f"{self.name} starts regenerating health.")
        self.health += 10

class Vampire(Enemy):
    def __init__(self):
        super().__init__("Vampire", 70, 12)

    def drain(self, player):
        damage = random.randint(1, self.attack_power)
        player.health -= damage
        self.health += damage // 2
        print(f"{self.name} drains {damage} health from {player.name} and heals for {damage // 2}.")

class Werewolf(Enemy):
    def __init__(self):
        super().__init__("Werewolf", 90, 14)

    def frenzy(self, player):
        damage = random.randint(1, self.attack_power * 2)
        player.health -= damage
        print(f"{self.name} goes into a frenzy and attacks {player.name} for {damage} damage.")

class Zombie(Enemy):
    def __init__(self):
        super().__init__("Zombie", 40, 6)

    def infect(self, player):
        print(f"{self.name} infects {player.name} with a deadly disease.")

class Demon(Enemy):
    def __init__(self):
        super().__init__("Demon", 110, 16)

    def fireball(self, player):
        damage = random.randint(10, self.attack_power)
        player.health -= damage
        print(f"{self.name} hurls a fireball at {player.name} for {damage} damage.")

class Phantom(Enemy):
    def __init__(self):
        super().__init__("Phantom", 50, 7)

    def phase_out(self, player):
        if random.random() < 0.5:
            print(f"{self.name} phases out, avoiding the next attack.")
            return True
        return False

class Hydra(Enemy):
    def __init__(self):
        super().__init__("Hydra", 130, 18)

    def regenerate_heads(self):
        additional_heads = random.randint(1, 3)
        self.attack_power += additional_heads * 2
        print(f"{self.name} regenerates {additional_heads} heads, increasing attack power to {self.attack_power}.")

def get_random_enemy():
    enemies = [
        Goblin(),
        Troll(),
        Dragon(),
        Vampire(),
        Werewolf(),
        Zombie(),
        Demon(),
        Phantom(),
        Hydra()
    ]
    return random.choice(enemies)
