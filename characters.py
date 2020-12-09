class Character:
    temp_chars = []
    def __init__(self, name, strength, dexterity, intelligence):
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.hp = strength
        self.mana = intelligence

    @property
    def max_hp(self):
        return self.strength
    
    @property
    def max_mana(self):
        return self.intelligence

