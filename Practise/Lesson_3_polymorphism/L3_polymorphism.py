import random

class Hero:

    def __init__(self, HP, class_hero, damage, armor, lucky):
        self.HP = HP
        self.class_hero = class_hero
        self.damage = damage
        self.armor = armor
        self.lucky = lucky

    def get_damage(self):
        return self.damage

    def attack(self):
        print(f"I'm {self.class_hero} and attacking now!")
        print(f'My damage is {self.get_damage()}')
        return self.get_damage()

class Warrior(Hero):

    def __init__(self, HP, class_hero, damage, armor, lucky):
        super().__init__(HP, class_hero, damage, armor, lucky)

    def attack(self):
        print(f"I'm {self.class_hero} and attacking now with sword!")
        print(f'My damage is {self.get_damage()}')
        return self.get_damage()


class SpiderMan(Hero):

    def __init__(self, HP, class_hero, damage, armor, lucky):
        super().__init__(HP, class_hero, damage, armor, lucky)

    def attack(self):
        print(f"I'm {self.class_hero} and attacking now by surprise!")
        print(f'My damage is {self.get_damage()}')
        return self.get_damage()


class SuperMan(Hero):

    def __init__(self, HP, class_hero, damage, armor, lucky):
        super().__init__(HP,class_hero, damage, armor, lucky)




class Enemy:

    def __init__(self, HP, class_enemy, damage, armor):
        self.HP = HP
        self.class_enemy = class_enemy
        self.damage = damage
        self.armor = armor
        self.is_alive = True

    def defence(self, damage_of_hero, lucky_of_hero, hero='Hero'):
        self.armor = self.armor - (damage_of_hero * (lucky_of_hero) * 0.1)
        if (self.armor < 0):
            self.HP = self.HP - 100
        print(f"I'm {self.class_enemy}. Injuries taken! armor: {self.armor}, HP: {self.HP}.")

        if self.HP < 0:
            self.is_alive = False

    def check_is_alive(self):
        return self.is_alive

class Goblin(Enemy):

    def __init__(self, HP, class_enemy, damage, armor):
        super().__init__(HP, class_enemy, damage, armor)

    def defence(self, damage_of_hero, lucky_of_hero, hero='Hero'):
        if hero == 'SpiderMan':
            self.HP = 0
            self.armor = 0
            self.is_alive = False
            print(f"I'm {self.class_enemy}. It's over. I'm dead!")
        else:
            self.armor = self.armor - (damage_of_hero * (lucky_of_hero) * 0.1)

        if (self.armor < 0):
            self.HP = self.HP - 100
        print(f"I'm {self.class_enemy}. Injuries taken! armor: {self.armor}, HP: {self.HP}.")

        if self.HP < 0:
            self.is_alive = False


class Orc(Enemy):

    def __init__(self, HP, class_enemy, damage, armor):
        super().__init__(HP, class_enemy, damage, armor)


def war(list_of_hero, list_of_enemy):
    i = 1
    while list_of_enemy:
        print(f"CLASH - {i}")
        i += 1
        defender = random.randint(0, len(list_of_enemy)-1)
        attacker = random.randint(0, len(list_of_hero)-1)
        damage = list_of_hero[attacker].attack()
        hero_class = list_of_hero[attacker].class_hero
        lucky_of_hero = list_of_hero[attacker].lucky
        list_of_enemy[defender].defence(damage, lucky_of_hero, hero_class)
        p = list_of_enemy[defender].check_is_alive()
        if not p:
            del_enemy = list_of_enemy[defender]
            list_of_enemy.remove(del_enemy)
        print("X" * 80)






warrior = Warrior(400, "Warrior", 45, 200, 20)
warrior2 = Warrior(600, "Warrior", 65, 210, 40)
warrior3 = Warrior(400, "Warrior", 45, 180, 30)

spiderman = SpiderMan(100, "SpiderMan", 10, 100, 70)
spiderman2 = SpiderMan(120, "SpiderMan", 10, 170, 60)
spiderman3 = SpiderMan(105, "SpiderMan", 10, 90, 67)

superman = SuperMan(500, "SuperMan", 300, 140, 10)
superman2 = SuperMan(500, "SuperMan", 350, 140, 15)
superman3 = SuperMan(500, "SuperMan", 310, 160, 20)

goblin = Goblin(600, "Goblin", 45, 140)
goblin1 = Goblin(600, "Goblin", 45, 140)

orc = Orc(800, "Orc", 55, 200)
orc1 = Orc(800, "Orc", 55, 200)

list_of_heros = [warrior, warrior2, warrior3, spiderman, spiderman2, spiderman3, superman, superman2, superman3]
list_of_enemy = [goblin, goblin1, orc, orc1]

war(list_of_heros,list_of_enemy)