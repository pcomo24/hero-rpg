#!/usr/bin/env python3

"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
class Hero:
    def __init__(self, health, power, attack):
        self.health = health
        self.power = power
        self.attack = attack
    def attack(enemy):
            goblin_health -= hero_power
            print("You do {} damage to the goblin.".format(hero_power))
            if goblin_health <= 0:
                print("The goblin is dead.")
        elif inpt == "2":
            pass
        elif inpt == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid inpt {}".format(inpt))


hero_stats = Hero(10, 5)

class Goblin(Hero):
    pass

goblin_stats = Goblin(6,2)


#def main():
#    hero_health = 10
#    hero_power = 5
#    goblin_health = 6
#    goblin_power = 2

    while goblin_health > 0 and hero_health > 0:
        print("You have {} health and {} power.".format(hero_health, hero_power))
        print("The goblin has {} health and {} power.".format(goblin_health, goblin_power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        inpt = input()
        if inpt == "1":
            # Hero attacks goblin
#            goblin_health -= hero_power
#            print("You do {} damage to the goblin.".format(hero_power))
#            if goblin_health <= 0:
#                print("The goblin is dead.")
#        elif inpt == "2":
#            pass
#        elif inpt == "3":
#            print("Goodbye.")
#            break
#        else:
#            print("Invalid inpt {}".format(inpt))

        if goblin_health > 0:
            # Goblin attacks hero
            hero_health -= goblin_power
            print("The goblin does {} damage to you.".format(goblin_power))
            if hero_health <= 0:
                print("You are dead.")

if __name__ == "__main__":
  main()
