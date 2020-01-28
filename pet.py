import sys

class pet:
    def __init__(self, name):
        self.name = name
        self.happiness = 4
        self.hunger = 3

    def add_happiness(self):
        self.happiness += 1

    def sub_hunger(self):
        self.hunger -= 1
        
    def get_happiness(self):
        return self.happiness

    def get_hunger(self):
        return self.hunger
    
# New pet
def new_pet():
    try:
        name = str(input("Please enter a name: "))
        new_pet = pet(name)
        print(new_pet)
    except: 
        print('Error, please write a name')
    return new_pet

def feed(pet):
    try:
        pet.add_happiness()
    except:
        print('Create pet.')

def play(pet):
    try:
        pet.sub_hunger()
    except:
        print('Create pet.')

def check_pet(pet_name):
    try:
        hunger = pet_name.get_hunger()
        happiness = pet_name.get_happiness()
        print(hunger)
        print("Hunger :" + str(hunger) + "\n Happiness :" + str(happiness) )
    except:
        print('Create pet.')

def game():
    exit = 0
    pet = ()
    while exit == 0 :
        user_input = int(input("""Enter 1 to create pet\nEnter 2 to feed pet\nEnter 3 to play with pet\nEnter 4 to check on pet\nEnter 5 to exit game\nPlease enter a number: """))
        print(user_input)
        if user_input == 1:
            pet = new_pet()
        elif user_input == 2:
            feed(pet)
        elif user_input == 3:
            play(pet)
        elif user_input == 4:
            check_pet(pet)
        elif user_input == 5:
            exit == 1
            print("Game Over!")
            sys.exit()

game()