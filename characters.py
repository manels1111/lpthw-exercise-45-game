#All Characters parent class/child
class Characters(object):
    def __init__(self, name, description, hp, base_att, base_def, base_spd, level):
        self.name = name
        self.description = description
        self.hp = hp
        self.base_att = base_att
        self.base_def = base_def
        self.base_spd = base_spd
        self.level = level

    def is_alive(self):
        return self.hp > 0

class MainChar(Characters):
    inv = {"rock": "sharp pointy rock", "gold": "100 gold", "sword": "giant sword"}

    def __init__(self, name):
        super().__init__(name, description = "Low level fighter", hp = 100, base_att = 10,
        base_def = 10, base_spd = 10, level = 1)

    def inventory_look(self):
        for item in MainChar.inv:
            print(item)
        print("\n")

    def add_inv(self, item):
        item = item
        MainChar.inv['item'] = item






    def __str__(self):
        return f"Your name is {self.name}. Your're level {self.level} with attack {self.base_att}, defense of {self.base_def} and attack speed {self.base_spd}.\n"



class Monsters(Characters):
    def __init__(self, name, description, hp, base_att, base_def, base_spd, level, exp_given):
        super().__init__(name, description, hp, base_att, base_def, base_spd, level )
        self.exp_given = exp_given
    def __str__(self):
        return f" There is a {self.name} here. {self.description}, It is level {self.level} and has {self.hp} HP "



class Vendor(Characters):
    def __init__(self, name, description, forsale):
        super().__init__(name ="Exlid", description = "This vendor sales potions")
        pass
#End Characters subclasses
