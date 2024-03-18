class Ninja:
    ninja_roster = []

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
        Ninja.ninja_roster.append(self)
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        pirate.health -= self.strength
        print(f'{self.name} attacks!')
        return self
    
    def throw_shuriken(self, pirate):
        dmg = self.strength * .2
        print(f"{self.name} gets ready to throw {self.speed} shuriken.")
        for x in range(0, self.speed):
            print(f"{self.name} throws a shuriken dealing {(self.strength * .2):.0f} damage.")
            pirate.health -= dmg
        return self

class HolyNinja(Ninja):

    def __init__(self, name):
        super().__init__(name)
        self.holy_strength = 20
        
    def use_ninja_holy_water(self,target):
        target.health += self.holy_strength
        print(f'{self.name} sprinkles holy water on {target.name} #BLESS')

class PoliticalNinja(Ninja):
    def __init__(self, name):
        super().__init__(name)
    
    def establish_prohibition(self,target):
        target.has_rum = False
        print(f'{self.name} says, "No rum while Congress is in session!"')
