class Pirate:
    pirate_roster = []

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100
        self.has_rum = True
        self.catch_phrase = f"{self.name} says, Prepare to walk the plank"
        Pirate.pirate_roster.append(self)

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        ninja.health -= self.strength
        print(self.catch_phrase)
        return self
    


# Method to heal self with Rum
    
    def drink_rum(self):
        if self.has_rum == True:
            if self.health +15 > 100:
                self.health = 100
            else:
                self.health += 15
            print(f'{self.name} takes a swig of rum and heals 15 points')
            self.has_rum = False
        else:
            print('Oh no! The Rum is gone...ARRGGGH!')

# Special Attack
            
    def hook_attack(self,ninja):
        ninja.health -= self.strength +5
        print(f'{self.name} says, "Dead Men Tell No Tales!!"')

class PreppyPirate(Pirate):

    def __init__(self, name):
        super().__init__(name)
        self.catch_phrase = f'{self.name} attacks like a total Chad.'

    def attack(self, ninja):
        super().attack(ninja)

class GothPirate(Pirate):

    def __init__(self, name):
        super().__init__(name)
        self.catch_phrase = f'{self.name} attacks with the POWER of angst.'   
    
    def attack(self, ninja):
        super().attack(ninja)