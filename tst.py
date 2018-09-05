class Characters(object):
    def __init__(self, name, description, hp, base_att, base_def, base_spd):
        self.name = name
        self.description = description
        self.hp = hp
        self.base_att = base_att
        self.base_def = base_def
        self.base_spd = base_spd

class MainChar(Characters):
    def __init__(self):
        super().__init__(name="Manel", description = "Low level fighter", hp = 100, base_att = 10, base_def = 10, base_spd = 10)

start = MainChar()
