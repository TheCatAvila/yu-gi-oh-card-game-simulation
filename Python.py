class Card():
    
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
    
    def DrawCard(self):
        print('------------------------------------------------')
        print("You have drawn this card.")
        print('------------------------------------------------')
        
    def DestroyCard(self):
        print('------------------------------------------------')
        print("This card has been sent to the graveyard.")       
        print('------------------------------------------------')
    
    def PlayCard(self):
        print('------------------------------------------------')
        print(f"The card {self.name} has been played.")       
        print('------------------------------------------------')
        
class MagicCard(Card):
    
    def __init__(self, name, desc, types):
        super().__init__(name, desc)
        self.types = types
    
    def ActivateCard(self):
        print('------------------------------------------------')
        print(f"You have activated {self.name}")
        print('------------------------------------------------')
    
    def SetCard(self):
        print('------------------------------------------------')
        print("This card has been set in the Spell & Trap Zone.")
        print('------------------------------------------------')
    
    def ViewCard(self):
        print('------------------------------------------------')
        print('Name: ', self.name)
        print('Effect: ', self.desc)
        print('Type: ', self.types)
        print('------------------------------------------------')
    
    def PlayCard(self):
        print('------------------------------------------------')
        print(f"You have activated {self.name}, a {self.types} Magic Card.")       
        print('------------------------------------------------')

class MonsterCard(Card):
    
    def __init__(self, name, desc, level, attack, defense, attribute):
        super().__init__(name, desc)
        self.level    = level
        self.attack   = attack
        self.defense  = defense
        self.attribute = attribute
    
    def AttackCard(self):
        print('------------------------------------------------')
        print(f"You are attacking with {self.name}.")
        print('------------------------------------------------')
    
    def SetCard(self):
        print('------------------------------------------------')
        print("This card has been set on the monster card field.")
        print('------------------------------------------------')
    
    def ViewCard(self):
        print('------------------------------------------------')
        print('Name: ', self.name)
        print('Effect: ', self.desc)
        print('Level: ', self.level)
        print('Attack: ', self.attack)
        print('Defense: ', self.defense)
        print('Attribute: ', self.attribute)
        print('------------------------------------------------')
    
    def PlayCard(self):
        print('------------------------------------------------')
        print(f"You have summoned {self.name}, a level {self.level} Monster.")       
        print('------------------------------------------------')

card1 = MagicCard('Mystical Space Typhoon', 'Target 1 Spell/Trap Card on the field; destroy that target.', 'Quick-Play')
card1.DrawCard()
card1.ViewCard()
card1.SetCard()
card1.PlayCard()

card2 = MonsterCard('Dark Magician', 'The ultimate wizard in terms of attack and defense.', 7, 2500, 2100, 'Dark')
card2.DrawCard()
card2.ViewCard()
card2.PlayCard()
card2.AttackCard()
