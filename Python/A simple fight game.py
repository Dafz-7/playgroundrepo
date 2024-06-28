
#* create a hero class --> with an attributes: name, health, armor, impact, weapon
#* create two object class: character(hero): richard and helen
#* with this two charaters, create an two objects with the same name
#* create a loop: play = true, while play
#* if any character experiences a death, play == false and the game ends.

#*! creation of the main class
class Hero:
    def __init__(self, name, health, armor, impact, weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.impact = impact
        self.weapon = weapon
    def introduce(self):
        print(f"Greet the hero -> {self.name}")
        print(f"Health level: {self.health}")
        print(f"Armor class: {self.armor}")
        print(f"Impact force: {self.impact}")
        print(f"Weapon: {self.weapon}")
    def strike(self, opponent):
        self.opponent = opponent
        print("-> STRIKE!")
        print(f"{self.name} attacks {opponent.name} using {self.weapon}")
        print()
        if opponent.armor > 0:
            opponent.armor = opponent.armor - self.impact
            if opponent.armor <= 0:
                opponent.health = opponent.health + opponent.armor #* the opponent.armor is going to be either a zero or a minus sign here
                opponent.armor = 0
        else:
            opponent.health = opponent.health - self.impact
        if opponent.health <= 0:
            print(f"{opponent.name} swayed.")
            print(f"Armor class dropped to {opponent.armor}")
            print(f"Health level decreased to {opponent.health}")
            print()
            print(f"{opponent.name} fell in a harsh battle.")
            return False
        print(f"{opponent.name} swayed.")
        print(f"Armor class dropped to {opponent.armor}")
        print(f"Health level decreased to {opponent.health}")
        print()
        return True

#*! creation of objects
hero1 = Hero("Richard", 50, 25, 20, "sword")
hero2 = Hero("Helen", 100, 10, 15, "bow")

#*! Start of the game
hero1.introduce()
print()
hero2.introduce()
print()
print("Let the battle begin!")

play = True
while play:
    play = hero2.strike(hero1)
    if not play:
        break
    play = hero1.strike(hero2)