import random

#* an introduction, if input == yes --> continue, if input == no --> end the game
#* the game starts with a normal game mechanism
#* the type of enemy spawned depends on the random number generator (make a list of 5 enemies)
#* if the player encounters new enemy --> NEW HERO is printed to the enemy's name
#* if the player chooses to fight the enemy (fight == yes) --> fight method is running
#* if the player chooses to run away (fight == no) --> skipped the fight and encounter another enemy
#* if the player encounters the enemy a second time, APPEAR AGAIN is printed to the enemye's name
#* if the player's armor == 0, player's health is impacted, if both player's armor and health is zero, the game ends

#*! Make the main class Attributes --> name, health, armor, for both the player and enemy
#*! Also the methods --> introduction(), fighting()
class Attributes():
    def __init__(self, name, health, armor):
        self.name = name
        self.health = health
        self.armor = armor
    def introduction(self):
        print()
        print(f"Hail to thee, good knight {self.name}.")
        print()
        print("You are standing at the entrance to the forest full of deadly dangers.")
        print()
        print("Please defeat all the enemies, if you can.")
        print()
    def fighting_mechanism(self, enemy):
        self.enemy = enemy
        print()
        print(f"{self.name} fearlessly pounces on {enemy.name}!")
#* the damage to the player is 5, the damage to the enemy is 10
        #*! handling the player's armor and health reduction, damage reduction is always 5
        if self.armor > 0:
            self.armor = self.armor - 10
            if self.armor < 0:
                self.health = self.health + self.armor
                self.armor = 0
        elif self.armor <= 0:
            self.health = self.health - 10 
            if self.health <= 0:
                self.health == 0
        #*! handling the enemy's armor and health reduction, damage reduction is always 15
        if enemy.armor > 0:
            enemy.armor = enemy.armor - 15
            if enemy.armor < 0:
                enemy.health = enemy.health + enemy.armor
                enemy.armor = 0
        elif enemy.armor <= 0:
            enemy.health = enemy.health - 15
            if enemy.health <= 0:
                enemy.health = 0
        #*! handling the messages
        print()
        print(f"{self.name} fearlessly pounces on {enemy.name}!")
        print()
        #* fight outcome for the player
        print(f"Fight outcome for {self.name}:")
        print(f"Health level: {self.health}")
        print(f"Armor class: {self.armor}")
        #* fight outcome for the enemy
        print()
        print(f"Fight outcome for {enemy.name}:")
        print(f"Health level: {enemy.health}")
        print(f"Armor class: {enemy.armor}")
        print()
        #*! handling if the enemy died
        if enemy.health <= 0 and enemy.armor <= 0:
            print(f"{enemy.name} died by the hand of {self.name}.")
            enemies.remove(enemy)
            if enemy.name in enemies_encounter:
                del enemies_encounter[enemy.name]
        if self.health <= 0 and self.health <= 0:
            print(f"The brave knight {self.name} died in battle with enemies.")
            return False
        return True

#*! Make the object --> player and enemies, make the dictionary for enemies
player = Attributes("Richard", 100, 50)
enemies = [
    Attributes("skilled warrior", 10, 15),
    Attributes("fierce dragon", 25, 10),
    Attributes("martial sergio", 10, 5),
    Attributes("Viserion", 15, 15),
    Attributes("Drogon", 25, 15),
    Attributes("martial Peter", 10, 5)
]
enemies_encounter = dict()

#*! the game starts here
play = True
player.introduction()
while play:
    if not enemies:
        print()
        print("You have defeated all enemies, the game's ending now.")
        print("Nice try on this game!")
        print()
        exit()
    answer = input("Are you ready to go there and fight the enemies (yes/no)? ").strip().lower()
    if answer == "yes":
        print()
        print("*** Let the fight begin! ***")
        print()
        #*! choose random enemy from the enemies's object list
        enemy = random.choice(enemies)
        if enemy.name not in enemies_encounter:
            print(f"--> NEW ENEMY! {enemy.name}!")
            enemies_encounter[enemy.name] = 1
        else:
            print(f"The {enemy.name} seems to appear again!")
            enemies_encounter[enemy.name] += 1
        print(f"Health level: {enemy.health}")
        print(f"Armor class: {enemy.armor}")
        #*! asks if the player wants to fight or run away
        print()
        fight = input("Join the fight? (yes/no)? ").strip().lower()
        if fight == "yes":
            fight_decide = player.fighting_mechanism(enemy)
            if not fight_decide:
                play = False
        else:
            print("----------")
    else:
        play = False
print("This is the end of the battle.")
print("You have not defeated all the enemies, try again next time.")