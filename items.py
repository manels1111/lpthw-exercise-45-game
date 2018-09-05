#Items parent class
class Items(object):
    def __init__(self, name, description, level):
        pass

class Weapons(Items):
    def __init__(self, name, description, level, att_mod):
        super().__init__(name, description, level)
        pass

class Armor(Items):
    def __init__(self, name, description, level, def_mod):
        super().__init__(name, description, level)
        pass

class Gold(Items):
    def __init__(self, name, description, ammount):
        super().__init__(name, description)
        pass

#End Items subclasses
