class Animal:
    
    @staticmethod
    def intro():
        print("Cat vs Dog is an entertaining game in which\n these two characters, a dog and a cat,\n they will face each other in a\n battle throwing things at each other.")
        print("To throw the objects you will have to\n maintain the finger on top of your character.\n Take into account the wind strength.")
        print("-------------------------------------------")
              
    def __init__(self, role, name, color, hp, atk, defense):
        self.role = role
        self.name = name
        self.color = color
        self.hp = hp   # the animal's health points
        self.atk = atk   # the animal's attack power
        self.defense = defense  # the animal's defense power
        
    def declare(self):
        print(f"I am a {self.role}. My name is {self.name}.")
        print(f"I am {self.color}. My HP is {self.hp}.")
        print(f"My attacking power is {self.atk}.")
        print(f"My defense is {self.defense}.")
        print("-------------------------------------------")
        
    def win(self):
        print(f"{self.role} {self.name} Wins!")

    def attack(self,enemy):
        if enemy.hp>self.atk:
            enemy.hp = enemy.hp - self.atk        
        else:
            enemy.hp = 0
    
# create instance - cat
cat = Animal('Cat', 'Carl', 'blue', 30, 5, 3)

# create instance - dog
dog = Animal('Dog', 'Doug', 'grey', 28, 7, 2)

lion = Animal('Lion','Larry', 'yellow', 100, 30, 20)

cat.declare()
dog.declare()
lion.declare()
cat.attack(lion)
lion.declare()
