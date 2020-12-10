temp_chars = []
class Character:
    def __init__(self, name, strength, dexterity, intelligence, location=None):
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.hp = strength
        self.mana = intelligence
        self.location = location
        temp_chars.append(self)

    @property
    def max_hp(self):
        return self.strength
    
    @property
    def max_mana(self):
        return self.intelligence

